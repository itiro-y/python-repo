from pyexpat import version_info
import sys

# Check Python Version In Code

# You can check for the Python version in your code, to make sure your users are not running 
# your script with an incompatible version.

# using module sys
# using sys.version_info function

if not sys.version_info > (2, 7):
    # user cannot use a python version 2.7-
    print("Incompatible Python Version ( > 2.7 )")
elif not sys.version_info >= (3, 5):
    # display that user needs to upgrade as the program is using python 3.5+ features
    print("Please note that this program uses Python 3.5+ features. Upgrade your Python version! ")
else:
    print("Your python version is compatible with this program. Python 3.5+")
