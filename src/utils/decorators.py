import cProfile
import time
from typing import Callable

from loguru import logger as log


# Decorator to measure the time taken by a function to execute and log the results.
def benchmark(func: Callable) -> Callable[..., int]:
    # Used to measure the time taken to execute via the perf_counter.
    # Returns result and logs the time taken to execute the function.
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        # Get the type of function, if the function name is parse, then we set variable to "Parsing", if it's not, then we set it to "Solving".
        func_type = "Parsing" if func.__name__ == "parse" else "Solving"

        if elapsed_time >= 1:
            log.debug(f"{func_type} Time: {elapsed_time:.3f} s")
        elif elapsed_time >= 1e-3:
            log.debug(f"{func_type} Time: {elapsed_time * 1e3:.3f} ms")
        elif elapsed_time >= 1e-6:
            log.debug(f"{func_type} Time: {elapsed_time * 1e6:.3f} µs")
        else:
            log.debug(f"{func_type} Time: {elapsed_time * 1e9:.3f} ns")

        return result

    return wrapper


# Decorator to profile a given function.
def profile(func):
    # Uses cProfile and dumps a file with the profiled information to view.
    def wrapper(*args, **kwargs):
        datafn = func.__name__ + ".profile"  # Name the data file sensibly
        prof = cProfile.Profile()
        retval = prof.runcall(func, *args, **kwargs)
        prof.dump_stats(datafn)
        return retval

    return wrapper
