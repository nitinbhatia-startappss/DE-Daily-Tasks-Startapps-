#Q write a function that uses a decorator to log the execution time of the passed function
import time

# Decorator function to calculate execution time
def time_logger(func):
    
    # wrapper function
    def wrapper(*args, **kwargs):
        
        start_time = time.time()  # record start time
        
        result = func(*args, **kwargs)  # call original function
        
        end_time = time.time()  # record end time
        
    
        print("Execution time:", end_time - start_time, "seconds")
        
        return result  # return original function result
    
    return wrapper


# Apply decorator using @ symbol
@time_logger
def sample_function():
    # sample loop to consume time
    for i in range(1000000):
        pass


# calling function
sample_function()