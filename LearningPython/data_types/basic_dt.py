import random

# Basic DataTypes
# Integers, Float, Complex num, Booleans, Strings
# Tuples (cannot be modified), Lists(can be modified), 
# Ranges(efficiently calculated), Dictionaries, 
# Sets(allow you to do mathematical set calculcations)

# Two types: Mutable and Immutable / Hashable or Unhashable
# Mutable means its data can be changed
# Immutable means its data CANNOT be changed

# Ex of Immutable data types:
# All numbers(int, float, complex numbers)
# Booleans
# String
# Tuples

# Ex of Mutable data types:
# Lists
# Dictionaries
# Sets


# We are not changing the data, 
# but just reassigning it to a new variable

# In the first instance, myint points to a spot in memory 
# where we stored the number 2. After changing myint to 3, 
# it points to another spot in memory where we store the number 
# 3. They are different numbers, in different locations in your
#  computer’s memory. 
# All we do is point myint to another location.
myint= 2
myint = 3

# If we modify a list, it will change the data in the same
# location in memory, where the pointer points

print(type(3))
print(type('hello'))
print(type([3,2,1]))

# Python 3 can hold large values, and only has one type of int

# Converting to int
print(int('100'))

# Converting to str
print(str(100))

# Float to int
print(int(2.3))

# Using randomly generated numbers
# Int - Range 1 to 10 inclusive
print(random.randint(1,10))

# Checking if a value is an integer
check = 2
print(type(check)) 

if isinstance(check, int):
    print('it is an int')
else:
    print('its not an int')

#dont use type(2) == int (lol)










