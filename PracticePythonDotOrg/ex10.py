# List Overlap Comprehensions

import random
 
def main():
    # a = []
    # b = []
    # randomizeList(a)
    # randomizeList(b)
    # c = sorted(a)
    # d = sorted(b)
    rand_length = random.randint(1,10)
    a = sorted(random.sample(range(10), rand_length))
    b = sorted(random.sample(range(10), rand_length))

    print(' list a:', a, '\n', 'list b:', b)
    listOverlap(a,b)


def listOverlap(list1, list2):
    temp_list = list(dict.fromkeys([x for x in list1 for y in list2 if x == y]))

    if(len(temp_list) == 0):
        print(' There are no overlaps')
    else:
        print(f' The overlapped elements are: {temp_list}')

def randomizeList(get_list):
    list_length = random.randint(1, 10)
    for i in range(list_length):
        get_list.append(random.randint(0, 10))

if __name__ == '__main__':
    main()    
