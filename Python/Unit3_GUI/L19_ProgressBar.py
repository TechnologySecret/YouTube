# Create a Progress Bar in Python USing GUI in python

from tkinter import*
from tkinter.ttk import*
import time

'''
def start():
    tasks = 10   
    x=0
    while(x<tasks):
        time.sleep(1)
        bar['value']+=10
        x+=1
        percent.set(str(int((x/tasks)*100))+"%")
        text.set(str(x)+"/"+str(tasks)+" Task Completed!!")

        window.update_idletasks()


window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=10)

percentLabel = Label(window,textvariable=percent) .pack()
tastLabel = Label(window, textvariable=text).pack()

button = Button(window, text="Download", command=start).pack()

window.mainloop()

'''


# Q2. Let's get an example in real life. Download an Video Games of 100 GB how many speed per GB 


def start():
    GB = 100   
    download=0
    speed = 2
    while(download<GB):
        time.sleep(0.05)
        bar['value']+=(speed/GB)*100
        download+=speed
        percent.set(str(int((download/GB)*100))+ "%")
        text.set(str(download)+ "/" +str(GB)+"GB Completed!!")
        game.update_idletasks()


game= Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(game, orient=VERTICAL, length=300)     # Change Orient for Horizontal 
bar.pack(pady=10)

percentLabel = Label(game,textvariable=percent) .pack()
tastLabel = Label(game, textvariable=text).pack()

button = Button(game, text="Download", command=start).pack()

game.mainloop()

