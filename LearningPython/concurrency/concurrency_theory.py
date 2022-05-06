# Python Concurrency: Divide and Conquer

# Concurrency is working on multiple things at the same time
# There are several ways you can do that

# Threading, letting multiple threads take turns
# Multiprocessing, using multiple processor cores to perform multiple processes
# Asynchronous IO, firing off a task and continuing to do another stuff, instead of waiting for an answer from the network or disk
# Multiple computers at the same time


# Python concurrency basics

# Difference between threads and processes

# A thread is an independent sequence of execution, but it shares memory with all the other
# threads belonging to your program. By default, Python only had one main thread. You can create
# more and switch between them. The switching happens so fast that it appears like they are running
# side by side at the same time

# A process is also an independent sequence of execution, but unlike threads, a process has its own
# memory space that is not shared with other processes. A process can clone itself, creating two or
# more instances. 
# Ex parent process -- child process 1
#                    L child process 2
# In the example the parent process has created two clones of itself. Now we have three processes in total
# working all at once

# Lastly, we have asynchronous IO, or asyncio for short. Asynchronous IO is not threading, nor multiprocessing.
# It is a single-threaded, single process paradigm. It's complicated...


# I/O bound vs CPU bound problems

# Most software is I/O bound and not CPU bound
# I/O bound software: sotware that is mostly waiting for input/output operations to finish, usually when
# fetching data from the network or from storage media

# CPU bound software: software that uses all CPU power to produce the needed results. It maxes out the CPU


# Taking the I/O bound and CPU bound now in consideration...


# Python concurrency with threads

# Unlike other languages, Python threads don't run at the same time. They take turns instead. The reason
# for this is a mechanism in Python called the Global Interpreter Lock (GIL). GIL ensures there is always
# one thread running, so threads can't interfere with each other.

# The takeaway is that threads make a big difference for I/O bound software but are useless for CPU bound
# software. Because while one thread is waiting for a reply from the network, other threads can continue
# running. If you make a lot of network requests, threads can make a tremendous difference. If your threads
# are doing heavy calculations instead, they are just waiting for their turn to continue. Threading would 
# only introduce more overhead: there's some administration involved in constantly switching between threads


# Python concurrency with asyncio

# Being a relatively new core library in Python. It solves the same problem as threading: it speeds up I/O 
# bound software, but it does so differently. The library has evolved a lot in the past years, so some code
# present in the web are outdated. More on this later...


# Python concurrency with multiprocessing

# If your software is CPU-bound, you can often rewrite your code in such a way that you can use more processors
# at the same time. This way you can linearly scale the execution speed. This type of concurrency is what we call
# parallelism, and you can use it in Python too, despite GIL

# Not all algorithms can be made to run in parallel. It is impossible to parallelize a recursive algorithm for example.
# But there's almost always an alternative algorithm that can work in parallel just fine.

# There are two ways of using more processors:

#   1. Using multiple processors and/or cores within the same machine. In Python, we can do so with the multiprocessing
#      library

#   2. Using a network of computers to use many processors, spread over multiple machines. We call this distributed 
#      computing.

# Python's multiprocessing library, unlike the Python threading library, bypasses the GIL. It does so by actually spawning
# multiple instances of Python. Instead, of threads taking turn within a single Python process, you now have multiple Python
# processes running multiple copies of your code at once.

# The multiprocessing library, in terms of usage, is very similar to the threading library. A question that might arise is:
# why should you even consider threading? Threading is "lighter": it requires less memory since it only requires one running
# Python interpreter. Spawning new process has its overhead as well. So if your code is I/O bound, threading is likely good
# enough and more efficient and lightweight


# Should I consider Python concurrency?

# Always take a good look at your code and algorithms first. Many speed and performance issues are resolved by implementing a
# better algorithm or adding caching. Some guidelines are:

#   1. Measure, don't guess. Measure which parts of your code take the most time to run. Focus on those parts first.

#   2. Implement caching. This can be a big optimization if you perfrom many repeated lookups from disk, network, and databases

#   3. Reuse objects instead of creating a new one on each iteration. Python has to clean up every object you created to free memory.
#      This is called garbage collection. The garbage collection of many unused objects can slow down your software considerably

#   4. Reduce the number of iterations in your code if possible, and reduce the number of operations inside iterations

#   5. Avoid (deep) recursions. It requires a lot of memory and housekeeping for the Python interpreter. Use things like generator and
#      iteration instead

#   6. Reduce memory usage. In generalm try to reduce the usage of memory. For example: parse a huge file line by line instead of loading it
#      in memory first.

#   7. Don't do it. Do you really need to perform that operation? Can it be done later? Or can it be done once, and can the result of it be
#      stored instead of calculated over and over again?

#   8. Use PyPy of Cython. You can also consider an alternative Python implementation. There are speedy Python variants out there.


# PyPy

# If you are sure your code is CPU bound, meaning it's doing lots of calculations, you should look into PyPy, an alternative to CPython. It's
# potentially a quick fix that doesn't require you to change a single line of code.

# PyPy claims that, on average, is 4.4 times faster than CPython. It does so by using a technique called just-in-time compulation (JIT). Java
# and the .NET framework are other notable examples of JIT compilation. In contrast, CPython uses interpretation to execute your code. Although
# this offers a lot of flexibility, it's very slow

# With JIT your code is compiled while running the program. It combines the speed advantage of ahead-of-time compilation (used by languages like C
# and C++) with the flexiobility of interpretation. Another advantage is that the JIT compiler can keep optimizing your code while it is running. The
# longer your code runs, the more optimized it will become

# PyPy works flawlessly with Pipenv, and can be used as a drop-in replacement to Python 2 and 3


# Cython

# Cython offers C-like performance with code that is written mostly in Python, but makes it possible to compile parts of your Python code to C code.
# This way, you cab convert crucial parts of an algorithm to C, which will generally offer a tremendous performance boost.

# It is a superset of the Python language, meaning it adds extras to the Python syntax. It's not a drop-in replacement like PyPy. It requires adaptations
# to your code and knowledge of the extras Cython adds to the language

# With Cython, it is also possible to take advantage of the C++ language because part of the C++ standard library is directly importable from Cython code.
# Cython is particularly popular among scientific users of Python. Some notes:

#   1. The SageMath computer algebra system depends on Cython, both for performance and to interface with other libraries

#   2. Significant parts of the libraries SciPy, pandas, scikit-learn are written in Cython

#   3. The XML toolkit, lxml, is written mostly in Cython


