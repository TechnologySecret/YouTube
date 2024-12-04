# # lambda function:-   Function written in 1 line using lambda keywords
#                     accepts any number of arguments, but only has one expression. 
#                     (think of it as a shortcut) 
#                     (useful if needed for a short period of time, throw-away)
# lambda parameters:expression

# Step -1: 

def double(x):
        return x * 2    # Multiplication
print(double(5))

# Step 2
double = lambda x:x + 2  # Addition
print("\n", double(5))
# Step 2: ONE LINE OF CODE 

multiply = lambda x,y : x*y 
# print("\n",multiply(5 * 6))   TypeError: <lambda>() missing 1 required positional argument: 'y'
# So, Can't run this code

add = lambda x,y,z: x + y + z
# print("\n", add(5+10+15))
full_name = lambda first_name, last_name:  first_name + " "+ last_name
# print("\n", full_name("Please Enter Full Name"))

# But You can print this function

age_check = lambda age: True if age >=18 else False
print("\n","Your Current age is: age >=18 - ", age_check(25))
