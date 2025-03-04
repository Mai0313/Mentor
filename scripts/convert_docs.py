# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "httpx",
#     "logfire",
#     "markitdown",
#     "openai",
#     "rich",
#     "unstructured[all-docs]",
# ]
# ///
from pathlib import Path

import logfire
from pydantic import Field, BaseModel, computed_field
from unstructured.staging.base import elements_to_json
from unstructured.partition.pdf import partition_pdf

logfire.configure(send_to_logfire=False)


import httpx
from openai import AzureOpenAI
from markitdown import MarkItDown
from rich.console import Console

console = Console()


class DocsConverter(BaseModel):
    path: str = Field(
        default="./docs/Bandgap Reference Verification_RAK.pdf",
        description="The path of the docs you want to convert, it can be either a file or a directory.",
        frozen=False,
        deprecated=False,
    )

    @computed_field
    @property
    def all_docs_paths(self) -> list[Path]:
        if Path(self.path).is_dir():
            all_docs_paths = list(Path(self.path).glob("**/*.*"))
        elif Path(self.path).is_file():
            all_docs_paths = [Path(self.path)]
        else:
            raise ValueError(f"Invalid path: {self.path}")
        return all_docs_paths

    def to_md(self) -> None:
        """Convert the docs to markdown format.

        Args:
            path (str): The path of the docs you want to convert, it can be either a file or a directory. Defaults to "./docs".

        Returns:
            None

        Raises:
            ValueError: If the path is neither a file nor a directory.

        Note:
            1. If the path is a directory, it will convert all the files in the directory to markdown format.
            2. If the path is a file, it will convert the file to markdown format.
            3. The converted files will be saved in the same directory as the original files, with the same name but with a .md extension.
        """
        console.print("Converting...", style="bold green")

        client = AzureOpenAI(
            api_key="hihi@srv_it_eas1_tester",
            azure_endpoint="https://tma.mediatek.inc/tma/sdk/api/v1",
            api_version="2024-08-01-preview",
            http_client=httpx.Client(verify=False, headers={"X-User-Id": "srv_it_eas1_tester"}),
        )
        md = MarkItDown(llm_client=client, llm_model="aide-gpt-4o")

        for docs_path in self.all_docs_paths:
            result = md.convert(source=docs_path)
            if result and result.title is None:
                result.title = Path(docs_path).stem
            output_filename = docs_path.with_suffix(".md")
            with open(output_filename, "w", encoding="utf-8") as f:
                f.write(result.text_content)
            console.print(f"Converted {docs_path} to {output_filename}", style="bold green")

    def to_json(self) -> None:
        for docs_path in self.all_docs_paths:
            output_dir = docs_path.parent / docs_path.stem.replace(" ", "_")
            output_dir.mkdir(parents=True, exist_ok=True)
            output_filename = (output_dir / docs_path.name).with_suffix(".json")

            file_elements = partition_pdf(
                filename=docs_path.as_posix(),
                strategy="hi_res",
                languages=["eng"],
                infer_table_structure=True,
                extract_images_in_pdf=True,
                extract_image_block_output_dir=output_dir.as_posix(),
                extract_image_block_types=["Image", "Table"],
                extract_forms=False,
                form_extraction_skip_tables=False,
            )

            elements_to_json(
                elements=file_elements, filename=output_filename.as_posix(), encoding="utf-8"
            )


if __name__ == "__main__":
    import fire

    # python convert_docs.py --path="./docs/Bandgap Reference Verification_RAK.pdf"

    fire.Fire(DocsConverter)
