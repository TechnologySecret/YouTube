from tkinter import*
from tkinter import colorchooser    #submodule

def click():


                                     # Example for Knowledge purpuse  
    # color = colorchooser.askcolor()
    # print(color)
    # colorHex = color[1]
    # print(colorHex)
    # # window.config(bg=colorHex)   #Change background color  Step1 
    # window.config(bg=color[1])   #Change background color  Step2 

    window.config(bg=colorchooser.askcolor()[1])   #change backgorund color one line of code 


window = Tk()

window.geometry("430x420")
button = Button(text='click me', command=click())


button.pack()
button.mainloop()
