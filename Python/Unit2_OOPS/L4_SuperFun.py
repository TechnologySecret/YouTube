# Super() = Super Funtion  used to give access to the  methods of a parent class.
#         Return a temporary object a parent class when ussed. 

class Rectangle:        #Parent class 
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length * self.width 
    
class Cube(Rectangle):
    def __init__(self, length, width, heigth):
        super().__init__(length, width)
        self.height = heigth

    def volume(self):
        return self.length  * self.width * self.height
    
obj1 =Square( 3 , 3)
obj2= Cube(3, 3, 3 )

print(obj1.area())
print(obj2.volume())