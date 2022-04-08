import json

# Dictionary
# holds key-value pairs

phone_numbers = { 'Jack': '070-123123', 'Pete': '071-123123' }
my_empty_dict = {}

#Accessing
print(phone_numbers['Jack']) # '070-123123'

config = {'host': 'example.org'}
# Retrieving values with .get(str, if not found: default value)
print(config.get('port', 80)) # returns 80 as 'port' is not in the dict

print(config.get('schema')) # returns None as the default value when not specified

# Overwrite data
phone_numbers['Jack'] = '070-321321'
print(phone_numbers)

# If a key does not exist, an exception of type KeyErro is thown
# phone_numbers['Lisa'] KeyError: 'Lisa'

# Nested values in dictionaries
a = {'subdict': {'b': True}, 'mylist': [100, 200, 300]}

print(a['subdict']['b']) #True
print(a['mylist'][0]) #100

# The Key: must be hashable (Lists, dict, sets won't work)
# it must be immutable: its data cannot be changed
# eg. tuple, float, int, class name or object based on a class

crazy_dictionary = {int: 1, float: 2, dict: 3}
crazy_dictionary[dict] #3

# class P:
#     pass

# crazy_dictionary[P] = 1
# p = P()
# crazy_dictionary[p] = 2

# using numbers as keys
runners = {1000: 'Jack', 1001: 'Eric', 1002: 'Lisa'}
print(runners[1001]) # Eric

# converting certain data types into dict
# eg. a tuple of tuples
my_list = (('Jack', '123123123'), ('Lisa', '123123123'), ('Eric', '123123123'))
my_new_dict = dict(my_list)
print(my_new_dict) # {'Jack': '123123123', 'Lisa': '123123123', 'Eric': '123123123'}

# Dictionary comprehensions
print({x: x**2 for x in range(3)})

# Using dict.fromkeys()
# It creates a new dict, based on the list of keys supplied
# All elements' values will be set to None by default if not supplied
# it can be a list, tuple, set
name = {'Jack', 'Josh', 'Andrea'}
phone_numbers_2 = dict.fromkeys(name, ' ')
print(phone_numbers_2)

# Parse a JSON object to dict
jsonstring = '{ "name":"erick", "age":"38", "married":"true"}'
dict_from_json = json.loads(jsonstring)
print(dict_from_json)
print(dict_from_json['name'])

# Checking if a key exists in a Dict
if 'Jack' in my_new_dict:
    print(my_new_dict['Jack']) #123123123
elif 'Jack' not in my_new_dict:
    print('Jack is not in the dict')

# Getting the length of a Python dict (returns the numbers of keys)
print(phone_numbers)
print('this is the length of phone numbers:', len(phone_numbers))

# Using .keys() and .values()
# it returns a view object on keys and
phone_numbers_3 = {'Jack': '070-02222748', 'Pete': '010-2488634', 'Eric': '06-10101010'}
names = phone_numbers_3.keys()
numbers = phone_numbers_3.values()

# Even though Linda was added after the view object was created
# She still appears as part of the list
# So, a view object is changed if the dict is changed regardless of the order in which it changed
phone_numbers_3['Linda'] = '030-987612312'
print(names)
print(numbers)

#Loop through a view object
for number in numbers:
    print(number)

for name in names:
    print(name)

# .items() method returns an iteerable view object of both keys and values
for name, phone_num in phone_numbers_3.items():
    print(name, ':', phone_num)

# Using list() or sorted() to get keys
# to return a native list so they can be manipulated
print(list(phone_numbers_3))
print(sorted(phone_numbers_3))

# Merging dicts
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# new operator | from python 3.9+
# can be merged as tuples merged = {**dict1, **dict2}
merged = dict1 | dict2
print(merged)

# Comparing dicts
# simply compare with ==
# order does not matter
# order of dict is determined by the order in which you insert items
print(dict1 == dict2) # False

first_dict  = { 'a': 1, 'b': 2, 'c': 'a string' }
second_dict  = { 'b': 2, 'a': 1, 'c': 'a string' }
print(first_dict == second_dict) # True even though is not in the same order

popped = first_dict.pop('a')
print(popped)
print(first_dict)

# Built-in methods for dict()

# .clear() -> empty dict / remove all keys and values

# .get(key, default_value*) -> gets an item with the given key or returns default value

# .items() -> returns a view object of both keys and values

# .keys() - > returns a view object of keys

# .values() -> returns a view object of values

# .pop(key, default_value) -> returns and removes the element specified with the key

# .popitem() -> return and removes the last inserted item or a random item

# .setdefault(key, value) -> returns the value of the specified key. If the key dne, its inserted with the given value

# .update(iterable) -> add all pairs from given iterable. Eg. phone_numbers.update({"Alina": 1234, "Alice": 1234})



