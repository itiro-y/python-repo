# Virtual Environments And Package Management

# A Python venv allows you to keep Python packages in an isolated location from the rest of your
# system. This is in contrast with the other option, installing them system-wide.

# venv advantages over system-wide installation

#   Preventing version conflicts: certain projects do not support certain versions of libraries

#   Ease to reproduce and install: easy to define and install the packages specific to your project
#       you can define specific versions that works with that specific project

#   Works everywhere, even when not root
#       you can install lib on a system with shared host (pc at universities eg.) because you install
#       them locally


# A good alternative to vern -> containerization with Docker and Kudernetes

#-------------------------------------------------------------------------------------------------------------
# You can also use Pipenv which is the combination o venv and pip

# How to create a Python venv

# Python 3.4+
#   run in cmd: python -m venv [directory]

# This command will create a venv in the specified directory and copy pip and easy_install into it too

# Other Python versions
#   run in cmd: pip install virtualenv
#   run in cmd: virtualenv [directory]


# Python venv activation

# On windows: run a script that gets installed by venv -> directoryName\Scripts\activate.bat
# On Linux and MacOs: run a script that gets installed by venv -> directoryName\bin\activate


# How a Python venv works

# When you activate a virtual environment, your PATH variable is changed
# you can check the PATH echo on windows (%PAHT%) and MacOs/Linux ($PATH)
# venv's bin directory stands before everything else, so when the OS searches for a command it will
# first look at the closest PATH variable. In this case venv.

# directory example
# .
# L bin
# | L activate
# | L activate.csh
# | L activate.fish
# | L easy_install
# | L easy_install-3.7
# | L pip
# | L pip3
# | L pip3.7
# | L python -> python3
# | L python3 -> /usr/local/bin/python3
# |
# L include
# L lib
# | L python 3.7
# |   L site-packages
# L pyvenv.cfg

# OBS: 
#   Both python and python3 commands work
#   All packages will be installed in site-packages directory
#   We have activation sripts for multiple shell types (bash, csh, fish)
#   Pip is available under pip and pip3


# Deactivating the Python venv

# run code: deactivate (works on every OS)


# Deleting a Python venv

# first deactivate the venv, then run this code: rm -r venv (this case the virtual env. is 
# within a directory called'venv')


# Delete a venv with Pipenv

# its simple. run code: pipenv --rm (you must be at the directory where the Pipenv and Pipenv.lock files are)
# or find where the files are with: pipenv --env
# and delete that entire directory with: rm -rf




