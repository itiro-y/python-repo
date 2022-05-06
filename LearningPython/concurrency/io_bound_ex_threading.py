from asyncio import threads
from concurrent.futures import thread
import threading
import time

# An IO-Bound Python threading example
# An I/O intensive calculation
# We simulate it with sleep

# Even though we have 80 Python threads all sleeping for two seconds, this code still finishes in 
# a little over two seconds. While sleeping, the Python threading library can schedule other 
# threads to run.
def heavy(n, myid):
    time.sleep(2)
    print(myid, "is done")

def threaded(n):
    threads = []

    for i in range(n):
        t = threading.Thread(target=heavy, args=(500, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join

if __name__ == "__main__":
    start =  time.time()
    threaded(80)
    end = time.time()
    print("Took ", end - start)

