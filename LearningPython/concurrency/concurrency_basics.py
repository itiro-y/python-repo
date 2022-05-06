import time

# Starting with Python concurrency

# Our test function (cpu heavy)
def heavy(n, myid):
    for x in range(1,n):
        for y in range(1,n):
            x**y
    print(myid, "is done")

