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
        elapsed_time = end_time - start_time

        if elapsed_time >= 1:
            print(f"Solve time: {elapsed_time:.3f} s")
        elif elapsed_time >= 1e-3:
            print(f"Solve time: {elapsed_time * 1e3:.3f} ms")
        elif elapsed_time >= 1e-6:
            print(f"Solve time: {elapsed_time * 1e6:.3f} µs")
        else:
            print(f"Solve time: {elapsed_time * 1e9:.3f} ns")

        return result

    return wrapper
