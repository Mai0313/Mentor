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
from autogen.agentchat.contrib.img_utils import get_pil_image, pil_to_data_uri, get_image_data

logfire.configure(send_to_logfire=False)

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


class DescribeImagesOutput(BaseModel):
    image_url: str = Field(
        ...,
        description="The image urls you want to describe, it should be a string of path that pair with the question.",
        frozen=False,
        deprecated=False,
    )
    answer: str = Field(..., description="The answer to the question you asked.", frozen=False,
        deprecated=False,)


class DocsConverter(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    path: str = Field(
        default="./docs",
        description="The path of the docs you want to convert, it can be either a file or a directory.",
        frozen=False,
        deprecated=False,
    )
    max_processes: int = Field(
        default=10,
        description="The maximum number of processes to use for conversion.",
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

    @computed_field
    @property
    def semaphore(self) -> asyncio.Semaphore:
        semaphore = asyncio.Semaphore(value=self.max_processes)
        return semaphore

    @computed_field
    @property
    def client(self) -> AsyncAzureOpenAI:
        client = AsyncAzureOpenAI(
            api_key=llm_config["config_list"][0]["api_key"],
            azure_endpoint=llm_config["config_list"][0]["base_url"],
            api_version=llm_config["config_list"][0]["api_version"],
            http_client=httpx.AsyncClient(headers=llm_config["config_list"][0]["default_headers"]),
        )
        return client

    def to_markdown(self) -> None:
        all_docs_paths = [f for f in self.all_docs_paths if f.suffix == ".pdf"]

        if not all_docs_paths:
            logfire.warn("No pdf files found in the path.")
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
                logfire.info("Skip existing dir", source=docs_path, output=output_dir.as_posix())
                continue
            output_dir.mkdir(parents=True, exist_ok=True)
            rendered = converter(filepath=docs_path.as_posix())
            save_output(
                rendered=rendered, output_dir=output_dir.as_posix(), fname_base=docs_path.stem
            )
            logfire.info(f"Converted Successfully", source=docs_path, output=output_dir.as_posix())

    async def _process_image(self, image_path_or_url: str) -> DescribeImagesOutput:
        # 使用 semaphore 控制並發數量
        async with self.semaphore:
            # https://platform.openai.com/docs/guides/vision
            image_path = Path(image_path_or_url)
            resolved_path = image_path.resolve().as_posix()
            if image_path.exists():
                logfire.info(f"Processing Image...", image_path = resolved_path)
                # 如果圖片路徑存在，讀取圖片並轉換成 data uri 格式
                base64_image = get_pil_image(image_file=resolved_path)
                image_uri = pil_to_data_uri(base64_image)
                content: list[dict[str, Any]] = [
                    {"type": "image_url", "image_url": {"url": image_uri}},
                    {"type": "text", "text": "Describe the image in detail."},
                ]
                # 呼叫 API 取得描述
                response = await self.client.chat.completions.create(
                    model="aide-gpt-4o",
                    messages=[{"role": "user", "content": content}],
                    temperature=0.0,
                )
                result = response.choices[0].message.content
            else:
                logfire.error(
                    f"Cannot find the image, please check the image path.", image_path = resolved_path
                )
                result=f"Cannot find the image of {resolved_path}, please check the image path."
            return DescribeImagesOutput(
                image_url=resolved_path,
                answer=result
            )

    async def describe_images(
        self, image_path_or_urls: list[str] | str
    ) -> list[DescribeImagesOutput]:
        if isinstance(image_path_or_urls, str):
            image_path_or_urls = [image_path_or_urls]
        tasks = [self._process_image(image_path_or_url) for image_path_or_url in image_path_or_urls]
        return await asyncio.gather(*tasks)

    async def parse_docs_with_images(self) -> None:
        docs_paths = [f for f in self.all_docs_paths if f.name.endswith(".md")]
        docs_paths = [f for f in docs_paths if not f.stem.endswith("_parsed")]
        if not docs_paths:
            logfire.info("No parsed markdown files found in the path.")
            return
        for docs_path in docs_paths:
            docs_content = docs_path.read_text(encoding="utf-8")
            # Use regex to find the line starts with `![](_page` and ends with `)`
            splitted_contents = docs_content.splitlines()
            docs_parent = docs_path.parent
            image_path_or_urls = []
            image_mapping = {}
            for line_idx, line in enumerate(splitted_contents, start=1):
                if line.startswith("![](_page") and line.endswith(")"):
                    image_path_string = line.split("](")[1].split(")")[0]
                    image_path = docs_parent / image_path_string
                    if image_path.exists():
                        image_url = image_path.absolute().as_posix()
                        image_mapping[image_url] = line_idx
                        image_path_or_urls.append(image_url)
            if not image_path_or_urls:
                logfire.info(
                    f"No images found in {docs_path}.", source=docs_path
                )
                continue
            # For debugging
            # image_path_or_urls = image_path_or_urls[:1]
            parsed_images = await self.describe_images(image_path_or_urls=image_path_or_urls)
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
            logfire.info(
                f"Parsed Successfully",
                source=docs_path,
                output=new_docs_path.as_posix(),
            )


if __name__ == "__main__":
    import fire

    # python convert_docs.py to_markdown --path="./docs/Bandgap Reference Verification_RAK.pdf"
    # python convert_docs.py to_markdown --path="./docs"
    # python scripts/convert_docs.py parse_docs_with_images --path="./docs/Bandgap References"
    # python scripts/convert_docs.py parse_docs_with_images --path="./docs"

    fire.Fire(DocsConverter)
