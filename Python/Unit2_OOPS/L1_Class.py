# Hey, Coder Welcome Back to the> Object Oritiented Programming Language in Python. 

# OOP (Object-Oriented Programming) in Python is a programming paradigm that structures code by bundling data and functionality into objects. 
# It allows developers to model real-world entities and their interactions, making code more modular, reusable, and easier to maintain.

# Key Features in Python : - 
    # 1. CLass :- Class: A blueprint for creating objects. It defines a set of attributes (data) and methods (functions) that the objects created from the class will have.
    # 2. Object :-  Class: A blueprint for creating objects. It defines a set of attributes (data) and methods (functions) that the objects created from the class will have.

    # 3. Encapsulation:- 
    # 5. Polymorphism: -
    # 6. Abstraction: - 

# Advantages of OOP in Python:
# Modularity: Code can be divided into self-contained modules.
# Reusability: Code can be reused through inheritance.
# Scalability: Easier to manage and extend for larger applications.
# Maintainability: Encapsulation helps keep code organized.


# Formate of class:

# class create 
# class Person: 
#     def __init__(self, name, age ):
#         self.name = name
#         self.age = age 

#     def greet(self):
#         print(f"Hello, My Name is {self.name}")

# # object create
# p1=Person("Shailesh ", 23)
# p1.greet()


# Example of Big class: 
'''

class Car:  
    def __init__(self, make , model , year , color):
        self.make = make 
        self.model = model 
        self.year = year
        self.color = color
    
    def drive (self):
        print("This is "+self.model+" Driving")

    def stop (self):
        print("This is "+self.model+" Stopped")

# from car import filename>> if you create a file another file 

car_1 = Car ("Chevy","Corvette","2021","Yello") 
car_2 = Car ("Ford","Mustang","2021","Blue") 

print ("Car 1 Details: -----")
print(car_1.model);
print(car_1.make);
print(car_1.year);
print(car_1.color);

car_2.drive()
car_2.stop()

print ("\nCar 2 Details: -----")

print(car_2.make);
print(car_2.model);
print(car_2.year);
print(car_2.color);

car_2.drive()
car_2.stop()

'''

# Q1.Diffrence between Instance variable and class variables.

class Car: 
    wheels = 4  # this is example of classs variables 

    def __init__(self,make, model, year,color):
        self.make =   make #instance variables
        self.model =   model #instance variables
        self.year =    year #instance variables
        self.color =   color #instance variables

car_1 = Car ("Thar","Corvetee", "2024","Black")
car_2 = Car ("Zakwarg","Mustang","2025","White")

Car.wheels = 4

print(car_1.wheels)
print(car_1.wheels)



