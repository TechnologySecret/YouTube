from tkinter import*


def doSomething(event):
    print("You did a thing:"+event.keysym)
    label.config(text = event.keysym)

    
window = Tk()

window.bind("<Key>",doSomething)
label = Label(window, font=("bold",80))
label.pack()

window.mainloop()
