import time

# Decorator to measure the time taken by a function to execute and print the results.
def time_function(func):

    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time_ms = (end_time - start_time) * 1000  # Convert seconds to milliseconds
        print(f"{func.__name__} took {elapsed_time_ms:.3f} ms.")
        return result
        
    return wrapper