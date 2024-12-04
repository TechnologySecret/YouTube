# Conditions :  It is defined true and false.
# If = It is a block of code that will be execute if Condition is true.

# Q1. Write a progeam eligible for vote. 

'''
age = int(input("Enter Your Current Age:" ))
if age == 100:
    print ( "You are eligible for vote becuase ur century has done with current age :" + str(age))
elif  age >= 18 :
    print ( "You are eligible for vote because ur current age :" + str(age))
elif age <=18:  
    print ( "You are not eligible for vote because ur current age :" + str(age))
elif  age >= 100 :
    print ( "You are eligible for vote because ur current age above of 100 :" + str(age))

'''

# Q2. find ur age adults or not >>?

age = int(input("How old are you ?:"))

if age == 100: 
    print("You are a century old")
elif age >= 10:
    print("You are an adult")
elif age <= 0 :
    print("You haven't been born yet: ")
else: 
    print("You are a child")
    














