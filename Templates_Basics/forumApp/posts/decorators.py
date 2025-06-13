import time


def measure_execution_time(func):
    def wrapper(request, *args, **kwargs):
        start = time.time()
        response = func(request, *args, **kwargs)
        end = time.time()

        execution_time = end - start
        print(f"The view executed in {execution_time}s")

        return response
    return wrapper
