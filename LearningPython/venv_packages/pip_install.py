# Pip install is the command you use to install Python packages with
# the Pip package manager

# Two ways to install Python packages
#   1. Manual installation
#   2. Using a requirements.txt that defines the required packages and their version


# Python: Install Pip

# Pip comes with your Python intaller (usually)
# check if pip is installed: pip help or pip3 help or python3 -m pip help
# if all fails you need to install yourself

# Install Pip on Windows and Mac
# download a script to install pip (get-pip.py) and run it from cmd: python3 get-pip.py


# Pip Install Python packages
# pip is present in you venv, so everything will be installed locally

# it's good to install pip system-wide
# so we use pip to install pip or update it: sudo pip3 install --upgrade pip (make sure
# you are outside venv)

# pip tries to install a package system-wide by default.
# so if you don't use sudo or become adm you might get permission erros
# Installing generic libs is fine, eg. NumPy, pandas, Jupyter Notebook


# Install locally (no root or super user)

# using the --user option
# eg. pip install --user simplejson
# it will install at %APPDATA%\Python


# Pip install requirements.txt file
# check requirements.txt
# an alternative would be to use Pipenv or Poetry
# there tools have an advanced dependancy management and will resolve
# all the dependancies automatically, if possible

# easily creating an requirements.txt file
# run cmd: pip freeze > requirements.txt
# this will create a file with all the current installed dependencies,
# including version numbers

# install from a requirements.txt file
# run cmd: pip install -r requirements.txt

# Custom repository with pip install -i

# by default the PyPI repository is located at https://pypi.org/simple/
# You can specify a custom repo using: -i or --index--url

# cmd: pip install -i https://your-custom-repo/simple <package name>
# or
# cmd: pip install -i /path/to/your/custom-repo/simple <package name>


# Editable install with pip install -e

# When creating your own package
# If you want to fix someone else's package
# If you want to install a bleeding edge version of package

# Editable install opion is called -e or --editable

# cmd: pip install -e .
# if you're not in project root, simply supply the path to the package instead of a dot


# Pip uninstall

# To uninstall a package, cmd: pip unistall <package name>
# Using a requirements file to uninstall packages, cmd: pip unistall -r requirements.txt


# Using pip to get info about a package, or about the currently installed packages

# cmd: pip list
# listing installed packages

# cmd: pip show <package name>
# gets package details

# Search engines for packages: DuckDuckGo, Google...
