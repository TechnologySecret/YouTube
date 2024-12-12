from tkinter import*
from tkinter import PhotoImage

# Step 1: All File Menu Functions Created

def openFile():
    print("File Opened Now")

def saveFile():
    print("File Saved Now")

def quitFile():
    print("File Exit Now")


# Step 2: All Exit Menu Functions Created

def cutMenu():
    print("This is Cut Menu File")

def copyMenu():
    print("This is Copy Menu File")

def pasteMenu():
    print("This is Paste Menu File")

def findMenu():
    print("This is Find Menu File")


window = Tk()


# Step 3: Add Images Every Menu

openImage = PhotoImage(file=".//image//open.png", width="200", height="100")
saveImage = PhotoImage(file=".//image//save.png", width="200", height="100")
exitImage = PhotoImage(file=".//image//exit.png", width="200", height="100")

menubar = Menu(window)
window.config(menu=menubar)

# Step 1 function file excuted here:-  

fileMenu = Menu(menubar,tearoff=0,font=("Bold",20)) 
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open",command=openFile, image=openImage, compound='left')
fileMenu.add_command(label="Save",command=saveFile, image=saveImage, compound='left')
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quitFile, image=exitImage, compound='left')


# Step 2 function Exit excuted here:-  

editMenu = Menu(menubar, tearoff=0,font=("Bold",20))
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=cutMenu)
editMenu.add_command(label="Copy", command=copyMenu)
editMenu.add_command(label="Paste", command=pasteMenu)
editMenu.add_command(label="Find", command=findMenu)



window.mainloop()