from typing import Callable
import time


# Decorator to measure the time taken by a function to execute and print the results.
def time_function(func: Callable[..., int]) -> Callable[..., int]:

    # This wrapper will be used to measure the time taken by the function to execute via the `time` module's `perf_counter` function.
    # It then returns the result of the function and prints the time taken.
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
