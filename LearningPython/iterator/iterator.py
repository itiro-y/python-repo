import traceback
# How the Iterator in Python works

# Iterator vs Iterable

#   Iterator: An object that can be iterated, meaning we can keep asking it for a new
# element until there are no elements left. Elements are requested using a method called __next__

#   Iterable: An object that implements another special method, called __iter__. This
# function returns an iterator


# How a Python iterator works
#   A Python iterator implements a function __name__ that keeps returning elements until it runs out of
# elements to return, in which case an exception is raised of type StopIteration

#   To get an iterator object, we need to first call the __iter__ method on an iterable object

# We can use the range() function (built-in Python iterable) to understand
# ex
# range() returns an object that is iterable
my_iterable = range(1, 3)

# We call the function and assign the iterator it return to my_iterator
my_iterator = my_iterable.__iter__()

# Call the __next__() method
print(my_iterator.__next__())
print(my_iterator.__next__())
try:
    print(my_iterator.__next__()) # exception: StopIteration error raised
except Exception:
    traceback.print_exc()
# In case you need to manually get an iterator use iter() and next() functions instead
# OBS: You can only go forward with next(), we can't reset (unless you make another iterator) or go back
#      iterable objects maintain their state, so you can use it in one loop at a time (helps in concurrency)


# Python built-in iterators
#   Python lists
#   Python sets
#   Python dictionaries
#   Python tuples
#   Ranges
#   Strings
#   Generators* (ex. range(), the function generates these numbers instead of matererializing them in an actual list)


# How to use a Python iterator

# Iterator in a for-loop
# Python for loops require an iterable!

#ex. strings and lists
my_string = "ABC"
for letter in my_string:
    print(letter)

my_list = ["A","B","C"]
for letter in my_list:
    print(letter)

# Iterators in comprehensions
# like for loops comprehensions also require an iterable object

list_a = [x for x in "ABC"]
print(list_a)

list_b = [x for x in [1, 2, 3, 4] if x > 2]
print(list_b)

# Iterate over Python dictionary keys, not the values
my_dict = {"name":"Alice", "age":23, "country":"NL"}
for keys in my_dict:
    print(keys)

# Iterating over dictionary values
# my_dict.values() retuns a list of values from the dict
for values in my_dict.values():
    print(values)

# Iterating over both keys and values
for keys, values in my_dict.items():
    print(keys, values)

# or with a list comprehension and f-string
keys_values = [f'{keys}: {values}' for keys, values in my_dict.items()]
print(keys_values)


# Convert Python Iterator to list, tuple, dict or set
# An iterator can be materialized into a iterable object: list(), set(), tuple()
#ex
list(range(1, 2)) # [1, 2]
set(range(1, 2)) # {1, 2}
tuple(range(1, 2)) # (1, 2)

# tuples that have keys, values can be materialized with dict()


# Reading files line-by-line in Python
with open("not_here.txt", "r") as f:
    for line in f:
        print(line)


# Creating your own Python iterator
# need to implement __iter__ and __next__

#ex. one simple class
# could make this endless, but we raise an exception as we past 8 iterations

class EvenNumbers:
    last = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.last += 2

        if self.last > 8:
            raise StopIteration
        
        return self.last
    
even_numbers = EvenNumbers()

for num in even_numbers:
    print(num)
