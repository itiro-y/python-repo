#a single python file that perform tasks - script
#a python file that store functions, classes, other definitions - module
#we import modules
#My advice: only import specific elements to stay in control of your namespace.

def greeter():
    print('hello from modules.py')

def my_function():
    print('hello world')

my_variable = 10

if __name__ == '__main__':
    greeter()

