import time
from typing import Callable


# Decorator to measure the time taken by a function to execute and print the results.
def time_function(func: Callable[..., int]) -> Callable[..., int]:

    # Used to measure the time taken to execute via the perf_counter.
    # Returns result and prints the time taken to execute the function.
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time_ms = (
            end_time - start_time
        ) * 1000  # Convert seconds to milliseconds
        print(f"Solve time: {elapsed_time_ms:.3f} ms")
        return result

    return wrapper
