def parse_logs_in_folder(folder_path: str, num_per_task: int = 5) -> None:
    """This function reads all '.txt' log files in the specified folder and parses them to calculate:
      1) pass@1 count: count how many times code_id:0 reports "success."
      2) pass@5 count: count how many times any code_id from 0 to 4 reports "success."

    The log filenames follow the structure <datetime>_<model_name>_<problem number>_log.txt.
    For each problem, the function assumes there are 5 iterations (it: 0..4). The final rates
    are calculated by dividing these counts by total_iterations (which is set to 5).

    Parameters:
    -----------
    folder_path : str
        The path to the folder containing the log files.
    num_per_task : int
        The number of iterations per task.

    Returns:
    --------
    None
        This function prints each model's success rates in separate Rich tables.
    """
    import os
    import re
    from collections import defaultdict

    from rich.table import Table
    from rich.console import Console

    # Regex to identify <datetime>_<model_name>_<problem number>_log.txt
    filename_pattern = re.compile(r"^.*_(.+?)_(\d+)_log\.txt$")

    # Initialize Rich console
    console = Console()

    # Dictionary to store scores for each model
    model_scores = defaultdict(list)

    # Traverse the folder to parse any '.txt' files matching our pattern
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            match = filename_pattern.match(filename)
            if not match:
                continue

            model_name = match.group(1)
            problem_number = int(match.group(2))
            file_path = os.path.join(folder_path, filename)

            with open(file_path, encoding="utf-8") as f:
                pass1, pass5 = 0, 0
                for line in f:
                    if "code_id:0	success." in line:
                        pass1 += 1
                        pass5 += 1
                    elif "success." in line:
                        pass5 += 1
                model_scores[model_name].append([problem_number, pass1, pass5])

    # Create and print tables for each model
    for model_name, scores in model_scores.items():
        # Create a Rich table for the current model
        table = Table(
            title=f"{model_name} Success Rates", show_header=True, header_style="bold blue"
        )
        table.add_column("Problem Number", justify="right")
        table.add_column("pass@1 Rate", justify="right")
        table.add_column("pass@5 Rate", justify="right")

        # Add rows to the table
        for score in sorted(scores, key=lambda x: x[0]):
            problem_number = score[0]
            pass1_rate = score[1] / num_per_task
            pass5_rate = score[2] / num_per_task

            table.add_row(
                str(problem_number), f"{pass1_rate * 100:.2f}%", f"{pass5_rate * 100:.2f}%"
            )

        # Print the table using Rich console
        console.print(table)
        print("\n")  # Add a newline between tables


if __name__ == "__main__":
    # folder_path = input('Input the logs folder path: \n')
    folder_path = "/home/mtk34282/gitea/AnalogCoderMTK_OLD/mutiple_logs"
    num_per_task = 5
    print("\n\n")
    parse_logs_in_folder(num_per_task=num_per_task, folder_path=folder_path)
