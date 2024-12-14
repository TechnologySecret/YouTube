# Q.1. How to Ceate Multiple Object In Python Using Python 

from tkinter import*
from L27_BallClass import*
import time

window  = Tk()

WIDGET = 500
HEIGHT = 500

canvas = Canvas(window, width=WIDGET, height=HEIGHT)
canvas.pack()

# MultiPly Ball Create

volley_Ball = Ball(canvas,0,0,100,1,1,"black")
tennis_Ball = Ball(canvas,0,0,50,4,2,"yellow")
basket_Ball = Ball(canvas,0,0,125,5,7,"orange")
cricket_Ball = Ball(canvas,0,0,75,5,4,"red")


while True:
    volley_Ball.move()
    tennis_Ball.move()
    basket_Ball.move()
    cricket_Ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()


