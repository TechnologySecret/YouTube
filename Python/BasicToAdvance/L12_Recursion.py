# Recursion:-  When a function calls itself repeatedly
# Declaration:  prints n to 1 backwords
'''
def show(n):      #Write Your 1st line Work
    if ( n ==0):        # When codintion or N value == 0 then stop
        return          # It is control of function return
    print(n)        # print enter value 
    show(n-1)           # print  -1 value  
        # print("Some Message>> END")
show(5)         #call function
'''

# Example 1:- WAP where factorial of Number
'''
# FORMULA:  fact! = 1*2*3*4..... *(n-1) *n
EXAMPLE1 :  5! = 1*2*3*4*5
            4! =1*2*3*4
            3! =1*2*3
            2! =1*2
            1! =1
    OR      n! =(n-1)! * n  '''

# Step 1:  using simple one time of methods
def fact(n):
    if( n == 1 or n== 0):
        return 1 
    return fact(n-1) *n


print("Ans of Step2:",fact(4))

# ANSWER>>>>>OUTPUT: 24 ( how ?>> 1*2*3*4) 

# Step 2:  using Conditions 

def fact1(f):
    if( f == 0  or f == 1):
        return 1
    else :
        return f * fact1 (f-1)

print("Ans of Step2:",fact1(5))
# ANSWER>>>>>OUTPUT: 120 ( how ?>> 1*2*3*4*5) 

# Practice Questions
# Q1. Write a recursion to calculate the sum of first natural numbers
# Ans

def sumNatural(n):
    if ( n == 0):
        return 0
    else: 
        return sumNatural(n-1) + n

sum = sumNatural(10)
print("Sum of Natural Numbers:-",sum)

# Q2. Write a recursive function to print all elements in a list. 
# HINTS:- use list and index a parameters methods...............

def print_list( list, index=0):
    if (index == len(list)):
        return 
    print(list[index])
    print_list(list, index +1)

fruits = ["Mango","Papaya","Banana","Lichi","PineApple"]
print(fruits)


