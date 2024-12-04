# 4. Inheritance :- It means when a class access property of parents class that is called Ineritance. 
'''    In Technical >  Inheritance provided mechanism that allowed a class to inherit property of another class. 
                   When extends another class it inherit all non-private members including fields and methods.
    Another Words: - Inheritance is a fundamental concept in object-oriented programming (OOP) that allows one class (child class) to inherit attributes and methods from another class (parent class).

There are five types of Inheritance :

    1.Single Inheritance 
    2.Multiple Inheritance 
    3.MultiLevel Inheritance
    4.Hirarchical Inheritance
    5.Hybrid Inheriatance
'''

# Single Inheriance: A Child Inherit from a Single parent class. 

'''
# Parent Class
class Vehicle:
    def start(self):
        print("Vehicle is starting...")

# Child Class
class Car(Vehicle):
    def drive(self):
        print("Car is driving...")

# Create an instance of Car
car = Car()
car.start()  # Inherited method from Vehicle
car.drive()  # Method from Car

'''

# 1. Single Inheritance > Example of Calculator, add, sub, mul.... 

'''
#Parent Class 
class Add:
    def add(seft):
        a = int(input("Enter a Value :"))
        b = int(input("Enter b Value :"))
        c=a+b

        print( f"Addition of Parent class : {c}" )

# Child Class
class sub(Add):  #sub inherit from Parent Class 
    def sub(self):
        a = int(input("Enter a Value :"))
        b = int(input("Enter b Value :"))
        c = a-b
        print(f"Subtraction of Child Class : {c}")

# Creating Object Class for Derived Class
obj = sub()
obj.add()  #calling the inherited method from the Parent Class
obj.sub()   #calling the method of the Derived Classs.
'''


# MultiPle Inheritance :-  In this type of inheritance Base class may be two or more than two but derived class should be one.
'''
class Add:   # 1st Parent Class
    def add(self):
        print("This is 1st Parent Class ")
        x=int(input("Enter X value:"))
        y=int(input("Enter Y value:"))
        z= x+y
        print("Value of Addition:",z)


class Sub:   #2nd Parent Class
    def sub(self):
        print("This is 2nd Parent Class ")
        x=int(input("Enter X value:"))
        y=int(input("Enter Y value:"))
        z= x-y
        print("Value of Substraction:",z)


class Mul(Sub,Add):   # Child class of 2nd and 1st 
    def mul(self):
        print("This is Child Class ")
        x=int(input("Enter X value:"))
        y=int(input("Enter Y value:"))
        z= x*y
        print("Value of Multiplication:",z)

# Create object for accessing all value/

obj = Mul()
obj.add()
obj.sub()
obj.mul()

'''

# 3.MultiLevel Inheritance:   In this Inheritance एक class दूसरी क्लास को extend करती है 
# और दूसरी class तीसरी class को extend करती है And so On...  चलते रहते है।

'''
class MultiL1():
    def simpleIntrest(self):         #Write a program to calculate simple interest.  
                                    #( Formula:- Simple Interest = (P × R × T)/100 )
        print("WAP Simple Intrest Value ")
        p=int(input("Enter Pricinpal Amount:"))
        t=int(input("Enter Time In Years:- "))
        r=int(input("Enter Rate of Amount:- "))

        si=(p*r*t)/100
        print("Total Value of Principal:-",si)

class MultiL2(MultiL1):         #2.Write a program to calculate area of circle   
                                #(Formula :- πr².)
    def areaCircle(self):
        print("\n WAP calculate area of circle ")
        raduis= int(input("Enter Value of Area:"))
        area= 3.14*raduis*raduis
        print("Your Area of Circle Value is :- ",area)

class MultiL3(MultiL2):           #Write a program to calculate volume of sphere or area of sphere
                                #( sphere is formula? :-  4/3 (π)r³ )
    def areaSphere(self):
        print("\n WAP area of sphere")
        r= int(input("Enter Spahere Raduis Value: -"))
        areaSphere= (4/3*3.14)*r*r*r
        print("Total Value of Spahere is ",areaSphere)

class MultiL4(MultiL3):         #Write a program to calculate area of triangle.  
                                #( Formula :-  (1/2)*b*h)
    def areaTriangle(self):
        print("\n WAP Area of Triangle")
        b= int(input("Enter Value of Base:-"))
        h= int(input("Enter Value of Base:-"))
        areatriangle = 1/2 *b*h

        print("Total Value of Base : ",areatriangle)


# Create object for accessing all value of MultiLevel Inheritance Program

object=MultiL4()

object.simpleIntrest()
object.areaCircle()
object.areaSphere()
object.areaTriangle()
'''

# HERARCHICAL INHERITANCE  : Multiple child classes inherit from a single parent class.
'''
class Parent():
    def compoundIntrest(self):                              #WAP Compund Intrsert find >>
        print("\n Enter Value for Compund Intreset")           # Compound Interest = Amount – Principal 
        p=int(input("Enter Pricipal Value:-"))        # Where   Amount, A = P(1+(r/n))nt
        t=int(input("Enter Time in Years:-  "))
        r=int(input("Enter Rate of Amount in Percent:- "))
        n=int(input("Enter Compound Quentry in Years/4: - "))

        # Calcualte SimpleIntreset Final Amount  >> A = P(1+(r/n))nt
        finalAmount = p*(1+(r/n))*n*t

        # Calcualte CompoundIntreset Final Amount >>  cmpInt= Amount – Principal 
        cmpInt  = finalAmount - p

        print("Total Value of Priciple is :- ",finalAmount)
        print("And Total Compound Intreset Amount Value: -",cmpInt)

class child1(Parent):
    def swapTwoNum(self):   #. Write a program to swap value of two variable. 
        print("\n Enter Value for Swap Number....")
        x=int(input("Enter 1st Number:-"))
        y=int(input("Enter 2nd Number:-"))
        print("Before Swap Both Number  x=",x,"y=",y)

# Swap Number Now
                            # x+y = swap
        swap = x+y    #  10+20 = 30
        y= swap-y       # 30-20 = 10
        x= swap-x       # 30-10 = 20

        print(" After Swap Both Number x=",x,"y=",y)


class child2(Parent):
    def calculator(self):
        print("\n Enter Value for Calculator Number....")
        a= int(input("Enter Value of a:- "))
        b= int(input("Enter Value of b:- "))

        c= a + b
        d= a - b
        e= a * b
        f= a / b
        g= a % b 

        print("Value Of Addition        : ",c)
        print("Value Of Substraction    : ",d)
        print("Value Of Multiplication  : ",e)
        print("Value Of Division        : ",f)
        print("Value Of Module          : ",g)


# Create a object of Hiracrichal INheritance Value 

object=child1()
object.compoundIntrest()       #parent Methods 
object.swapTwoNum()         #child 1 Functions

# Note: There are create two object for Hirarichical Inheritance Value 

object=child2()
object.calculator()             #child2 Methods
'''
##################### THIS IS CALLED  1 PARENT MUTILPLE CHILDRENS METHODS 

# Hybird Inheritance :- A combination of two or more types of inheritance.

class Parent():
    def celToFah(self):      #write a program to input temperature in Celcious and convert to Fahrenheit:- 
                                #Celcious to Fahrenheit conversion  ( Formula :- ºF = (ºC x 9 / 5) + 32)
        print("\nThis is Celcuis To Fahrenhit Program: ")
        cal= int(input("Enter Temprature in Celcuis:- "))
        fahrenhite= 9/5*cal+32
        print("Your Temparture Fahrenhit Value: ",fahrenhite)
        
class Child1(Parent):
    def FahToCel(self):     #write a program to input temperature in Fahrenheit and convert to Celcious (Formula :- T(°C) = (T(°F) - 32) × 5/9)
        print("\nThis is  Fahrenhit to Celcuis Program: ")
        fah= int(input("Enter Your Fahrenhite Value: - "))
        calcuis = 5/9*fah-32
        print("Your Celcuis Value is: ",calcuis)

import math 
class Child2(Parent):
    def quaraticEqucation(self): #Write a program to find root of quadratic equation ax²+bx+c=0  
        print("\nThis is Quadratic Equcations Program: ")
                                    # formula is:  x=-b±✓b²4ac/2a
                                    #Discriminant formula (D)= b²-4ac
                                    #Let's  see an example >>>  2x²+5x-3= 
# Step 1: Identify Coefficient Value of Example

        a=int(input("Enter value of a (2):-"))
        b=int(input("Enter value of b (5):- "))
        c=int(input("Enter value of c (-3):-"))
# Step 2: Calculate the discriminat value
        # D= b²-4ac  
        D=b**2 - 4*a*c 

# Step 3: Use the quadratic formula   x= -b±✓D/2a >> Now Use Conditions for  real roots finds.
        
# Two distinct real root equcation 
        if D>0:      #If D>0, it calculates two distinct real roots.
            x =(-b + math.sqrt(D)) / (2*a)
            x1=(-b - math.sqrt(D)) / (2*a)
            print("Root are real and distinct value of x=",x)
            print("Root are real and distinct value of x1=",x1)
        
        
# one repeated real root
        elif D==0:     #If D=0, it calculates one repeated real roo
            x3= -b/(2*a)
            print("Root are real repeated = ",x3)

# Two complex roots
        else:       #otherwise excute D<0 , it calculates two complex roots.
            real_part     = -b/(2*a)
            imaginary_part= math.sqrt(-D)/(2*a)
            print("This is total value of Quaratic Equcation value is x and x2 = ", real_part, imaginary_part)

class GrandChild(Child1,Child2):
    def evenOdd(self):         # 11. Write a program to input a number and check whether it is odd or even. :- 
        print("\nThis is Even and Number Program: ")
        num= int(input("Enter a Random Number:-"))
        if num % 2 ==0:
            print("This is a Even Number.")
        else:
            print("This is a odd Number . ")


# Create Object of Hirarichical Inheritance Program

object = GrandChild()
object.celToFah()
object.FahToCel()
object.quaraticEqucation()
object.evenOdd()







        

