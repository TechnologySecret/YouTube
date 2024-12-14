# Q1. In this post wr are discuss about details, 
# How to move 2D Image in Python help of Graphic 

from tkinter import*
import time 

WIDTH = 1620
HEIGHT = 900
xVelocity =3
yVelocity = 2

window = Tk()


canvas= Canvas(window,height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = PhotoImage(file='.//image//skyGrass.png')  #Background Image
background= canvas.create_image(0, 0, image =background_image, anchor= NW)

photo_image = PhotoImage(file='.//image//ball.png')     #front Image
my_image = canvas.create_image(0, 0, image=photo_image, anchor= NW)


# Create a Big Image 
image_width = photo_image.width()
image_height = photo_image.height()

while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    if(coordinates[0] >= (WIDTH-image_width) or coordinates[0] < 0):   #move right side and left
        xVelocity= -xVelocity   
        
    if(coordinates[1] >= (HEIGHT-image_height) or coordinates[1] < 0):   #move cuorsor up and down
        yVelocity= -yVelocity   
        
    canvas.move(my_image,xVelocity,yVelocity)
    # canvas.move(my_image,0, yVelocity)
    
    window.update()
    time.sleep(0.01)

window.mainloop()