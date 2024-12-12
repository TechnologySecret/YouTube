# frame  = a rectangular container to group and hold widgets

from tkinter import*

window  = Tk()

frame = Frame(window, 
              bg="yellow",
              bd=5,
              relief=SUNKEN)

frame.place(x=10, y=20)


button = Button(frame, text='W',font=("Consolas",25), width=3).pack(side=TOP)
button = Button(frame, text='A',font=("Consolas",25), width=3).pack(side=LEFT)
button = Button(frame, text='S',font=("Consolas",25), width=3).pack(side=LEFT)
button = Button(frame, text='D',font=("Consolas",25), width=3).pack(side=LEFT)

window.mainloop()

                