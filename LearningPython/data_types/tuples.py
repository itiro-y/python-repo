# Python Tuples
# holds multiple values in a single variable
# its ordered, the value of the items are preserved
# A tuple can have duplicate values
# its indexed: you can access items numerically
# A tuple can have an arbitrary length

# But its immutable, cannot be changed once you define it
# Its defined by using optional () instead of []
# Immutable -> Hashed, can act as a key to a dictionary
my_tuple = (1,2,3)
my_tuple_2 = 1,2,3
my_tuple_3 = ('hey', 'okay')
my_tuple_4 = ('sure', 123, True)

#Convert from list/anything to tuple
print(tuple([1,2,3])) #(1, 2, 3)

#this is not a tuple
t = (1)

#but this is (explicitly signaling to Python)
t = (1,)

list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]


# We can umpack a list(of anything) in a tuple using *
tuple_5 = (*list_1, *list_2)

print(tuple_5) # (1, 2, 3, 4, 5, 6, 7, 8)


# Multiple assignment using Tuple
person = ('John', 40, True)
name, age, registered = person

print(person) # ('John', 40, True)

print(name) # 'John'
print(age) # 40
print(registered) #True


# Returning multiple values from a function
def get_user_data(userID: tuple):
    name, age, ID = userID
    return name, age, ID

name, age, ID = get_user_data(('jhn', 10, 1234))

print(name) #'jhn'
print(age) #10
print(ID) #1234


# Using Index
# my_tuple_4 = ('sure', 123, True)
print(my_tuple_4[1]) #123
print(my_tuple_4[2]) #True


# Cannot add new items/remove from a tuple
# But you can append to a new tuple with old values
t1 = (1,2,3)
t2 = (*t1, 4, 5, 6)
print(t2) # (1, 2, 3, 4, 5, 6)


# Getting tuple length
print(len(t2)) #6


# Apart from lists, tuples' values cannot be changed
# in other words it prevent erros when you don't want that value
# to be ever changed

# Apart from sets, tuples' values cannot be duplicated
# Sets are useful to deduplicate data

# Converting tuples to lists so the data can be modified
l1 = list(t2)
print(l1) # [1, 2, 3, 4, 5, 6]

# With the unpacking method (can be useful when adding it to
# some extra content)
l2 = [*t1, *t2, 'extra', 'extra']
print(l2)


# Converting tuples into a set
# t1 = (1,2,3)
s1 = set(t1)
print(s1) #{1, 2, 3}

# unpacking method
s1 = {*t1}
print(s1)

t1 = (1, 1, 2, 3)
s1 = set(t1)
print(s1) # {1, 2, 3} removing the duplicate value 1

# Converting it to a string
print(str(t1))