from dataclasses import dataclass
from dataclasses_json import dataclass_json

# Python Data Class: A Better Way to Store Data

# A python data class is a regular class that has the @dataclass decorator. It is specifically
# created to hold data.

# built-in module called dataclass

# advatantages of using a data class

#   1. Requires a minimal amount of code: the @dataclass decorator adds a lot of functionality to
# a class without adding any visible code. All you need to do is define your fields to hold your
# data. No need to define functions

#   2. Comparison: Two Python data classes can be compared with "==" because the so-called dunder
# method __eq__ is implemented automatically.

#   3. Printing a data class: because __repr__ is implemented, you can print data classes and get
# a nice representation of it. This helps when debugging.

#   4. Data classes require type hints: Using type hints reduces the chances of bugs and 
# unexpected behavior in your code. You essentially declare the type of data that should be stored 
# in a variable

# Ex.
@dataclass
class Card:
    rank: str
    suit: str

card = Card("Q", "hearts")
card2 = Card("Q", "hearts")

# Comparing data classes
print(card == card2) # True

# Acessing rank from Card
print(card.rank) # 'Q'

# Print details about the data class
print(card) # Card(rank='Q', suit='hearts')


# Defining default values
@dataclass
class Book:
    title: str = "Learning Python"
    author: str = "James Bond 007"

# Crating an instance of Book with default values
book = Book()

print(book) #Book(title='Learning Python', author='James Bond 007')


# Converting a data class to JSON

# An alternative is to inherit from the JSONEncoder class:
# https://www.bruceeckel.com/2018/09/16/json-encoding-python-dataclasses/

# A common use case is to convert your nicely structured data class to JSON. E.g., if you want 
# to export the data to a database, or send it to the browser.

# Using dataclasses-json

@dataclass_json
@dataclass
class Cup:
    brand_name: str = 'Starbucks'
    type: str = 'Mug' 

newCup = Cup()
print(newCup.to_json())
