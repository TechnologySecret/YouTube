# #  Args = Parameter that will pack all arguments into a tuple. 
#         It is so useful that a function can accept a varying amount of arguments

# An Example : Sum of two numbers without error

# def add( num1, num2):
#     sum = num1 + num2
#     return sum
# print(add(1,2))


# An Example : Sum of two numbers with error

# print(add(1,2,3))  # add() function only takes 2 positional arguments but we are given 3 argument so not execute. 


# How to find this error let's see :  use *astricks symbolls. 
'''
def add(*stuff ):
    sum =0 
    stuff = list(stuff)
    stuff[0] = 0
    for i in stuff:
        sum +=i
    return sum
print(add(1,2,3,4,5,7))
'''

# Q1. Sum of fast natural number using args(*strick symbolls)

def sum(*natural):
    add=0
    for i in natural:
        add += i
    return add
print(sum(1,2,3,4,5,6,7,8,9,10))


