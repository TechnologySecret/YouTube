# Q1. Write a Program using graphic user interface where a button in python                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

from tkinter import PhotoImage
from tkinter import *


count = 0    # count how many time enter button


def click():
    global count
    count +=1
    print(count)       

    print("You Clicked the Button!!!")

window = Tk()

photo = PhotoImage(file ='.//image//java.png')

button  = Button(window,

                 text= "Click Me!!",
                 command=click,
                 font=("Comic Sans", 30),
                 fg= "yellow",
                 bg="black",
                 activeforeground="#00FF00",
                 activebackground="black",
                 state=ACTIVE,
                 image=photo,
                 compound="bottom"
                 )

button.pack()
  
window.mainloop()







