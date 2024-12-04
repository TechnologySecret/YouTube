# Loop:  Iterative sentences: There are three types:  While, For and foreach Loop.
# Example 1. While Loop:  In this statements that will execute it block of code, as long as it conditions remains true. 

# Ex-1: 

print("While Loop")


# while 1==1 : 
#     print("Help Me!:  I'm stuck in the loop")


# Ex-2: 

# name = " " 
# # while not name :

# while len(name) == 0: 
#     name = str(input("Enter your name: "))
    
# print("Hello" +name)

# Ex-2 :  


# name = None 
# while not name :
#     name = input("Enter Your Name:  ")
#     print ("Hello" + name)


# 2.   for loop :--  a statements that will execute it's block of code a limited amount of times. 

# while loop  = unlimited 
# for loop = limited


print("For Loop")

# Example -1 :

# for i in range(10): 
    # print(i)   # 0 to 9
    # print(i+1)   # 1 to 10  
    
#  Example -2 : 

# # for i in range(50, 100) :  
# for i in range(50, 100+1, 2) : 
#     print(i) // skip 2 words 
#     # print(i+1)

# Example -3

# for j in "Tech Secret":
#     print(j)


# import time 
# for seconds in range(10, 0, -1): 
#     print(seconds)
#     time.sleep(1)

print("Happy New Year!")

print("Nested Loop")

# Nested Loop:  The "inner loop" will will finish all of its Iterations before finishing one iteration of the "outer loop"
# or: One loop inside the other loop 

# rows = int(input("How many rows: "))
# columns = int(input("How many columns: "))
# symbol = (input("Enter a symbol to use: "))

# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
#     print()

print("Loop Control Statements")
# Ans:  change a loop execution from a its normal sequence  

#break = used to terminate the loop entirely 
# Example-1 break statements:  

# while True :  
#     name = input ("Enter Your Name:  ")
#     if name != "":
#         break

# contione  statements: skip to the next iteration of the loop. 

# phone_number = "80649858965"

# for i in phone_number: 
#     if i =="-": 
#         continue 
#     print(i, end="")

#pass statements:  does nothing, acts as a placeholder 

for i in range(1,21): 
    if i == 12: 
        pass
    else: 
        print(i)








