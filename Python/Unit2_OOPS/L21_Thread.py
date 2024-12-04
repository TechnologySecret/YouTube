# Thread:- Threading in Python is a way to run multiple parts of a program concurrently (at the same time) in separate threads. 
#         :- A thread is a lightweight, smaller unit of a process. Python's threading module provides a way to work with threads.

# Key Features in Threading:- 
    # 1. I/O-Bound Tasks: Threading is particularly useful for tasks involving I/O operations (like file reading/writing, network requests).
    # 2. Concurrency: Threads enable multiple tasks to run concurrently within the same program.
    # 3. Lightweight: Threads share the same memory space, making them faster and less resource-intensive than creating multiple processes.

# How to works:  
#     . GIL(Global Interpreter Lock) allows only one thread to execute Python bytecode at a time. 
#     Hence, threading is most effective for I/O-bound tasks, not CPU-intensive ones.

#  Example:  

import threading
import time

'''
def print_num():
    for i in range(5):
        print(f"Thread: {i}")
        time.sleep(1)

# create thread
thread = threading.Thread(target=print_num)

# Start thread 
thread.start()

# Main thread continue 

for i in range(5,10):
    print(f"Main:{i}")
    time.sleep(1)

# wait for the thread to complete

thread.join()

# EXample of Some Methods of threading
# 1. Thread(target, args) >> Create a thread start line 
    # target: - Function to run in the thread
    # args: - Arguments for the functions.
# 2. start() :- starts the execution of the thread
# 3. join()  :- Waits for the thread to finish
# 4. is_alive()  :- Checks if the thread is still running or not
'''

# Example Threas with a class methods 

class MyThread(threading. Thread):
    def run(self):
        for i in range(5):   #Five time runs
            print(f"Running in {self.name}")
            time.sleep(1)

# Create and start threads 
thread1 = MyThread()
thread2 = MyThread()

thread1.start()
thread2.start()

thread1.join()
thread2.join()



# Example other  with synchronization

lock = threading.Lock()
shared_cou = 0

def increment():
    global shared_cou
    with lock:  # Lock ensures only one thread modifies `shared_counter` at a time
        for _ in range(100000):
            shared_cou += 1

thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f"Final counter value: {shared_cou}")






