# Daemon THreading: - A daemon thread is a thread that runs in the background and terminates automatically when the main thread (the program) exits. 
#                  Daemon threads are typically used for tasks like monitoring, logging, or background services 
# Non- Daemon Thread- This threads keep running even after the main program finishes.
# # EX- Background task , garbage collection, waiting for input, long running process 

# How to Set a Thread as Daemon: - Use thread.daemon = True before calling start()
# Example: - 

import threading
import time


def background_task():
    while True:
        print("Background task running... ")
        time.sleep(1)

def main_task():
    for i in range(5):
        print(f"Main task: {i}")
        time.sleep(1)

# Create daemon thread

daemon_thread = threading.Thread(target=background_task, daemon=True)
daemon_thread.start()

# Main Task call
main_task()

print("Main program exits, Daemon thread will stop.")



# Another EXample of count down


# def timer():
#     print()
#     print() 
#     count = 0
#     while True:
#         time.sleep(1)
#         count +=1
#         print("logged in for : ", count, "seconds")

# x = threading.Thread(target=timer, daemon= True)

# x.start()

# x.setDaemon(True)
# print(x.isDaemon())

# answer = input("Do you wish to exit? ")


# Note: Non- Daemon THread Can't use for but For long-running tasks, 
# consider using non-daemon threads to ensure completion.