from tkinter import*
from tkinter import PhotoImage
import tkinter
# Create a function Click or Not 

def display():
    if(x.get()==1):
        print("You Agree!!")
    else:
        print("You don't agree : ")


window  = tkinter.Tk()

x= BooleanVar()

python_photo = PhotoImage(file ='.//image//blog.png')

check_button = Checkbutton(window, 
                            text=" I agree with You", 
                            variable=x,
                            onvalue=True,
                            offvalue=False,
                            command=display,
                            font=('Arial',30),
                            background="black",
                            fg="green",
                            activebackground="blue",
                            activeforeground="black",
                            padx=25,
                            pady=10,
                            image=python_photo,
                            compound='left'  #this is image move shift place

)

check_button.pack()
window.mainloop() 

