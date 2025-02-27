import re
from pathlib import Path
from collections import defaultdict

import httpx
from openai import AzureOpenAI
from rich.table import Table
from rich.console import Console


def parse_logs_in_folder(
    folder_path: str = "./logs", num_per_task: int = 5, llm_comment: bool = False
) -> None:
    """This function reads all '.txt' log files in the specified folder and parses
    them to calculate.

    1) pass@1 count: count how many times code_id:0 reports "success."
    2) pass@5 count: count how many times any code_id from 0 to 4 reports "success."

    The log filenames follow the structure <datetime>_<model_name>_<problem number>_log.txt.
    For each problem, the function assumes there are 5 iterations (it: 0..4). The final rates are calculated by dividing these counts by total_iterations (which is set to 5).

    Args:
        folder_path (str): The path to the folder containing the log files. Defaults to "./logs".
        num_per_task (int): The number of iterations per task. Defaults to 5.
        llm_comment (bool): Whether to use LLM to comment on the results. Defaults to False.

    Returns:
        None: This function prints each model's success rates in separate Rich tables.
    """
    # Initialize Rich console
    console = Console()

    # Dictionary to store scores for each model
    model_scores = defaultdict(list)

    # Init AzureOpenAI
    client = AzureOpenAI(
        api_key="hihi@srv_it_eas1_tester",
        azure_endpoint="https://tma.mediatek.inc/tma/sdk/api/v1",
        api_version="2024-08-01-preview",
        http_client=httpx.Client(verify=False, headers={"X-User-Id": "srv_dvc_tma001"}),
    )

    # Regex to identify <datetime>_<model_name>_<problem number>_log.txt
    filename_pattern = re.compile(r"^.*_(.+?)_(\d+)_log\.txt$")

    console.print("\n")

    # Traverse the folder to parse any '.txt' files matching our pattern
    log_files = Path(folder_path).rglob("*.txt")
    for file_path in log_files:
        file_content = file_path.read_text()
        short_comment = ""
        if llm_comment is True:
            response = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": f"Here is the experiment log content for LLM evaluation\n{file_content}",
                    },
                    {
                        "role": "user",
                        "content": "Please give a one line comment for this result. What are the root causes of the errors it might be.",
                    },
                ],
                model="aide-gpt-4o",
            )
            short_comment = response.choices[0].message.content
        match = filename_pattern.match(file_path.name)
        if not match:
            continue

        model_name = match.group(1)
        problem_number = int(match.group(2))
        with open(file_path, encoding="utf-8") as f:
            pass1, pass5 = 0, 0
            for line in f:
                if "code_id:0	success." in line:
                    pass1 += 1
                    pass5 += 1
                elif "success." in line:
                    pass5 += 1
            model_scores[model_name].append([problem_number, pass1, pass5, short_comment])

    # Create and print tables for each model
    for model_name, scores in model_scores.items():
        # Create a Rich table for the current model
        table = Table(
            title=f"{model_name} Success Rates from [bold green]{folder_path}[/bold green]",
            show_header=True,
            header_style="bold blue",
        )
        table.add_column("Problem Number", justify="right")
        table.add_column("pass@1 Rate", justify="right")
        table.add_column("pass@5 Rate", justify="right")
        table.add_column("Short Comment by LLM", justify="right")

        # Add rows to the table
        for score in sorted(scores, key=lambda x: x[0]):
            problem_number = score[0]
            pass1_rate = score[1] / num_per_task
            pass5_rate = score[2] / num_per_task
            short_comment = score[3]

            # table.add_row(
            #     str(problem_number), f"{pass1_rate * 100:.2f}%", f"{pass5_rate * 100:.2f}%"
            # )
            # Add rows with color;
            # color rules:
            # 1. pass@1 rate < 0.5: red
            # 2. pass@5 rate < 0.5: yellow
            # 3. pass@1 rate >= 0.5 and pass@5 rate >= 0.5: green
            pass1_color = "yellow" if pass1_rate < 0.5 else "green"
            pass5_color = "red" if pass5_rate < 0.5 else "green"

            # Add rows with color
            table.add_row(
                str(problem_number),
                f"[{pass1_color}]{pass1_rate * 100:.2f}%[/{pass1_color}]",
                f"[{pass5_color}]{pass5_rate * 100:.2f}%[/{pass5_color}]",
                short_comment,
            )

        # Print the table using Rich console
        console.print(table)
        # Add a newline between tables
        console.print("\n")


if __name__ == "__main__":
    import fire

    fire.Fire(parse_logs_in_folder)
