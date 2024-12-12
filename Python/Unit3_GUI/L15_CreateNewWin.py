# Q1. Create a new window in Window using python. 

from tkinter import*

def create_window():
    new_window = Tk()  # Top level() :- is a new window on top of other windows linked in window
                            # Tk() :- new independent window
    
    old_window.destory()
old_window = Tk()

Button(old_window, text="create new window",command=create_window).pack()

old_window.mainloop()
