from pathlib import Path

import logfire

logfire.configure(send_to_logfire=False)


import httpx
from openai import AzureOpenAI
from markitdown import MarkItDown
from rich.console import Console

console = Console()


def convert2markdown(path: str = "./docs") -> None:
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
    if Path(path).is_dir():
        all_docs_paths = list(Path(path).glob("**/*.*"))
    elif Path(path).is_file():
        all_docs_paths = [Path(path)]
    else:
        raise ValueError(f"Invalid path: {path}")

    console.print("Converting...", style="bold green")

    client = AzureOpenAI(
        api_key="hihi@srv_it_eas1_tester",
        azure_endpoint="https://tma.mediatek.inc/tma/sdk/api/v1",
        api_version="2024-08-01-preview",
        http_client=httpx.Client(verify=False, headers={"X-User-Id": "srv_it_eas1_tester"}),
    )

    md = MarkItDown(llm_client=client, llm_model="aide-gpt-4o")

    for docs_path in all_docs_paths:
        result = md.convert(source=docs_path)
        if result and result.title is None:
            result.title = Path(docs_path).stem
        output_filename = docs_path.with_suffix(".md")
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(result.text_content)
        console.print(f"Converted {docs_path} to {output_filename}", style="bold green")


if __name__ == "__main__":
    import fire

    fire.Fire(convert2markdown)
