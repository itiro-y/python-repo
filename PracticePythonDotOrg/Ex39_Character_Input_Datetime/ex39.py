# Character Input Datetime
# code from ex1 using datetime lib from python std lib

import datetime

def main():
    name = input('What is your name: \n > ')
    age = int(input('What is your age: \n > '))
    rep_lines = int(input('How many times you want this line to repeat? \n > '))
    current_year = datetime.datetime.now()
    year_age_100 = current_year.year + (100 - age)

    for i in range(rep_lines):
        print(f'{name} you will be 100 years old in {year_age_100}')
    

if __name__ == '__main__':
    main()