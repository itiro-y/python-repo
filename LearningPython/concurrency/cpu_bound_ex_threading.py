import threading
import time

# A CPU-Bound Python threading example
# Took 24.637s to run this code
# An improvement of 6.038s (10.9% faster) from the single threaded version

# If the heavy function had a lot of blocking IO, like network calls or filesystem operations, 
# this version would be a big optimization. The reason this is not an optimization for CPU-bound 
# functions is the Python GIL!

# A CPU heavy calculation
def heavy(n, myid):
    for x in range(1, n):
        for y in range(1, n):
            x**y
    print(myid, "is done")

def threaded(n):
    threads = []

    for i in range(n):
        t = threading.Thread(target=heavy, args=(500, i))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

if __name__ == "__main__":
    start = time.time()
    threaded(80)
    end = time.time()
    print("Took: ", end - start) 