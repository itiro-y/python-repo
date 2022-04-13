# Lists
# can be of any datatype and mixed
# can create list of lists

my_list = [1, 2, 3]
empty_list = []

nested_list = [{1, 2, 3}, (4, 5, 6), [7, 8, 9]]

# list() -> convert datatypes into lists
l1 = list(range(1,4))
print(l1) # [1, 2, 3]

l2 = list((1, 2, 3))
print(l2) # [1, 2, 3]

# Accessing lists index
print(nested_list[0]) # {1, 2, 3}
print(nested_list[1]) # (4, 5, 6)
print(nested_list[2]) # [7, 8, 9]

#.append() adds a element at the end of that list
nested_list[2].append(10)

print(nested_list[2]) # [7, 8, 9, 10]

print(nested_list[1][1]) # 5 (can do this with tuples and lists, but not sets)


# Adding or combining two python lists
l3 = l1 + l2
print(l3)

# Or use .extend() to add combine one and not change the 
# list used to combine
l1.extend(l2)
print(l1)

# pop(index or empty) removes and returns the last item in a list
print(l1.pop())
print(l1)
print(l1.pop())
print(l1)
print(l1.pop())
print(l1)
print(l1.pop(0))
print(l1)

# del() deletes or remove items without returning the removed item
# it can also delete lists
del(l1[0])
print(l1)

del(l1)

# .remove() removes a specific value from the list
# it removes the first occurance of that value in the list
# from left to right
l1 = [1, 2, 3, 2]
l1.remove(2)
print(l1)


# .clear() clears all items form a list
l1.clear()
print(l1)

# removing duplicats -> turn into set -> back to list
# can also keep it as a list if needed to optimize efficiency
l1 = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4]
l1 = list(set(l1))
print(l1)


# Assigning a new value to a list
l1[0] = 0
print(l1)

# list length
print(len(l1))

# counting occurance ina list
l1.append(0)
print(l1.count(0))

# checking if an item is in the list
if 3 in l1:
    print('3 is in l1')

# finding the index of a item in the list
# .index(value, start, stop), so you can specify the range of the search
print('the index of 3 is ', l1.index(3))

# looping over a list
my_list = [1, 2, 3, 4, 5]
for i in my_list:
    print(i)

# converting an entire list into a string
string = str(my_list)
print(type(string), string)

# sorting
list_1 = [3, 2, 123, 124, 16324, 1346, 1453, 1346]

#.sort() sorts the list itself
# ascending
list_1.sort() #changing the actual variable when sorting
print(list_1)

# decending
list_1.sort(reverse=True) 
print(list_1)

#sorted() returns a new sorted list
list_2 = sorted(list_1) #does not change the original list
print(list_1, list_2)

# can sort strings with ascii
list_3 = ['b', 'c', 'a', 'e', 'f', 'd']
print(sorted(list_3))

# cant sort a list with both numbers and strings
list_not_sorted = [1, 'a', 2, 'b']

# python list slicing
# my_list[start:stop(exclusive):step]
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[0:3]) # index 0 to 2 (3 first items)
print(my_list[:3]) # start is 0 by default
print(my_list[3:]) # start at index 3
print(my_list[::2]) # step 2 by 2 (1 by default)

# Going backwards
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# index     -9 -8 -7 -6 -5 -4 -3 -2 -1
print(my_list[-1:-3:-1]) # 9, 8

# Reversing lists
# using .reverse() -> it reverses the original list
my_list.reverse()
print(my_list)

#back to normal
my_list.reverse()
print(my_list)

# using slicing to reverse
new_list = my_list[::-1]
print(new_list)

print(my_list)

# using the reversed() function
new_new_list = list(reversed(my_list))
print(new_new_list)


#-------------------------------------------------------------------------------------------------------

# zip() to convert a dict into 2 lists (one of values and another for keys)
month = { "jan": 1, "feb":2, "march":3}

# dict.items() returns key:values as tuples
print(month.items())

# zip() at the memory location (* to unpack the tuple into a single tuple)
print(zip(*month.items()))

# finally convert it back to lists
# now we have [(keys), (values)]
print(list(zip(*month.items())))





