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



