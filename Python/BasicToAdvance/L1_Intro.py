# Hey Dear Welcome to Python basic to Advance Course: 
#     *In this Lecture we are discuss about simple and easy to learn basic of Python.
#     *Also discuss about, Some major popular Project in Python
#     *So Follow me and read all comments and learn basic to Advance Jounrney 

print("I love Python Language")


# 1.1 Variable : It is just like that a container where stored a data. 


first_name = "Shailesh"
last_name = "Jaiswal"
full_name = (first_name + " "+ last_name)
print("Hello! " + full_name)

# print(type(name))  >>> Now We are discuss about type operators.
age =21
age +=1
print("Your age is : "+ str(age))
print(type(age))

height = 250.5
print("Your Height is "+ str(height)+ "cm")
print(type(height))

human= True
print("Are you a human: "+ str(human))
print(type(human))

# Multiple assignment= allow us to assign Multiple Variable at the same time in one line of of code, like>>>>>
name  = "Bro"
age = 21 
attractive = True

name, age, attractive = "Bro", 21, True; 
print(name)
print(age)
print(attractive)

songebob =Patrick = sandy = squisqward = 30

print(songebob)
print(sandy)

# Example >> String Methods In Python
name = "shailesh jaiswal"
print(len(name))  #lenghth of code
print(name.find("a"))  #find of code
print(name.capitalize())  #Fast Letter Capital of code
print(name.upper())  # All Letter is Capital of code
print(name.lower())  #Fast Letter Small of code
print(name.isdigit())  #total digit of code
print(name.isalpha())  #find of code
print(name.count("o"))  #find o any space of this code
print(name.replace("ai","ol"))  #replace of code.
print(name*4)  #mutiple time print of code.



# Type Casting = Convert the data type of a value to another data type. 

x= 1   #int 
y= 2.0 #float 
z= "3"  #str

print(str(x))
print(int(y))
print(str(z*4))


# How to input function use in Python.

name = input("What is your name: ")  #by default use integer 
age = int(input("How old are You? :"))  #defined int only
height = float (input("How tall are You? :"))  #defined float only

print("Hello "+ name)
print("You are "+str(age)+ " Years old")
print("You are "+str(height)+ " cm tall")




age = 25  #Integer 
print(age)  # Output: 25


pi = 3.14   #Float 
print(pi)  # Output: 3.14

greeting = "Hello, Shailesh!"    #String 
print(greeting)  # Output: Hello, Shailesh!


is_logged_in = True    #Boolean 
print(is_logged_in)  # Output: True

fruits = ["apple", "banana", "cherry"]   #list 
print(fruits)  # Output: ['apple', 'banana', 'cherry']

coordinates = (10, 20, 30)   #tuples 
print(coordinates)  # Output: (10, 20, 30)


person = {"name": "Shailesh", "age": 25}    #dictionary 
print(person)  # Output: {'name': 'Shailesh', 'age': 25}

 
unique_numbers = {1, 2, 3, 2, 1}    #set 
print(unique_numbers)  # Output: {1, 2, 3}








