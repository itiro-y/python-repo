from concurrent.futures import process
import time
import multiprocessing

# Multiprocessing example

# This took 5.943s to run this code
# (61.1% faster) compared to the threaded version of the code
# My computer has 4 physical cores, so it makes sense to be ~4x as fast as only running with only
# 1 core

# This perfectly demonstrates the linear speed increase multiprocessing offers us in the case of 
# CPU-bound code.

# A CPU heavy calulation
def heavy(n, myid):
    for x in range(1, n):
        for y in range(1, n):
            x**y
    print(myid, "is done")

def multiproc(n):
    processes = []

    for i in range(n):
        p = multiprocessing.Process(target=heavy, args=(500, i))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()

if __name__ == "__main__":
    start = time.time()
    multiproc(80)
    end = time.time()
    print("Took: ", end - start) 