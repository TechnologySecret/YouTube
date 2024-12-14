from tkinter import*
from time import*

def update():
    time_String = strftime("%I:%M:%S %p")   # For MoreAbour strftime follow(https://docs.python.org/3.13/library/datetime.html#strftime-and-strptime-behavior)
    time_label.config(text=time_String)
    time_label.after(1000,update)
    
    
    date_String = strftime(" %d %B %Y")   # For MoreAbour strftime follow(https://docs.python.org/3.13/library/datetime.html#strftime-and-strptime-behavior)
    date_label.config(text=date_String)
    date_label.after(1000,update)

     






window  = Tk()

# Print Time Label

time_label = Label(window,
                   font=("Arial",40),
                   fg="green",
                   bg="black"
                   )

time_label.pack()

# Print Date Label

date_label = Label(window,
                   font=("Arial",40),
                   fg="yellow",
                   bg="green"
                   )

date_label.pack()

update()

window.mainloop()
