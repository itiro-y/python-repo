#Everthing in python is an object
#In python theres list not arrays
#None return means 'nothing'
#getting out of a infinite loop: ctrl + C

result = 'abc def ghj'
long_quote = """hahahahahahahahahahaha"""

#type of data class
print(type(result))

#string concatenation
print(result + result)

#uppercase lowercase functions
print(long_quote.lower())
print(long_quote.upper())

#size of string
print(len(result))

#split when whitespace, return list of separated strings
print(result.split())

#function that replaces strings or chars
print(result.replace('abc','+'))

#char at index 0 of string result
print(result[0])

#transverse the entire string
print(result[::-1])

#f-string for formatted strings (\t adds tab and \n a new line)
print(f'\t the abc starts with \n {result}')

#bool 
is_locked = True
is_enabled = True

if is_locked:
    print('the door is locked')

if(is_locked & is_enabled):
    print('the door is locked and enabled')

else:
    print('the door is open')

#comparison operators (>,>=,<,<=,==,!=)
a = 10
b = 10
if a == b:
    print(a==b, 'a is equal to b', a!=b)
else:
    print(a==b)

#comparison with strings (ascii comes to play when comparing)
string1 = 'abc'
string2 = 'abc'

if string1 == string2 and len(string1) == len(string2):
    print(f'string 1 equals string 2: {len(string1)} and {len(string2)}')
else:
    print('string 1 is not equal to string 2')

#iterate over string1 and display each char
for i in string1:
    print(i)
    #break out of loop (also have 'continue')
    if i == 'b':
        print('\n')
        break

#the range(6) [0,5], range(2,6) [2,5], range(2,6,2) [2,6] +2
#range(start,end+1,increment)
for i in range(6):
    print(i)
    if i == 3:
        break

#else statement for the FOR LOOP, it executes when the loop is completed (in exception of a break)     
else:
    print('the loop is finished')


#Nested loops
#for i in range(3):
    #for j in range(10):
        #print(i,j)

my_list = [1, 'asd', True]

#print list as its whole
print(my_list) 

#iterate over my_list and display its contents
for i in my_list:
    print(i)

#print the second item in my_list
print(my_list[1])

#lists of lists
my_matrix = [[0, 5], [1, 4], [2, 3]]

#print 3rd item and its second content
print(my_matrix[2][1])

count = 0
while count:
    print(count)
    count = count + 1

#funcion example
def print_name_function(name):
    print(f'the name is {name}')

print_name_function('John')

#function with two parameters
def function_name(parameter, parameter1):
    i = parameter + 10 + parameter1
    return i

print(function_name(10, 10))


#function with a default value/parameter
def type_code(num_1 = 10, code = 'nice'):
    print(num_1, code)

#invoking function with a default value
type_code()

type_code(11)

type_code('hello')

#named parameters
type_code(num_1 = 1, code = 'hello')

#positional parameters
type_code(1, 'hi')

#user input input('string')
prompt_num = input('Insert here number: ')
prompt_code = input('Insert here code: ')

type_code(prompt_num, prompt_code) 

#-----------------------------------------------------------------






















