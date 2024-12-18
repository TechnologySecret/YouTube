# Q1. Covert Python file to Execution File 
#       .py to .exe 
# Following These Step:  #
#        windows defender may prevent you from running, 
# Note:   sure pip and pyinstaller are installed/updated

# cd to directory that contains your .py file

# pyinstaller .......
#     -F              (all in 1 file)
#     -w               (removes. terminal window)
#     -i icon.ico       (adds custome icon to .exe)    (seearch on google >> conver ico file and download then run .ico file )
#     clock.py           (name of your main python file)

# One line Command>>>> pyinstaller -F -w -i liveclock.ico L4_Py_to_Exe.py  
# Click on>> dict>> .exe    is avaible and enter is located in the dist folder

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




