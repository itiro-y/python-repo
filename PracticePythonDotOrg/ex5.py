# List Overlap

import random

def main():
    list_1 = []
    list_2 = []

    for i in range(random.randint(1, 10)):
        list_1.append(random.randint(0, 10))
        list_2.append(random.randint(0, 10))

    print('this is list 1: ', list_1)
    print('this is list 2: ', list_2)
    set_1 = set(list_1)
    set_2 = set(list_2)

    print('this is what they have in common: ', list(set_1 & set_2))

    # list_1 = [1, 2, 3, 4, 5, 6]
    # list_2 = [1, 1, 1, 2, 3, 2]
    # one line challenge print(list(set(list_1) & set(list_2)))

if __name__ == '__main__':
    main()    