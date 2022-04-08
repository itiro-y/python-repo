# List Remove Duplicates

def main():
    a = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 6, 6, 7, 8, 9]
    remDuplicatesLoop(a)
    remDuplicatesSets(a)

def remDuplicatesLoop(get_list):
    temp_list = []
    for i in get_list:
        if i not in temp_list:
            temp_list.append(i)
    print(temp_list)        
        

def remDuplicatesSets(get_list):
    temp_list = list(set(get_list))
    print(temp_list)

if __name__ == '__main__':
    main()