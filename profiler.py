import time
from functools import wraps

# Store function profiling information
function_timings = {}


# Decorator to measure execution time of synchronous functions
def profile_function_sync(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed_time = time.perf_counter() - start_time
        func_name = func.__name__

        if func_name not in function_timings:
            function_timings[func_name] = []

        function_timings[func_name].append(elapsed_time * 1000)
        return result

    return wrapper


# Decorator to measure execution time of asynchronous functions
def profile_function_async(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = await func(*args, **kwargs)
        elapsed_time = time.perf_counter() - start_time
        func_name = func.__name__

        if func_name not in function_timings:
            function_timings[func_name] = []

        function_timings[func_name].append(elapsed_time * 1000)
        return result

    return wrapper
