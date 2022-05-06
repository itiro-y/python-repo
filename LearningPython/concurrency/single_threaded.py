import time

# Single threaded execution
# Took 30.675s to run this code

# Our test function (cpu heavy)
def heavy(n, myid):
    for x in range(1,n):
        for y in range(1,n):
            x**y
    print(myid, "is done")

def sequential(n):
    for i in range(n):
        heavy(500,i)

if __name__ == '__main__':
    start = time.time()
    sequential(80)
    end = time.time()
    print("Took: ", end - start)
