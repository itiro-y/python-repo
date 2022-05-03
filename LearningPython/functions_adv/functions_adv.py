# Forced keyword arguments
#     You are not forced to a particular order - the name matters, but not the position
#     Keyword arguments provide clarity

# Using the asterisk before the arguments to force keyword arguments
# ex
def f(*, a, b):
    print(a,b)

try:
    f(1, 2) # This will trigger an error because the function forces keywords
except Exception as e:
    print("An error occurred:", e)    

f(a = 1, b = 2) # Is the correct way of calling it

# Using ** to pass a dictionary containing multiple arguments
args = {"a":1, "b":2}
f(**args)

# Can use a single * to unpack a list and feed its content as positional arguments to a funciton
def f(a, b, c):
    print(a, b, c)

l = [1, 2, 3]
f(*l)


# Decorating your functions
# Decorators are wrappers around a function that modify the behaviour of the function in a certain way

#ex
# print_argument is a wrapper function that prints the name and the argument of a function
def print_argument(func):
    def wrapper(the_number):
        print("Argument for", func.__name__, "is", the_number)
        return func(the_number)
    return wrapper

# We apply the decorator to a function
@print_argument
def add_one(x):
    return x + 1

print(add_one(1))


# Anonymous functions (or lambda functions)
# ex. are functions that will only run once

# a lambda function can be assigned to a variable
add_1 = lambda x: x + 1
print(add_1(3))

# Using a function as an argument
# map() -> applies a function to all elements of a iterable object
# ex
numbers = [1, 2, 3, 4]
times_two = map(lambda x: x * 2, numbers)
print(list(times_two))

# map() + lambda is very useful to apply simple changes to an iterable object

