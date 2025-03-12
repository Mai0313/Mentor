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
from typing import Any
from pathlib import Path

import pandas as pd
from pydantic import Field, BaseModel, computed_field
from rich.table import Table
from rich.console import Console

# 各種 error 的關鍵字定義 (依序為 log 裡搜尋的字串、欄位名稱、顯示在表格的標題)
ERRORS = [
    ("dc sweep error", "dc_sweep_error", "DC Sweep Error Rate"),
    ("empty code error", "empty_code_error", "Empty Code Error Rate"),
    ("simulation error", "simulation_error", "Simulation Error Rate"),
    ("execution error", "execution_error", "Execution Error Rate"),
    ("mosfet connection error", "mosfet_error", "Mosfet Connection Error Rate"),
    ("function error", "function_error", "Function Error Rate"),
]

console = Console()


class EvaluationResult(BaseModel):
    """用來記錄每個 log 檔的分析結果，包含 pass 數量與各種 error的計數。"""

    model_name: str
    problem_number: int
    pass1: int
    pass5: int
    total: int
    dc_sweep_error: int
    empty_code_error: int
    simulation_error: int
    execution_error: int
    mosfet_error: int
    function_error: int
    file_path: str


class EvaluationChecker(BaseModel):
    path: str = Field(default="./logs", description="log 檔案的資料夾路徑")
    num_per_task: int = Field(default=5, description="每個 task 的回合數", gt=0)
    live: bool = Field(default=False, description="是否持續更新")
    clean: bool = Field(default=False, description="是否刪除未完成的 task 的 log 檔案")

    @computed_field
    @property
    def all_files(self) -> list[Path]:
        log_filder = Path(self.path)
        if not log_filder.exists():
            raise FileNotFoundError(f"[yellow]Log folder {self.path} does not exist.[/yellow]")
        if not log_filder.is_dir():
            raise NotADirectoryError(f"[yellow]{self.path} is not a directory.[/yellow]")

        all_file_paths = list(log_filder.glob("*.txt"))
        if not all_file_paths:
            console.print(f"[red]No log files found in {self.path}[/red]")
        return all_file_paths

    @staticmethod
    def process_log_file(
        file_path: Path, model_name: str, problem_number: int
    ) -> EvaluationResult:
        """分析單個 log 檔案，回傳一個字典，記錄 code 成功次數與各種 error 的計數。"""
        abs_filepath = file_path.resolve().absolute().as_posix()
        counters = {
            "model_name": model_name,
            "problem_number": problem_number,
            "pass1": 0,
            "pass5": 0,
            "total": 0,
            "dc_sweep_error": 0,
            "empty_code_error": 0,
            "simulation_error": 0,
            "execution_error": 0,
            "mosfet_error": 0,
            "function_error": 0,
            "file_path": abs_filepath,
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
                            # 一行內只符合一種錯誤，故 break
                            break
        parsed_counters = EvaluationResult(**counters)
        return parsed_counters

    def display_model_scores(self, data: pd.DataFrame) -> None:
        models: list[str] = data["model_name"].unique().tolist()
        for model in models:
            console.print("\n")
            table = Table(
                title=f"{model} Success Rates from [bold green]{self.path}[/bold green]",
                show_header=True,
                header_style="bold blue",
            )
            table.add_column("Task ID", justify="right")
            table.add_column("pass@1 Rate", justify="right")
            table.add_column("pass@5 Rate", justify="right")
            for *_, col_title in ERRORS:
                table.add_column(col_title, justify="right")
            table.add_column("Error Found", justify="right")

            divided_data = data[data["model_name"] == model].sort_values("problem_number")
            for _, row in divided_data.iterrows():
                pass1_rate = row["pass1_rate"]
                pass5_rate = row["pass5_rate"]
                # 指定顏色：若率值低於 50% 即標示不同顏色
                pass1_color = "yellow" if pass1_rate < 0.5 else "green"
                pass5_color = "red" if pass5_rate < 0.5 else "green"
                error_comment = row["error_comment"]
                error_comment_color = "red" if error_comment != "Pass" else "green"

                row_data = [
                    str(row["problem_number"]),
                    f"[{pass1_color}]{pass1_rate * 100:.2f}%[/{pass1_color}]",
                    f"[{pass5_color}]{pass5_rate * 100:.2f}%[/{pass5_color}]",
                ]
                for _, err_key, _ in ERRORS:
                    err_rate = row[f"{err_key}_rate"]
                    err_color = "yellow" if err_rate > 0.0 else "green"
                    row_data.append(f"[{err_color}]{err_rate * 100:.2f}%[/{err_color}]")
                row_data.append(f"[{error_comment_color}]{error_comment}[/{error_comment_color}]")
                table.add_row(*row_data)

            console.print(table)
            console.print("\n")

    def parse_error_message(self, row: pd.Series) -> str:
        error_message = "Pass"
        if row["pass1"] != self.num_per_task and row["pass5"] != self.num_per_task:
            error_message = f"Missing {self.num_per_task - row['pass5']} rounds"
        return error_message

    def parse_logs_in_folder(self) -> tuple[pd.DataFrame, list[Path]]:
        """
        讀取指定資料夾下所有 .txt 的 log 檔，
        利用 pandas 先統整每個 log 檔計算各項統計資訊，
        並回傳一個 DataFrame 與未完成 (Missing rounds) 的 task 列表。

        檔名格式參照: <datetime>_<model_name>_<problem number>_log.txt 或 <datetime>_<model_name>_<problem number>_log_no_skill.txt
        """
        # 檔名用此正規表示式解析：忽略前置部分，接著 "_" 之後拿 model 相關資訊，
        # 再讀取一段數字作為 problem_number
        filename_pattern = re.compile(r"^(?:.*?)_(.+?)(\d+)_log(?:_no_skill)?")

        rows: list[dict[str, Any]] = []
        for file_path in self.all_files:
            match = filename_pattern.match(file_path.name)
            if match:
                model_info = match.group(1)
                # 預設檔名格式為：<datetime>_<prefix>_<model_name>_<...>，此處簡單取第二個底線後的字串
                parts = model_info.split("_")
                model_name = parts[1] if len(parts) >= 2 else parts[0]
                problem_number = int(match.group(2))

                counters = self.process_log_file(
                    file_path=file_path, model_name=model_name, problem_number=problem_number
                )
                rows.append(counters.model_dump())

        if not rows:
            return None, []

        data = pd.DataFrame(rows)

        # 計算各項率值，先預防 total 為 0 的狀況 (用 1 代替避免除 0)
        data["pass1_rate"] = data["pass1"] / self.num_per_task
        data["pass5_rate"] = data["pass5"] / self.num_per_task
        for _, err_key, _ in ERRORS:
            data[f"{err_key}_rate"] = data[err_key] / data["total"].replace({0: 1})

        # 計算 error_comment：若任一 pass 數達標則顯示 "Pass"，否則顯示缺少幾回合 (以 pass@5 為準)
        data["error_comment"] = data.apply(self.parse_error_message, axis=1)

        not_done_task_paths = []
        no_pass_task = data.query("error_comment != 'Pass'")
        if not no_pass_task.empty:
            not_done_tasks = no_pass_task["file_path"].tolist()
            for not_done_task in not_done_tasks:
                not_done_task_paths.append(Path(not_done_task))
        return data, not_done_task_paths

    def __call__(self) -> None:
        """Main Function.
        1. 利用 parse_logs_in_folder() 與 pandas 先統整所有 log 檔案資訊。
        2. 根據模型分組利用 rich table 顯示各項率值與錯誤狀況。
        3. (Optional) 在 clean 模式下，將未完成的 task 對應的 log 檔移除。
        4. 若 live 為 True 則每隔 5 秒更新一次結果。
        """
        if self.live:
            while True:
                data, _ = self.parse_logs_in_folder()
                if data.empty:
                    break
                self.display_model_scores(data=data)
                time.sleep(5)
                os.system("clear")  # noqa: S605, S607
        else:
            data, not_done_tasks = self.parse_logs_in_folder()
            if data.empty:
                return
            self.display_model_scores(data=data)
            if self.clean:
                for not_done_task_path in not_done_tasks:
                    console.print(f"[red]Removing {not_done_task_path}[/red]")
                    not_done_task_path.unlink()


if __name__ == "__main__":
    import fire

    fire.Fire(EvaluationChecker)
