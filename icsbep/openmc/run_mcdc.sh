#!/bin/bash

# Get the root directory (the directory where the script is located)
ROOT_DIR="$(dirname "$(realpath "$0")")"

# Find all directories named "mcdc" under the root directory
find "$ROOT_DIR" -type d -name "mcdc" | while read -r MCDC_DIR; do
    echo "Processing directory: $MCDC_DIR"
    cd "$MCDC_DIR" || continue  # Change to the mcdc directory
    rm *.log

    # Find all Python scripts inside the directory
    find . -maxdepth 1 -type f -name "*.py" | while read -r PYTHON_SCRIPT; do
        echo "Found Python script: $PYTHON_SCRIPT"
        
        # Create a Slurm batch script
        JOB_SCRIPT="submit_job_$(basename "$PYTHON_SCRIPT" .py).sh"
        cat > "$JOB_SCRIPT" <<EOL
#!/bin/bash
#SBATCH -J mcdc_sim_$(basename "$PYTHON_SCRIPT" .py)
#SBATCH -o mcdc_output_$(basename "$PYTHON_SCRIPT" .py).log
#SBATCH -t 00:10:00
#SBATCH -p pbatch
#SBATCH -A orsu
#SBATCH -N 1
#SBATCH -c 16

source ~/.bashrc
conda activate mcdc_env
export MCDC_XSLIB="path/to/MCDC/xs/library"
python "$PYTHON_SCRIPT" --mode=numba --output=$(basename "$PYTHON_SCRIPT" .py).h5 --no-progress_bar --caching
EOL
    
        # Submit the job
        sbatch "$JOB_SCRIPT"
        echo "Submitted job for $PYTHON_SCRIPT"
    done
    
    cd "$ROOT_DIR"  # Return to root directory

done
