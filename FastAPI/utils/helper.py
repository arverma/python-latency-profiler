import numpy as np

from profiler import function_timings, profile_function_sync


@profile_function_sync
def construct_welcome_message_with_name(name):
    return {"message": f"Hello {name}"}


def calculate_profile_summary():
    summary = {}
    for func_name, timings in function_timings.items():
        count = len(timings)
        avg_time = sum(timings) / count
        max_time = max(timings)
        min_time = min(timings)

        # Calculate p99 time
        p99_time = np.percentile(timings, 99)

        summary[func_name] = {
            "count": count,
            "average_time": avg_time,
            "min_time": min_time,
            "max_time": max_time,
            "p99_time": p99_time,
        }
    return summary
