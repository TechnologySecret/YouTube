# Return Statments=  Functions send Python value/object back to the caller. 
                    # These value/objects are known as the functions return value.

def multiply(number1,number2): 
    result=  number1 * number2 
    return result


# print(multiply(10, 20))

# another rules 

x = multiply(20, 3)
print(x)
# Sum Of Return Arguments: Parameter that will pack all arguments into a tuple useful so that a functions can accept a vaying amount of arguments . 

# Example: 

def add( num1, num2):
    sum = num1 + num2 
    return sum

print(add(1,2))



