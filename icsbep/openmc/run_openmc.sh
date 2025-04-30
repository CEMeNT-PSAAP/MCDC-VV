#!/bin/bash

BASEDIR=$PWD

cd $BASEDIR

# Check for argument -- if one exists, we assume it is a file with the list of
# directories to run. Otherwise, we simply search for directories containing a
# settings.xml file
if [[ $# -gt 0 ]]
then
    directories=$(cat $1)
else
    directories=$(find . -name settings.xml | sed 's/\/settings.xml//g' | sort)
fi

for dir in $directories
do
    echo "Submitting job for ${dir}..."
    cd "$BASEDIR/$dir"
    
    # Create a Slurm batch script
    JOB_SCRIPT="submit_job.sh"
    cat > "$JOB_SCRIPT" <<EOL
#!/bin/bash
#SBATCH -J openmc_sim_$(basename "$dir")
#SBATCH -o openmc_output_$(basename "$dir").log
#SBATCH -t 00:10:00
#SBATCH -p pbatch
#SBATCH -N 1
#SBATCH -A orsu

export OPENMC_CROSS_SECTIONS="<path_to_openmc>/openmc/data/endfb-viii.0-hdf5/cross_sections.xml"

<path_to_openmc>/openmc/executable/bin/openmc > openmc.stdout 2>&1
EOL
    
    # Submit the job
    sbatch "$JOB_SCRIPT"
    echo "Submitted job for $dir"

done