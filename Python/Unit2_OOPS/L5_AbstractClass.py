# Prevent a user from creating an object of that class, comples a user to override abstract methods in a child class. 

# Abstract Class = A class which contains one or more abstract methods.  
# Abstract Methods= A method that has a declaration but does not have an implementation
# NOTE: --  an abstract class is a blueprint for other classes. 

# Step 1: Define an Abstract Class Formate:- 
# Step 1: Define an Abstract Class Format


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod    # Abstract Method
    def area(self):
        pass

    @abstractmethod    # Abstract Method
    def perimeter(self):
        pass

# Example of Methods class:
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Create Objects of Classes
rec = Rectangle(10, 5)
cir = Circle(7)

print("Rectangle Area:", rec.area())
print("Rectangle Perimeter:", rec.perimeter())

print("Circle Area:", cir.area())
print("Circle Perimeter:", cir.perimeter())
