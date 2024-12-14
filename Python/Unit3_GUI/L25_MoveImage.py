# Q1. In this program write a program where Move images on a Canva

from tkinter import*
from tkinter import PhotoImage

def move_up(event):
    canvas.move(myimage, 0, -10)
def move_down(event):
    canvas.move(myimage, 0, 10)
def move_left(event):
    canvas.move(myimage, -10, 0)
def move_right(event):
    canvas.move(myimage, 10, 0)

window = Tk()

window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)

window.bind("<Up>",move_up)
window.bind("<Down>",move_down)
window.bind("<Left>",move_left)
window.bind("<Right>",move_right)


canvas = Canvas(window, width=1000, height=1000)
canvas.pack()

photoImage= PhotoImage(file= ".//image/car.png")

myimage= canvas.create_image(0,0, image=photoImage, anchor=NW)

window.mainloop()