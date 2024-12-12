# Q1. Write a program where enter a single line of code in input. 


from tkinter import*

# entry Widget = textbox that accepts a single line of user input

def submit():      #Sumit Button Function
    username=entry.get()
    print("Hello Mr "+ username)
   


def delete():        #Delete box all code on time
    entry.delete(0,END)


def backspace():  #BackSpace Button Delete Function Line by Line
    entry.delete(len(entry.get())-1,END)


window = Tk()   #Create Window Box


# Create Entry Buttom 

entry = Entry(window, 
              bg="green",
              fg="Yellow",
              font=("Bold Arial ", 55))



entry.pack(side=TOP)    # Entery Box create success but top, change like left, right, bottom

# Window Pre Desing In Empty Box 
#entry.insert(0,'Write Something')  #Pre Write Sentence in Box
entry.config(show="**")   #When You Create a Password box then it is visible only type
# entry.configure(state=DISABLED)



# Create Sumbit Button
submit_button = Button(window, text="submit", command=submit)
submit_button.pack(side="bottom")

# Create Delete Button
delete_button = Button(window, text="Delete", command=delete)
delete_button.pack(side="bottom")


#  Create BackSpace Button 
backspace_button = Button(window, text = "BackSpace", command=backspace)
backspace_button.pack(side="bottom")



window.mainloop()
