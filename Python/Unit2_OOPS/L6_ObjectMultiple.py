# Q1. In this program we are discuss here some important. 
# concept create a object of python multiple times. 


class Car: 
    color = None

class Motorcycle:
    color = None

def change_color (vehicle,color):
    vehicle.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle()

change_color(car_1,"blue")
change_color(car_2,"White")
change_color(car_3,"Yellow")
change_color(bike_1,"black")


print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)
