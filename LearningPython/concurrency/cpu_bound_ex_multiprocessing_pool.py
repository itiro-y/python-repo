import time
import multiprocessing

# Multiprocessing example using pool
# This took 5.118s to run
# not a big difference from the 5.943s of the same version of the code but without pool

# This Python multiprocessing helper creates a pool of size p processes. If you don’t supply 
# a value for p, it will default to the number of CPU cores in your system, which is actually 
# a sensible choice most of the time.

# A CPU heavy calculation
def heavy(n, myid):
    for x in range(1, n):
        for y in range(1, n):
            x**y
    print(myid, "is done")

def doit(n):
    heavy(500, n)

def pooled(n):
    # By default, our pool will have numproc slots
    with multiprocessing.Pool() as pool:
       pool.map(doit, range(n))

if __name__ == "__main__":
    start = time.time()
    pooled(80)
    end = time.time()
    print("Took: ", end - start)