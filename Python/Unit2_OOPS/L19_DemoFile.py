

# This is demo file of 19_IfMainFile.py 
# #  
# def greet():
#     print("Hello from 19_DemoFile ")

# if __name__ =="__main__":
#     print("DemoFile 19 is running on directly right now.")
#     greet()
# else:
#     print("DemoFile 19 is imported into another module")


# Let's see an example of details in python where create an calculator

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a, b):
    return a *  b

def divide(a, b):
    if b != 0:
        return a/b
    else:
        return "Divided by zero is not allowed."

# Main logic for testing the functions

if __name__ == "__main__":
    print("Running math_operations directly")
    x,y = 10,5

    print(f"Addition: {x} + {y}= {add(x,y)}")
    print(f"Substraction: {x} - {y}= {subtract(x,y)}")
    print(f"Multiplication: {x} * {y}= {multiply(x,y)}")
    print(f"Division: {x} + {y}= {add(x,y)}")

 