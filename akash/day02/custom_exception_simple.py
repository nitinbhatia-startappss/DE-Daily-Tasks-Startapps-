# create custom exception
class MyError(Exception):
    pass


# function to check value
def check_value(num):
    
    # if number is negative, raise error
    if num < 0:
        raise MyError("Number cannot be negative")
    
    return num


try:
    # call function
    result = check_value(-5)
    print("Result:", result)

# handle custom exception
except MyError as e:
    print("Error:", e)