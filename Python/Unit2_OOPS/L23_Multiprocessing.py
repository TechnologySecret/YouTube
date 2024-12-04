# Multiprocessing in Python: 
        # It is running task in parallel on diffrent cpu cores, bypasses GIL used for threading 
        # Multiplrocessing = better for cpu bound task (heavy cpu usage)
        # Multithreading = better for io bound tasks(waiting around)

from multiprocessing import Process,cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count +=1


# def main():

if __name__ == '__main__':

    print(cpu_count())

    a = Process(target=counter, args =(12500000000,))
    b = Process(target=counter, args =(12500000000,))
    c = Process(target=counter, args =(12500000000,))
    d = Process(target=counter, args =(12500000000,))
   
    a.start()  #start the process
    b.start()  #start the process
    c.start()  #start the process
    d.start()  #start the process

    a.join()   # wait for the process completed 
    b.join()   # wait for the process completed 
    c.join()   # wait for the process completed 
    d.join()   # wait for the process completed 

    print("finished in: -",time.perf_counter(),"seconds")


