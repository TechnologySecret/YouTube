# Q1. Write a Program in Python create a calcuator using graphic
from tkinter import*

equation_text = " "

def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_Label.set(equation_text)


def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_Label.set(total)
        equation_text = total
    except SyntaxError:
        equation_Label.set("Syntax Error!!! ")
        equation_text = ""
    except ZeroDivisionError:
        equation_Label.set("Arthemetic Error ")
        equation_text = ""
def clear():
    global equation_text
    equation_Label.set("")

    equation_text = ""

window = Tk()

window.title("Calculator Program")
window.geometry=("500x500")

equation_Label = StringVar()

label = Label(window,
              textvariable = equation_Label, 
              font=("consolas",39),
              bg="Yellow",
              width=20,
              height=2
              )
label.pack()

frame= Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=4, width=9, font=25,command=lambda:button_press(1))
button1.grid(row = 0, column=0)

button2 = Button(frame, text=2, height=4, width=9, font=25,command=lambda:button_press(2))
button2.grid(row = 0, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=25,command=lambda:button_press(3))
button3.grid(row = 0, column=2)

button4 = Button(frame, text=4, height=4, width=9, font=25,command=lambda:button_press(4))
button4.grid(row = 1, column=0)

button5 = Button(frame, text=5, height=4, width=9, font=25,command=lambda:button_press(5))
button5.grid(row = 1, column=1)

button6 = Button(frame, text=6, height=4, width=9, font=25,command=lambda:button_press(6))
button6.grid(row = 1, column=2)

button7 = Button(frame, text=7, height=4, width=9, font=25,command=lambda:button_press(7))
button7.grid(row = 2, column=0)

button8 = Button(frame, text=8, height=4, width=9, font=25,command=lambda:button_press(8))
button8.grid(row = 2, column=1)

button9 = Button(frame, text=9, height=4, width=9, font=25,command=lambda:button_press(9))
button9.grid(row = 2, column=2)

button0 = Button(frame, text=0, height=4, width=9, font=25,command=lambda:button_press(0))
button0.grid(row = 3, column=0)

plus = Button(frame, text='+', height=4, width=9, font=25,command=lambda:button_press('+'))
plus.grid(row = 0, column=3)

minus= Button(frame, text='-', height=4, width=9, font=25,command=lambda:button_press('-'))
minus.grid(row = 1, column=3)

multiply= Button(frame, text='*', height=4, width=9, font=25,command=lambda:button_press('*'))
multiply.grid(row = 2, column=3)

divide= Button(frame, text='/', height=4, width=9, font=25,command=lambda:button_press('/'))
divide.grid(row = 3, column=3)

decimal= Button(frame, text='.', height=4, width=9, font=25,command=lambda:button_press('.'))
decimal.grid(row = 3, column=1)

equal= Button(frame, text='=', height=4, width=9, font=25,command=equals)
equal.grid(row = 3, column=2)

clear= Button(window, text='clear', height=4, width=13, font=25,command=clear)
clear.pack()

window.mainloop()

