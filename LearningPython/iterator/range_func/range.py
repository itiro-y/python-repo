# The range() function
# When used in a for loop the range() function can be treated as a built-in function
# that returns an iterable object

# With one argument -> counts from 0 to stop 
# range(stop)

# With two arguments -> counts from start to stop
# range(start, stop)

# With three arguments -> it counts from start to stop, with a defined step
# range(start, stop, step)

# 0 to 101, step = 10
for i in range(0, 101, 10):
    print(i, end=" ")

# range with negative step size
# range will count backwards
# start > stop
for i in range(5, 0, -1):
    print(i, end=" ")

# But how a python range() works?
#   A range is an iterable object, and this object can return an iterator that keeps
# track of its current state.

#   When we start iterating over a range object, the range object will return an iterator.
# the iterator sets a start, end, and step value, but also a counter variable i (that is 
# initialized to 0 by default and increases on each iteration)

#   On each call: next = start + step*i
#   Ex. range(3)
#   1st call: 0 + 1*0 == 0, range() returns 0 and sets i == 1
#   2nd call: 0 + 1*1 == 1, range() returns 1 and sets i == 2
#   3rd call: 0 + 1*2 == 2, range() returns 2 and sets i == 2
#   4th call: reached the end of range. StopIteration exception is raised

my_range = range(0, 3)

# Obtain the iterable object
my_iter = iter(my_range)

# Request values from the iterable
# 1st call
print(next(my_iter))

# 2nd call
print(next(my_iter))

# 3rd call
print(next(my_iter))

# 4th call (raises a StopIteration exception)
# print(next(my_iter))

# Conclusion, a range object is an iterable, and is an object that can return an iterator
# The iterator can be requested manually, like we did in the example above with iter() and next
# Or it can be requested automatically as in a for loop for example

# range vs list
#   range have the advantage over list because they require a constant, predictable amount of memory
# since they are calculated on the fly (step by step).

#   all range needs are the start, stop, step. therefore, range(1000) == range(1)
#   a list with values from 0 to 999 takes a thousand more times more memory

# In Python 2, range would materialize into an actual list of numbers!

# Some common practices with range()
#   Converting range to list
my_list = list(range(0,3))
print(my_list)

#   Testing for membership
my_num = 10
print(my_num in range(0, 11)) #True

#   Range slicing
# 0, 1, 2, 3, 4 slices index 2 to 4
print(list((range(0, 5)[2:4]))) # 2, 3

print(list(range(0, 5)[4:2:-1])) # 4, 3


#   Comparing ranges (compares sequence until Python 3.3)
print(range(0, 2) == range(0,3)) # False

print(range(0) == range(4, 2)) # True

# range(0) == []
# range(4, 2) == []
# So, they are equal





