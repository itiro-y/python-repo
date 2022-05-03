import json
import traceback

# Exceptions

# keywords: try and except

# All non-system-exiting exceptions are derived from the Exception class

# Ex of hierarchy

# BaseException
# +--SystemExit
# +--KeyboardInterrupt
# +--Exception
    # +--ArithmeticError
        # +--FloatingPointError
        # +--OverflowError
        # +--ZeroDivisionError   
#...

# Concept

# try:
#   Protected code that might trigger an exception
# except:
#   Handle exception properly
# else:
#   Only when no exceptions
# finally:
#   Always run this code

# ex code
try:
    print(2/0)
except Exception:
    traceback.print_exc()

try:
    with open("not_here.txt", "r") as f:
        print(f.read())
except IOError as e:
    print("An error occurred:", e)

try:
    f = open("not_here.txt", "r")
    f.write("Hello Browld")
except IOError as e:
    print("An error occurred:", e)
finally:
    print("Closing the file now")
    f.close()

# Exception best practices

# Don't use blank except blocks
# eg try: .... except: ...
# this will not only catch most types of erros, but will also
# catch SystemExit and KeyboardInterrupt which means you won't
# be able to stop the program manually.

# a better practice would be to use except Exception, which will
# catch most types of errors and will prevent the exception of
# SystemExit and KeyboardInterrupt

#eg
# while True:
#     try:
#         print("blabla")
#     except Exception:
#         print("Something went wrong")

# In Python is better to 'ask for forgiveness'
# you try first if it doesnt work catch an exception

# In Java is better to ask for permission then try because
# exceptions can slow the program down 

user_json = '{"name": "John", "age":39}'
user = json.loads(user_json)

try:
    print(user['name'])
    print(user['age'])
    print(user['address'])
except KeyError as e:
    print("There are missing field in the user object:", e)

# Creating a subclass of the class Exception (all non-system-exiting exceptions)
# This means you can create your own type of error

class UserNotFound(Exception):
    pass


# Raising or Throwing exceptions
# keyword raise

def fetch_user(user_id):
    user = None

    # If the user is not found the function will raise an error of type UserNotFound
    # which will be handled later in the except block
    if user == None:
        raise UserNotFound(f'User {user_id} not in database')
    else:
        return None

users = [123, 456, 789]
for user_id in users:
    try:
        fetch_user(user_id)
    except UserNotFound as e:
        print("There was an error:", e)

# Printing a Python exception
# except Exception as e:
#   print("error:", e)

# or you can print the call stack just like python does with the traceback module (have to import)
# try:
# except Exception:
#     traceback.print_exc()  






