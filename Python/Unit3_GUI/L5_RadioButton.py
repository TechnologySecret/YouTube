# Q1. Write a program using Graphic USer Interface create a Radio Button with image in Python .

from tkinter import PhotoImage
from tkinter import *
food = ["pizza", "burger","hotdog"]

def order():
    if(x.get()==0):
        print("You Ordered Pizza!")
    elif(x.get()==1):
        print("You Order Burger!!")
    elif(x.get()==2):
        print("You Ordered a hotdog!!!")
    
    else:
        print("Pls Selecte any One??")

window = Tk()

# pizzaImage = PhotoImage(file ='pizza.png')
# burgerImage = PhotoImage(file ='burger.png')
# hotdogImage = PhotoImage(file ='hotdog.png')

# foodImage = [pizzaImage,burgerImage,hotdogImage]




x= IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window , 
                            text=food[index],   #text to radio button
                            variable=x,       #groups to radiobutton together if they are share this
                            value=index,      #assign each radiobutton a diffrent values 
                            padx= 25,        #adds padding on x-axis
                            font=("Impact",50),
                            # image= foodImage[index],     #adds image to radiobutton 
                            # command= 'LEFT',   #adds image & text left-side
                            indicatoron= 0,  #eleminate circle indicators
                            width=50,    #sets width of radio buttons
                            background="green",   #change background color
                            command=order       #set command for radiobutton to functions
                            
                            )
    
    radiobutton.pack(anchor=W)

radiobutton.pack()
window.mainloop()
