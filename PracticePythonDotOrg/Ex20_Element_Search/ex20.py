# Element Search

from math import ceil, floor


def main():
    a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    a_num = 2
    print(a_list)
    print(f'key: {a_num}')
    sort_list = sorted(a_list)

    if binarySearch(sort_list, a_num):
        print('the number is within the list')
    else:
        print('the number is NOT within the list')    

def elementSearch(get_list, get_num):
    # input: takes an ordered list of numbers (ascending order), and another number
    # return: Bool -> whether the number is within the list or not 

    for i in range(len(get_list)):
        if get_list[i] == get_num:
            return True
    return False

def binarySearch(get_list, get_num):
    # input: takes an ordered list of numbers (ascending order), and another number
    # return: Bool -> whether the number is within the list or not 
    temp_list = get_list.copy()
    while True:
        mid = floor(len(temp_list) / 2)
        if get_num > temp_list[len(temp_list) - 1] or get_num < temp_list[0]:
            return False  
        elif get_num == temp_list[mid]:
            return True  
        elif get_num > temp_list[mid]:
            temp_list = temp_list[mid: len(temp_list)]
            print(temp_list, mid)
        elif get_num < temp_list[mid]:
            temp_list = temp_list[0: mid]
            print(temp_list, mid)
        else:
            return False
                  

if __name__ == '__main__':
    main()