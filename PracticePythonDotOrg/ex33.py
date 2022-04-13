# Birthday Dictionaries
# keys are names
# values are birth dates

def main():
    lines = []
    name_birth_dict = {}
    with open('/PythonStuff/PracticePythonDotOrg/name-birth-dict.txt', 'r') as f:
        for line in f:
            lines.append(line.strip().split('  ', 1))
    
    name_birth_dict = dict(lines)
    print(">>> Welcome to the birthday dictionary. We know the birthdays of: \n")
    for i in name_birth_dict.keys():
        print(i, '\n')
    user_input = input("Who's birthday do you want to look up? \n >")
    print(f"\n {user_input}'s birthday is {name_birth_dict[user_input]}")


if __name__ == '__main__':
    main()