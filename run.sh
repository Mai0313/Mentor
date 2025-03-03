#!/bin/bash
# 用法：
#   ./run.sh 1 24        # 執行從 1 到 24 的 tasks
#   ./run.sh 9 10 11 14  # 執行這四個 task

PYTHON_PATH=~/miniconda3/envs/analog/bin/python

# 檢查參數數量
if [ "$#" -lt 1 ]; then
    echo "Usage: $0 <start> <end> OR $0 <list_of_task_ids>"
    exit 1
fi

# 如果僅有兩個參數且都是數字，且第一個小於或等於第二個，就當作 range 處理
if [ "$#" -eq 2 ] && [[ "$1" =~ ^[0-9]+$ ]] && [[ "$2" =~ ^[0-9]+$ ]] && [ "$1" -le "$2" ]; then
    tasks=$(seq "$1" "$2")
else
    # 其他情況下，把所有參數視為 task id 清單
    # 為了保險起見，將每個參數印成獨立一行
    tasks=$(printf "%s\n" "$@")
fi

# 計算要並行跑的 task 數量（依據 task id 個數）
num_tasks=$(echo "$tasks" | wc -l)

# 執行 tasks，xargs 會以換行符作分隔符，並以 -n 1 每次丟一個參數進去
echo "$tasks" | xargs -n 1 -P "$num_tasks" -I {} $PYTHON_PATH gpt_run.py --num_per_task=5 --num_of_retry=5 --task_id={}

# Version-1:
# Loop through task_id from 1 to 24
# for task_id in $(seq 1 15)
# do
#     # Run the python command with the current task_id
#     PYTHON_PATH gpt_run.py --num_per_task=5 --num_of_retry=5 --model=aide-gpt-4o --task_id=$task_id
# done

# Version-2:
# seq 1 24 | xargs -n 1 -P 24 -I {} $PYTHON_PATH gpt_run.py --num_per_task=5 --num_of_retry=5 --skill --task_id={}
