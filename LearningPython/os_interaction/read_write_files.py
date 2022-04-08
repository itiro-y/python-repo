#Open a file (old fashion)
# f = open('text.txt')
# print(f.read())
# f.close()

# with the with-statement
with open('D:\PythonStuff\LearningPython\os_interaction\\text.txt') as f:
    text = f.read()

print(text)