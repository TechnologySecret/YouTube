# Duck Typing:  In this concept the class of an object is less important than the methods attributes,
#             class type is not checked if minimum methods/attributes are present, 
#             If it walks like a duck, and it quacks like a duck, then is must be a duck  

# Example 1 : I have to Class And Print When walks like a duck, and it quacks like a duck, then is must be a duck.. 

class Duck:
    def walk(self):
        print("This duck is walking")
    def talk(self):
        print("This duck is qwuaking")

class Chicken: 
    def walk(self):
        print("This Chicken is walking")

    def talk(self):
        print("This chicken is clucking")

class Person():
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You Caught the crutter")

duck = Duck ()
chicken = Chicken()
person = Person()
person.catch(chicken)



