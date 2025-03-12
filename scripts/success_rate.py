# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pandas",
#     "rich",
# ]
# ///
import os
import re
import time
from pathlib import Path
from collections import defaultdict

import pandas as pd
from rich.table import Table
from rich.console import Console

# Error 訊息與記錄鍵值的對應
ERRORS = [
    ("dc sweep error", "dc_sweep_error", "DC Sweep Error Rate"),
    ("empty code error", "empty_code_error", "Empty Code Error Rate"),
    ("simulation error", "simulation_error", "Simulation Error Rate"),
    ("execution error", "execution_error", "Execution Error Rate"),
    ("mosfet connection error", "mosfet_error", "Mosfet Connection Error Rate"),
    ("function error", "function_error", "Function Error Rate"),
]

console = Console()


def process_log_file(file_path: Path) -> dict:
    """分析單個 log 檔案，回傳一個字典，記錄 code 成功次數與各種 error 的計數。"""
    counters = {
        "pass1": 0,
        "pass5": 0,
        "total": 0,
        "dc_sweep_error": 0,
        "empty_code_error": 0,
        "simulation_error": 0,
        "execution_error": 0,
        "mosfet_error": 0,
        "function_error": 0,
    }
    with file_path.open(encoding="utf-8") as f:
        for line in f:
            # code_id:0 reports success
            if "code_id:0	success." in line:
                counters["pass1"] += 1
                counters["pass5"] += 1
                counters["total"] += 1
            # 其他 code_id 如果報 success，只統計 pass@5
            elif "success." in line:
                counters["pass5"] += 1
                counters["total"] += 1
            else:
                # 依序檢查錯誤訊息
                for err_message, err_key, _ in ERRORS:
                    if err_message in line:
                        counters[err_key] += 1
                        counters["total"] += 1
                        break  # 一行內只符合一種錯誤，故 break
    return counters


def display_model_scores(
    console: Console, model_name: str, scores: list, folder_path: str, num_per_task: int
) -> list[str]:
    """依據傳入的 scores 列表 (每個元素為字典，包含 problem_number 與各項計數)
    組成一個 Rich Table 並輸出。
    """
    table = Table(
        title=f"{model_name} Success Rates from [bold green]{folder_path}[/bold green]",
        show_header=True,
        header_style="bold blue",
    )
    # 設定表格欄位
    table.add_column("Task ID", justify="right")
    table.add_column("pass@1 Rate", justify="right")
    table.add_column("pass@5 Rate", justify="right")
    for _, _, col_title in ERRORS:
        table.add_column(col_title, justify="right")
    table.add_column("Error Found", justify="right")

    not_done_tasks: list[str] = []
    # 對各個問題依 problem_number 排序
    for score in sorted(scores, key=lambda x: x["problem_number"]):
        total = score["total"] if score["total"] > 0 else 1  # 避免除 0

        pass1_rate = score["pass1"] / num_per_task
        pass5_rate = score["pass5"] / num_per_task

        # 若有缺少 round，顯示缺失回合數；否則顯示 Pass
        if score["pass1"] != num_per_task and score["pass5"] != num_per_task:
            error_comment = f"Missing {num_per_task - score['pass5']} rounds"
        else:
            error_comment = "Pass"

        if error_comment.startswith("Missing "):
            not_done_tasks.append(str(score["problem_number"]))

        # 設定顏色：
        # 注意：原始邏輯中 pass@1 rate 與 pass@5 rate 用不同的顏色標示
        pass1_color = "yellow" if pass1_rate < 0.5 else "green"
        pass5_color = "red" if pass5_rate < 0.5 else "green"
        error_comment_color = "red" if error_comment != "Pass" else "green"

        # 格式化率顯示百分比
        row = [
            str(score["problem_number"]),
            f"[{pass1_color}]{pass1_rate * 100:.2f}%[/{pass1_color}]",
            f"[{pass5_color}]{pass5_rate * 100:.2f}%[/{pass5_color}]",
        ]
        # 處理各種 error 的 rate (若 error count > 0 用 yellow 否則用 green)
        for _, err_key, _ in ERRORS:
            err_rate = score[err_key] / total
            err_color = "yellow" if err_rate > 0.0 else "green"
            row.append(f"[{err_color}]{err_rate * 100:.2f}%[/{err_color}]")

        row.append(f"[{error_comment_color}]{error_comment}[/{error_comment_color}]")
        table.add_row(*row)

    console.print(table)
    console.print("\n")
    return not_done_tasks


def parse_logs_in_folder(folder_path: str, num_per_task: int) -> list[Path]:
    """讀取指定資料夾下的所有 .txt log 檔，並依據檔名格式 <datetime>_<model_name>_<problem number>_log.txt解析 log 內容
    計算包含：
        1) pass@1: 計算 code_id:0 的成功次數
        2) pass@5: 計算任意 code_id (0-4) 的成功次數
    最後以 Rich table 輸出各個 model 的成功率與錯誤率。
    """

    # 用 defaultdict 儲存不同 model 的分數資料 (list 每個元素為一個 dict)
    model_scores = defaultdict(list)
    # 檔名規則: <datetime>_<model_name>_<problem number>_log.txt
    # filename_pattern = re.compile(r"^.*(.+?)(\d+)_log(?:_no_skill)?")
    # 檔名規則: <datetime>_<model_name>_<problem number>_log.txt 或 _no_skill
    filename_pattern = re.compile(r"^(?:.*?)_(.+?)(\d+)_log(?:_no_skill)?")

    # 遍歷資料夾中所有 .txt 檔案
    counters_list = []
    all_file_paths = list(Path(folder_path).glob("*.txt"))
    for file_path in all_file_paths:
        match = filename_pattern.match(file_path.name)
        if not match:
            continue

        model_info = match.group(1)
        _, model_name, *_ = model_info.split("_")
        problem_number = int(match.group(2))

        counters = process_log_file(file_path)
        counters["problem_number"] = problem_number

        model_scores[model_name].append(counters)
        counters_list.append(counters)

    data = pd.DataFrame(counters_list)
    data = data.rename(columns={"problem_number": "Task ID", "pass1": "pass@1", "pass5": "pass@5"})
    data = data[["Task ID", "pass@1", "pass@5"]]
    data = data.groupby("Task ID").sum().reset_index()

    # 根據 model 分別顯示結果
    if not model_scores:
        console.print(f"No log files found in {folder_path}")
        return None
    console.print("\n")
    for model_name, scores in model_scores.items():
        not_done_tasks = display_model_scores(
            console, model_name, scores, folder_path, num_per_task
        )

    not_done_task_paths: list[Path] = []
    for all_file_path in all_file_paths:
        problem_number = str(all_file_path.name.split("_")[2])
        if problem_number in not_done_tasks:
            not_done_task_paths.append(all_file_path)
    return not_done_task_paths


def get_success_rate(
    folder_path: str = "./logs", num_per_task: int = 5, live: bool = False, clean: bool = False
) -> None:
    """主函式，解析指定資料夾中的 log 檔案，並顯示各個 model 的成功率與錯誤率。"""
    if live:
        while True:
            parse_logs_in_folder(folder_path, num_per_task)
            time.sleep(5)
            os.system("clear")  # noqa: S605, S607
    else:
        not_done_task_paths = parse_logs_in_folder(folder_path, num_per_task)
        if clean:
            not_done = ", ".join([path.as_posix() for path in not_done_task_paths])
            console.print(f"Those tasks are not done yet: \n{not_done}")


if __name__ == "__main__":
    import fire

    fire.Fire(get_success_rate)
