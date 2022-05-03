# Odd or Even

def main():
    number = int(input('Write a number: \n > '))
    check = int(input('Write a number to divide your previous number: \n > '))

    if number % check: 
        print("The number is not multiple of your 'check' number!") 
    else:
        print('The number is a multiple of the chosen number!')
        if number % 4 == 0:
            print('The number is also a multiple of 4')
    


if __name__ == '__main__':
    main()