import os
import shutil

#Open a file (old fashion)
# f = open('text.txt')
# print(f.read())
# f.close()

# with the with-statement
# the file can only be used in the with statement
# if you need to open the file once more, you need to open the file again

# open() -> mode argument (rt or "read-text" by default)

# Mode arguments
# r -> open file for reading (default)
# w -> open file for writing, truncating the file first
# x -> create a new file and open it for writing
# a -> open for writing, append to the end of the file if it exists already
# t -> text mode (the default) can be used in combination with rwxa (expecting to be a .txt file)
# b -> binary mode (opposed to text mode), can be used in combination with rwxa
# + -> open a disk file for updating (reading and writing)

# txt files are located in workspace (in this ex. PythonStuff)
# with open('random-text.txt') as f:
#     text = f.read()
# print(text)
# write file -> use 'w' and 't' (leave it out as it is the default)

with open('text.txt', 'w') as f:
    for i in range(1,5):
        f.write(f'Number {i} \n')

# By default, the writing mode overwrite anything that's already in the file
# To add new content to an existing file we use the 'a' mode
with open('text.txt', 'a') as f:
    for i in range(5,8):
        f.write(f'Number {i} \n')

with open('text.txt', 'r') as f:
    print(f.read())


# Python read file to list
with open('text.txt') as f:
    #list(f) or f.readlines()
    lines = f.readlines() # lines = ['content within the file']

print(lines)

# Read file line-by-line
# Parsing the file line by line
# We treat the opened file as an iterator using a for loop
with open('text.txt', 'r') as f:
    for line in f:
        print(line)

# Common Python file operations
# os library -> deleting files, creating directories, moving files...

# Checking if a file exists
if os.path.isfile('text.txt'):
    print('The file exists')

# Checking if a directory exists
if os.path.isdir('LearningPython\\os_interaction'):
    print('The directory exists')    

# Creating a directory
# os.mkdir('mydir')

# Deleting a file
# os.remove('text.txt')

# Rename or Move a file
# works as long as the file stays on the same file system
# os.rename('text.txt', 'newtext.txt')

# Moving the file system to another
# Move a file with shutil
# import shutil (/ at the end keeps the file name)
#shutil.move('newtext.txt', '/PythonStuff/LearningPython/os_interaction/')

# Copy a single file with Python
#shutil.copy('text.txt', '/PythonStuff/LearningPython/os_interaction/text_copy.txt')

# Copy an entire tree of files
#shutil.copytree('mydir', 'mydir_copy')

# Remove a tree of files
#shutil.rmtree('mydir')

# Handling Python file exceptions
# use try except blocks to handle OSError or SameFileError
# the common ones in shutil

# Unix file permissions (linux), but how we do in windows?
# Files permissions
# Permissions are specified per file
# r -> the file can be read
# w -> the file is writeable
# x -> the file is executable
# - -> unset, permission not granted

# Users and groups
# Computer systems usually have multiple users and groups
# Each file has permission for three access types
    # Everybody else, also called 'world'
    # Group: a group of 0 or more users
    # User: the owner of the file. The one who creates a file, automatically becomes the owner

# The permissions are listed in this order as well
# Resulting in a nine-character long string
#   World   Group   User
# 0 123     456     789
# - rwx     r-x     r-x 

# Positions 1, 2, 3 define permissions for the entire world
# Positions 4, 5, 6 define permissions for the group that the user is in
# Positions 7, 8, 9 define permissions for the user
# Position 0 is the file type

# File Types
# -: regular file
# d: directory
# c: character device file
# b: block device file
# s: local socket file
# p: named pipe file
# l: symbolic link




