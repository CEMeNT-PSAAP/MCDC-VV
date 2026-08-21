"""Shared helpers for VVP configuration and launch processing."""

import math


def get_case_walltime(task, platform, walltime_base=None):
    """Scale the launch walltime for one case and apply the platform limit."""
    walltime_factor = task.get("walltime_factor", 1.0)

    # Validate the optional launch-wide base duration.
    if walltime_base is not None and (
        isinstance(walltime_base, bool)
        or not isinstance(walltime_base, (int, float))
        or not math.isfinite(walltime_base)
        or walltime_base <= 0.0
    ):
        raise ValueError("Launch walltime must be a positive real number of hours.")

    # Validate the multiplier supplied by the individual case.
    if (
        isinstance(walltime_factor, bool)
        or not isinstance(walltime_factor, (int, float))
        or not math.isfinite(walltime_factor)
        or walltime_factor <= 0.0
    ):
        raise ValueError("Case walltime_factor must be a positive real number.")

    # Use the platform limit as the base when the launch does not specify one.
    if walltime_base is None:
        walltime_base = platform["max_walltime_hours"]

    # Round up to the scheduler resolution, then enforce the platform limit.
    resolution = platform["walltime_resolution_seconds"]
    max_seconds = (
        math.floor(platform["max_walltime_hours"] * 3600.0 / resolution) * resolution
    )
    walltime_seconds = (
        math.ceil(walltime_base * walltime_factor * 3600.0 / resolution) * resolution
    )
    walltime_seconds = min(walltime_seconds, max_seconds)

    # Convert seconds into the scheduler-specific walltime syntax.
    hours, remainder = divmod(walltime_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return platform["walltime_format"].format(
        hours=hours,
        minutes=minutes,
        seconds=seconds,
    )
