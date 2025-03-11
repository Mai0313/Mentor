# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "httpx",
#     "logfire",
#     "marker-pdf[full]>=1.6.0",
#     "openai",
#     "rich",
# ]
# ///
import os
from typing import Any
import asyncio
from pathlib import Path
import warnings

import httpx
from openai import AsyncAzureOpenAI
from autogen import config_list_from_json
import logfire
from pydantic import ConfigDict, Field, BaseModel, computed_field
from rich.console import Console
from marker.models import create_model_dict

# from PIL import Image
# from autogen.agentchat.contrib.img_utils import get_pil_image, pil_to_data_uri
# from marker.output import text_from_rendered
from marker.output import save_output
from marker.config.parser import ConfigParser
from marker.converters.pdf import PdfConverter
from autogen.agentchat.contrib.img_utils import get_pil_image, pil_to_data_uri

logfire.configure(send_to_logfire=False)


from markitdown import MarkItDown

console = Console()
warnings.filterwarnings("ignore", category=ResourceWarning)


def get_config_dict(model: str, temp: float = 0.5) -> dict[str, Any]:
    config_list = config_list_from_json(
        env_or_file="./configs/llm/OAI_CONFIG_LIST", filter_dict={"model": model}
    )
    llm_config = {
        "timeout": 60,
        "cache_seed": os.getenv("SEED", None),
        "temperature": temp,
        "config_list": config_list,
    }
    return llm_config


llm_config = get_config_dict(model="aide-gpt-4o", temp=0.3)


class DescribeImageInput(BaseModel):
    question: str = Field(..., description="The question you want to ask.")
    image_url: str = Field(
        ...,
        description="The image urls you want to describe, it should be a string of path that pair with the question.",
    )


class DescribeImagesOutput(BaseModel):
    answer: str = Field(..., description="The answer to the question you asked.")
    image_url: str = Field(
        ...,
        description="The image urls you want to describe, it should be a string of path that pair with the question.",
    )


class DocsConverter(BaseModel):
    path: str = Field(
        default="./docs",
        description="The path of the docs you want to convert, it can be either a file or a directory.",
        frozen=False,
        deprecated=False,
    )

    @computed_field
    @property
    def all_docs_paths(self) -> list[Path]:
        if Path(self.path).is_dir():
            all_docs_paths = list(Path(self.path).rglob("*"))
        elif Path(self.path).is_file():
            all_docs_paths = [Path(self.path)]
        else:
            raise ValueError(f"Invalid path: {self.path}")
        return all_docs_paths


    def to_markdown(self) -> None:
        all_docs_paths = [f for f in self.all_docs_paths if f.suffix == ".pdf"]

        if not all_docs_paths:
            console.print("No pdf files found in the path.", style="bold yellow")
            return

        config = {"languages": "en", "output_format": "markdown", "output_dir": "parsed"}
        config_parser = ConfigParser(config)

        converter = PdfConverter(
            config=config_parser.generate_config_dict(),
            artifact_dict=create_model_dict(),
            processor_list=config_parser.get_processors(),
            renderer=config_parser.get_renderer(),
            llm_service=config_parser.get_llm_service(),
        )
        for docs_path in all_docs_paths:
            output_dir = docs_path.with_suffix("")
            if output_dir.is_dir() and output_dir.exists():
                console.print(f"Skip existing dir: {output_dir.as_posix()}", style="bold yellow")
                continue
            output_dir.mkdir(parents=True, exist_ok=True)
            rendered = converter(filepath=docs_path.as_posix())
            # text, _, images = text_from_rendered(rendered)
            # for image in images:
            #     if isinstance(image, Image.Image):
            #         image_bytes = pil_to_data_uri(image=image)
            save_output(
                rendered=rendered, output_dir=output_dir.as_posix(), fname_base=docs_path.stem
            )
            console.print(f"Converted {docs_path} to {output_dir.as_posix()}", style="bold green")

    async def describe_images(
        self, image_infos: list[dict[str, str]], image_nums: int = 10
    ) -> list[DescribeImagesOutput]:
        client = AsyncAzureOpenAI(
            api_key=llm_config["config_list"][0]["api_key"],
            azure_endpoint=llm_config["config_list"][0]["base_url"],
            api_version=llm_config["config_list"][0]["api_version"],
            http_client=httpx.AsyncClient(headers=llm_config["config_list"][0]["default_headers"]),
        )

        # 使用 semaphore 限制同時只處理 image_nums 張圖片
        semaphore = asyncio.Semaphore(image_nums)

        async def process_image(image_info_dict: dict[str, str]) -> DescribeImagesOutput:
            # 使用 semaphore 控制並發數量
            async with semaphore:
                # 將 dict 轉換成描述圖片請求物件
                image_info = DescribeImageInput(**image_info_dict)
                content: list[dict[str, Any]] = [
                    {
                        "type": "text",
                        "text": "Please follow the question below to describe the image(s) you received.",
                    },
                    {"type": "text", "text": image_info.question},
                ]
                if Path(image_info.image_url).exists():
                    console.print(f"Processing {image_info.image_url}...", style="bold green")
                    # 如果圖片路徑存在，讀取圖片並轉換成 data uri 格式
                    base64_image = get_pil_image(image_file=image_info.image_url)
                    image_uri = pil_to_data_uri(base64_image)
                    content.append({"type": "image_url", "image_url": {"url": image_uri}})
                    # 呼叫 API 取得描述
                    response = await client.chat.completions.create(
                        model=llm_config["config_list"][0]["model"],
                        messages=[{"role": "user", "content": content}],
                        temperature=0.0,
                    )
                    return DescribeImagesOutput(
                        answer=response.choices[0].message.content, image_url=image_info.image_url
                    )
                # 若圖片不存在則回傳錯誤訊息
                console.print(
                    f"Cannot find the image of {image_info.image_url}, please check the image path.",
                    style="bold red",
                )
                return DescribeImagesOutput(
                    answer=f"Cannot find the image of {image_info.image_url}, please check the image path.",
                    image_url=image_info.image_url,
                )

        tasks = [process_image(image_info) for image_info in image_infos]
        # 使用 asyncio.gather 同時執行所有 tasks，且由 semaphore 限制最大並發量為 10
        return await asyncio.gather(*tasks)

    async def parse_docs_with_images(self) -> None:
        docs_paths = [f for f in self.all_docs_paths if f.name.endswith(".md")]
        docs_paths = [f for f in docs_paths if not f.stem.endswith("_parsed")]
        if not docs_paths:
            console.print("No parsed markdown files found in the path.", style="bold yellow")
            return
        for docs_path in docs_paths:
            docs_content = docs_path.read_text(encoding="utf-8")
            # Use regex to find the line starts with `![](_page` and ends with `)`
            splitted_contents = docs_content.splitlines()
            docs_parent = docs_path.parent
            image_info_list = []
            image_mapping = {}
            for line_idx, line in enumerate(splitted_contents, start=1):
                if line.startswith("![](_page") and line.endswith(")"):
                    image_path_string = line.split("](")[1].split(")")[0]
                    image_path = docs_parent / image_path_string
                    if image_path.exists():
                        image_url = image_path.absolute().as_posix()
                        image_info = {
                            "question": "Describe the image in detail.",
                            "image_url": image_url,
                        }
                        image_mapping[image_url] = line_idx
                        image_info_list.append(image_info)
            if not image_info_list:
                console.print(f"No images found in {docs_path}.", style="bold yellow")
                continue
            # For debugging
            # image_info_list = image_info_list[:5]
            parsed_images = await self.describe_images(image_infos=image_info_list, image_nums=30)
            for parsed_image in parsed_images:
                image_url = parsed_image.image_url
                line_idx = image_mapping.get(image_url)
                if line_idx:
                    splitted_contents[line_idx - 1] = (
                        f"Here is the image describtion:\n```\n{parsed_image.answer}\n```"
                    )
            parsed_content = "\n".join(splitted_contents)
            new_docs_path = docs_path.with_name(f"{docs_path.stem}_parsed{docs_path.suffix}")
            new_docs_path.write_text(parsed_content, encoding="utf-8")
            console.print(f"Parsed {docs_path} to {new_docs_path}", style="bold green")


if __name__ == "__main__":
    import fire

    # python convert_docs.py to_markdown --path="./docs/Bandgap Reference Verification_RAK.pdf"
    # python convert_docs.py to_markdown --path="./docs"
    # python scripts/convert_docs.py parse_docs_with_images --path="./docs/Bandgap References"
    # python scripts/convert_docs.py parse_docs_with_images --path="./docs"

    fire.Fire(DocsConverter)
