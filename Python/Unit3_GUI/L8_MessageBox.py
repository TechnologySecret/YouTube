# Q. Write a some message in python gui for bignners to advance level 
from tkinter import *
from tkinter import messagebox   #import messagebox library 

window = Tk()

def click():
    
    # print("Example 1:")
    # # Add code to be executed when the button is clicked
    # messagebox.showinfo("Button Clicked", "You clicked the button!")

    # messagebox.showinfo(title='This is an info message box', message="You are a person !!!!")
    # print("Example 2:")
    # while(True):   // Don't  use this loop with message one time just for leatning purpose, I am share with you.
        # messagebox.showwarning(title='WARRING', message='You have A VIRUS')
    # messagebox.showerror(title='Error!!', message="Something went wrong !!")
    
    # print("Example 3:")
    # if messagebox.askokcancel(title='ask ok cancel', message="Do you want to do the thing"):
    #     print("You did a thing!!")
    # else:
    #     print('You canceled a thing !!')
    
    # print("Example 4:")
    # if messagebox.askretrycancel(title='ask ok cancel', message="Do you want to do the thing"):
    #     print("You did a thing!!")
    # else:
    #     print('You canceled a thing !!')

    # print("Example 5:")
    # if messagebox.askyesno(title='ask yes or no', message='Do You like Cake'):
    #     print("Yes, I like ")
    # else:
    #     print("I don't like Cake ")

    # print("Example 6:")
    # print("Example 6:")
    # answer= messagebox.askquestion(title='ask questions', message="Do you like Pie? ")
    # if (answer == 'yes'):
    #     print('I like pie too :')
    # else:
    #     print("Why do you not like pie")

    print("Example 7:")
    answer = messagebox.askyesnocancel(title='Yes no cancel',message='Do you like to code',icon = 'warning')   # Icon (messagebox, error etc. )
    if(answer == True):
        print("You like to code:")
    elif(answer == False):
        print("Then why are you watching a coding video, oh! for Funny")
    else:
        print("You have dodged the questions")


button = Button(window,
                command=click,
                text='Click Me', 
                )
button.pack()

window.mainloop()
