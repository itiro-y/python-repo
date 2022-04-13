# f Strings
# same code as ex1

def main():
    name = input('What is your name: \n > ')
    age = int(input('What is your age: \n > '))
    rep_lines = int(input('How many times you want this line to repeat? \n > '))
    current_year = 2022
    year_age_100 = current_year + (100 - age)

    for i in range(rep_lines):
        print(f'{name} you will be 100 years old in {year_age_100}')
    

if __name__ == '__main__':
    main()