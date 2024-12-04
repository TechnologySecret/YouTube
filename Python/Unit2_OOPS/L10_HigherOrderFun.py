# Higher Order Function = a function that either:
                        # 1. accepts a function as an argument or returns a function 
                        # 2. In python, function are also trated as objects
''' 
def loud(text): 
    return text.upper()

def quiet(text):
    return text.lower()

def Hello(func):
    text = func("Hello")
    print(text)

hello(loud)
hello(quiet)

'''


# Example 1: Find a program where dividend, divisor and quotient
# Example :  10/2= 5

def divisor(x):
    def dividend(y):
        return y/x 
    return dividend

divide = divisor(2)
print("Dividend Value is: ", divide(10))





