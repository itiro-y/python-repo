def main(): 
    # List comprehensions
    # [ <expression> for item in list if <conditional>] syntax
    # creating a list based on an existing list
    # the if part act as a filter (if True it includes, False omittes)
    # 
    my_comp_list = [x for x in range(1,10) if x % 2 == 0]
    print(my_comp_list)

    # calling a function in the expression slot.
    # x is defined to be [0, 1, 2, 3, 4, 5, 6, 7]
    # where some_function() is being called for every item in that list
    my_comp_list_2 = [some_function(x) for x in range(8)]
    print(my_comp_list_2) 

    # creating a matrix using nested list comprehension
    # [[j for j in num_of_column] for i in [num_of_row]]
    # better coding style than making a matrix with a nested for loop
    my_comp_list_3 = [[j for j in range(3)] for i in range(10)]
    print(my_comp_list_3)

    # flatten the matrix into a one dimentional list
    print([value for sublist in my_comp_list_3 for value in sublist])

    # Set comprehensions are just like lists but with {}
    # "s % 2 == 1" is the same as "s % 2" where it only sorts the odds
    my_comp_set = [s for s in range(1, 5) if s % 2]
    print(my_comp_set)

    # Dictionary Comprehension
    # it takes a key and a value
    my_comp_dict = {x: x**2 for x in (2, 4, 6)}
    print(my_comp_dict)


def some_function(a):
    return (a + 5) / 2

if __name__ == '__main__':
    main()


