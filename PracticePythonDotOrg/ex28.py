# Max of Three

def main():
    largest = maxOfThree(4, 5, 1)
    print(largest)

def maxOfThree(num_1, num_2, num_3):
    list_num = [num_1, num_2, num_3]
    list_num = sorted(list_num)
    return list_num[2]

if __name__ == '__main__':
    main()