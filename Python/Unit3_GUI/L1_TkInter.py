# What is TkInter :- 
#         TkInter is Python's built-in-library for creating Graphical User Interfaces(GUI's).
#         It is Independent langauge so you don't need to install it separately. 
#         TkInter provided functions a simple way to create Windows, button, labels, text fields, and other GUI components for desktop applications.

# # Why Use TkInter? 
#    1. Easy to use:  Simple and beginner-friendly syntax. 
#    2. Platfrom Independent:  Works on Windows, MacOS and LInux also. 
#    3. Built-in-Library:- Comes pre-installed with Python, so no additional installation is required. `
#    4. Customizable :- Allows you to build and style various GUI components 

# When it use:  create simple GUI applications like calculators, text editors, or file managers.

# TkInter Basic Tools:-  
# 1. Widgets: - Components like Label, Button, Entry, Text , etc are used to create GUI elements. 
# 2. ManiLoop:- A loop that runs the applications, wating for user interaction(Eg:- Clicking a button)
# 3. Geometry Management : Determines how Widgets are arranged using methods like:- pack(), grid() or place()

# EXample-1:- 

'''
import tkinter as tk


root = tk.Tk()      #Create the main window
root.title("Simple Example of TkInter")
root.geometry("300x200")


label = tk.Label(root, text = "Hello, Tkinter !=", font =("Arial", 16))
label.pack(pady = 20)

def on_button_click():
    label.config(text="Button Clicked Me !!")

button = tk.Button(root, text="Click Me", command = on_button_click)

root.mainloop()  #Start the main event loop
'''


# Common Widgets in Tkinter
#             1. Label: Displays text or images.
#             2. Button: Creates clickable buttons.
#             3. Entry: Input field for single-line text.
#             4. Text: Input field for multi-line text.
#             5. Checkbutton: Checkboxes for boolean choices.
#             6. Radiobutton: Radio buttons for selecting one option from many.
#             7. Canvas: Used for drawing shapes and graphics.


# Example 2:  GUI with Multiple Widget
'''

import tkinter as tk
from tkinter import*

# Create the main Windows

root = tk.Tk()
root.title("Multiple Widgets Tools in GUI")
root.geometry("500x500")

# Label
label = tk.Label(root,text="Enter Your Name:- ")
label.pack(pady=10)

# Entry(input Filed)
entry = tk.Entry(root)
entry.pack(pady=6)


# Button
def greet():
    name= entry.get()
    result_label.config(text=f"Hello Mrs, {name} !!")

button = tk.Button(root,text="Greet",command=greet)
button.pack(pady=10)

# Result  Label
result_label = tk.Label(root,text="", font=("Arial", 14))
result_label.pack(pady=20)


# Image 
image = PhotoImage(file="blog.png")
root.iconphoto(True,image)

# Color
root.config(background="Yellow")


# Start the main Loop
root.mainloop()
'''

# Example 3 :- Change Icons of File  >

'''
from tkinter import *
from tkinter import PhotoImage

window = Tk()       #instantiate an instance of a window
window.geometry("430x400")  
window.title("Technology Secret first GUI Program")   

# Change Icons Image
img = PhotoImage(file ="blog.png")    #set icon of image 

# label = Label(window, image=img)
# label.pack()  # print full image on front page

window.config(background="Yellow")


window.iconphoto(True, img)

window.mainloop()  #place window on computer screen, listen for events
'''
# Example 4:  WAP Use label where hold image and text in a windows.

import tkinter as Tk
from tkinter import *
# from tkinter import PhotoImage


window = Tk()

img = PhotoImage(file="blog.png")

label = Label(window, 
            text="Hello World",
            font=('Arial',20,'bold'),
            fg='Yellow',
            bg='Blue',
            relief= RAISED, 
            # relief= SUNKEN, 
            bd= 10,
            padx= 50,
            pady= 50,
            image=img,
            compound='bottom'   #top, left, right

            )

label.pack()

# label.place(x = 500, y=500)
# window.iconphoto(True, img)

window.mainloop()


