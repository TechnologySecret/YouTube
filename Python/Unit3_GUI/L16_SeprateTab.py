# Q. How to create a seprate tab in new window.

from tkinter import*
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window)  #widget that manage a collection of window/displays. 


tab1= Frame(notebook) #new frame for tab 1
tab2= Frame(notebook) #new frame for tab 2

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")

notebook.pack(expand=True)    #expand = expand to fill any space not otherwise used. 
                            #fill = fill space on x and y axis


Label(tab1, text= "Hello, This is Tab 1 in Window", width= 50, height= 30).pack()
Label(tab2, text= "Hello, This is Tab 2 in Window", width= 50, height= 30).pack()

window.mainloop()
