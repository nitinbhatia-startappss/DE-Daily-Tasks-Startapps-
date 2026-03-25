import time


def log_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        diff = end - start

        print(diff)
    return wrapper


@log_time
def my_function():
    total = sum(range(100))
    print(total)


my_function()