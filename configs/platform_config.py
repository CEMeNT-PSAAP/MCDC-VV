"""
Supported compute platforms and their parameters for MC/DC VVP workflows.
"""

PLATFORMS = {
    "dane": {
        "host": "dane",
        "scheduler": "slurm",
        "submit": "sbatch",
        "launcher": "srun",
        "cpu_cores_per_node": 112,
        "gpus_per_node": 0,
        "max_nodes": 128,
        "max_walltime_hours": 24,
        "walltime_resolution_seconds": 1,
        "walltime_format": "{hours}:{minutes:02d}:{seconds:02d}",
    },
    "lassen": {
        "host": "lassen",
        "scheduler": "lsf",
        "submit": "bsub",
        "launcher": "jsrun",
        "cpu_cores_per_node": 40,  # physical: 44
        "gpus_per_node": 4,
        "max_nodes": 128,  # actual system limit: 256
        "max_walltime_hours": 24,  # actual system limit may be lower
        "walltime_resolution_seconds": 60,
        "walltime_format": "{hours}:{minutes:02d}",
    },
    "tuolumne": {
        "host": "tuolumne",
        "scheduler": "flux",
        "submit": "flux batch",
        "launcher": "flux run",
        "cpu_cores_per_node": 96,
        "gpus_per_node": 4,
        "max_nodes": 128,
        "max_walltime_hours": 24,
        "walltime_resolution_seconds": 1,
        "walltime_format": "{hours}:{minutes:02d}:{seconds:02d}",
    },
}
