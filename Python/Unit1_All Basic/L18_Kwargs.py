# ** Kwargs = Parameter that will pack all arguments into a dictionary useful so that a function can accept a varying amount of keywords arguments. 

def hello(**kwargs):
    # print("Hello" + kwargs['first']+ " "+ kwargs['last'])
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value,end=" ")

hello(title ="Mr", first= "Shailesh", middle= "", last= "Kr")