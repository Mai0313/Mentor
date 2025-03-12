# Set the number of parallel tasks
parallel_jobs=6

# Function to create a new tmux window
create_tmux_window() {
    window_index=$(tmux list-windows | wc -l)
    tmux new-window -t run_sessions: -n "window_$window_index"
}

# Create a new tmux session
tmux new-session -d -s run_sessions -n "window_0"

# Initialize a variable to track the number of jobs
job_counter=0
model_name=aide-gpt-4o

# Loop over the range of task IDs
for task_id in $(seq 1 24)
do
    # Calculate the current window index
    window_index=$(($job_counter / $parallel_jobs))

    # If the window index changes, create a new window
    if [ $(($job_counter % $parallel_jobs)) -eq 0 ]; then
        if [ $job_counter -ne 0 ]; then
            create_tmux_window
        fi
    fi

    # Construct the python command
    if [ $task_id -le 15 ]; then
        tmux send-keys -t run_sessions:window_$window_index "conda activate analog && export PATH="/home/mtk34282/.conda/envs/analog/bin:$PATH" && python gpt_run.py --num_per_task=5 --num_of_retry=5 --model=$model_name --task_id=$task_id" C-m
    else
        tmux send-keys -t run_sessions:window_$window_index "conda activate analog && export PATH="/home/mtk34282/.conda/envs/analog/bin:$PATH" && python gpt_run.py --num_per_task=5 --num_of_retry=5 --model=$model_name --skill --task_id=$task_id" C-m
    fi

    # Increment the job counter
    job_counter=$(($job_counter + 1))
done

# Attach to the tmux session
tmux attach -t run_sessions
