# Q. HOw to create a list box in python using GUI .
# # ListBox: A listing of seletable test items within its own container 

from tkinter import*


window = Tk()   

def submit():

    food = []
    for index in listbox.curselection():
        food.insert(index,listbox.get(index))

    print("You Have ordered the selected:- ")

    for index in  food:
        print(index)


    # print(listbox.get(listbox.curselection()))

def add():

    listbox.insert(listbox.size(),entryBox.get())

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)

    # listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())
     




listbox = Listbox(window,
                bg="yellow",
                font=("Constantia",25),
                width= 12,
                selectmode=MULTIPLE
                
                
                )



listbox.pack()

listbox.insert(1,"pizza")
listbox.insert(2,"pasta")
listbox.insert(3,"bread")
listbox.insert(4,"soup")
listbox.insert(5,"salad")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()


submitButtton= Button(window,text="Submit",command=submit)
submitButtton.pack()


addButtton= Button(window,text="Add",command=add)
addButtton.pack()

deleteButtton= Button(window,text="Delete",command=delete)
deleteButtton.pack()


listbox.pack()
window.mainloop()