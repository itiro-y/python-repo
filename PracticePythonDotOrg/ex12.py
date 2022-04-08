# List Ends

import random

def main():
    list_len = random.randint(1, 10)
    a = sorted(random.sample(range(10), list_len))
    print(f'This is list a: {a}')
    b = getFirstLast(a)
    print(b)
    

def getFirstLast(get_list):
    list_len = len(get_list)
    temp_list = []
    temp_list.append(get_list[0])
    temp_list.append(get_list[list_len - 1])
    return temp_list

if __name__ == '__main__':
    main()