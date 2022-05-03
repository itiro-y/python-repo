# Divisors
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is 
# a divisor of 26 because 26 / 13 has no remainder.)

def main():
    num = int(input('Enter a number: '))
    temp_list = []

    for i in range(1, 100):
        if num % i == 0:
            temp_list.append(i)

    print(f'The list of divisors is here: \n {temp_list}')

if __name__ == '__main__':
    main()