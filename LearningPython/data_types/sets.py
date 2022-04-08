# Sets
# Set can only contain UNIQUE VALUES
# Sets are UNORDERED

def main():
    names = { "John", "Ali", "Eric"}
    mixed_sets = {1, 'a', (1,2)}

    #creating an empty set with .set()
    my_set = set()
    my_set.add(1)
    my_set.add('Ali')
    print(my_set) #1, Ali

    # add multiple elements at once, need to use the .update()
    # update() only takes iterable objets like list, range, tuple
    my_set_2 = set()
    my_set_2.update(range(3))
    my_set_2.update(['a', 'b'])
    print(my_set_2)

    # set to convert any iteratle object into a set
    print(set([1, 2, 3, 4, 5])) # {1, 2, 3, 4, 5}

    # Sets as comprehensions
    # this comprehension makes a list of chars from the string
    # excluding , . or whitespaces
    # the list is completely RANDOM
    my_set_3 = {x for x in "Hi, my name is..." if x not in '., '}
    print(my_set_3)

    # Mathematical Python Set Operations
    # Two sets: A and B
    # 1) The difference between two sets. Only present in A, and not
    # overlapping with elements in B [all elemnets that are in A but not in A ∩ B]
    A = {1, 2, 3, 4, 5}
    B = {3, 4, 5, 6, 7}

    # - operator
    print(A-B) # {1, 2}

    print(B-A) # {6, 7}

    # 2) Find the Symmetric Difference Between Python Sets
    # elements in A and in B but not in A ∩ B

    # ^ operator
    print(A^B) # {1, 2, 6, 7}
    
    #3) Find the Intersection of Two Python Sets
    # A ∩ B

    # & operator
    print(A&B) # {3, 4, 5}


    # 4) Subsets and Supersets
    #  A is a subset of B if B has all the elements present in A
    A = {1, 2, 3}
    B = {1, 2, 3, 4, 5}
    C = {1, 2, 3, 10}

    # Subset: < operator
    print(A < B) # True, as all elements in A is in B

    print(C < B) # False, as one element in C is not in B

    # B is a superset of A if B has all the elements of A but it may also
    # have some extra elemtents.

    # Superset: > operator
    print(B > A) # True, as B has all the elements present in A (and more)

    print(B > C) # False, as C has one element that is not present in B

    # print(A < A) # False, as A is not a subset to A

    # print(A <= A) # True, as A is a subset or equal to A

    # print(A >= A) # True, as A is a superset or equal to A

    # Unions
    # Add two python sets and only keep elements that are unique
    # A ∪ B

    A = {1, 2, 3}
    B = {3, 4, 5}

    # | operator
    print(A|B) # {1, 2, 3, 4, 5}
    print(A.union(B))

    # <= can be called as .issubet()
    # >= can be called as .issuperset()
    # | can be called as .union()
    # & can be called as .intersection()
    # ^ can be called as .symmetric_difference()
    # - can be called as .isdisjoint()

    # using this format is better as the method takes any iterable object
    # so we can compare a set A and a list B without having to convert B into a set

    # IMPORTANT NOTES: Sets cannot be accessed by index as my_set{2}


if __name__ == '__main__':
    main()
