# Pipenv: A Better Package Manager

# Advantages:
#   Combines pip and virtualenv into one tool
#   Separates your top-level dependencies from the last tested combination
#   Encourages the use of latest versions of dependencies to minimize security
#       risks, and it also scans for known vulnerabilities
#   Insight into dependency graph with 'pipenv graph'
#   Hashes all dependencies. It will detect packages that have been tampered with
#       after you initially included them as dependency
#   Can also work with requirements.txt, if it has one it will automatically detect it
#       and convert it into a Pipfile


# Installing Pipenv

# cmd: pip install --user pipenv
# it installs locally

# cmd on MacOs or Linux (Homebrew): brew install pipenv


# Using Pipenv

# First create a directory, cd into the directory and install your first dependency
# cmd: pipenv install requests

# What happens:
#   pipenv detects there's no virtual env. yet, so it creates one
#   it install requests
#   it creates two files: Pipfile and Pipfile.lock

# After all it's done, you can enter the virtual env. with:
# cmd: pipenv shell

# or run a Python script inside the virtual env.
# cmd: pipenv run python3 mymodule.py

# Pipfile shows our top-level requirements
# Pipfile.lock its basically an advanced 'pip freeze'
#   it shows the combination of packages that are guaranteed to work


# To find where was the virtual env was created
# cmd: pipenv --venv

# The venv is also located at somewhere outside of our project structure
# venv with same names won't be reused, as Pipenv uses hash pased on the path to your venv


# Separating Development Packages

# development requirements vs production requirements
# cmd: pipenv install pytest --dev

# so another developer can work on your project and install all requirements (including dev requiremnts)
# cmd: pipenv install --dev


# Dependency Management

# Pipenv will warn you when dependencies are outdated or has version requirements
# cmd: pipenv graph
# will display a nice insigh of your dependencies


# Detection of Security Vulnerabilities
# it uses the safety package and scans your packages for security vulnerabilities
# cmd: pipenv check





