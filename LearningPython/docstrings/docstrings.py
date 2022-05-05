# Docstring allows you to document your code more formally

# What is a docstring?
#   is a tring that occurs as the first statement in a module, function, class, method definition
#   such docstring becomes the __doc__ special attribute of that object

# A comment vs docstring: a comment is ignored completely by the Python interpreter, while a docstring
# is an actual string that the interpreter sees. We don't assign the string, so it's considered useless
# by the interpreter while running the code and is effectively ignored.

# Python can find and show the docstring when asked for, since it gets assigned to the __doc__ special 
# attribute


# How to create Python docstrings?
#   simnply insert a string as the first statement of any module, function, class, or method

#ex
class MyDocumentedClass:
    """This class is well documented but doesn't do anything special"""

    def do_nothing(self):
        """This method doesn't do anything but feel free to call it anyway"""
        pass

# Triple quotes are used so docstrings are more recognizable and also multi-line


# How to read docstrings?
#   instead of accessing it with __doc__, we call help()
print(help(MyDocumentedClass))

# you can use help() on any object in Python
print(help(print("")))