# Q. IN this program we write here code in details about file import from Drive and 
#       Read all content of this file

from tkinter import *
from tkinter import filedialog

def openFile():
    # filepath = filedialog.askopenfile 
    filepath = filedialog.askopenfilename(initialdir="D:\\Learning File\\BCA\\BCA 1st Sem\\PYTHON\\YT\\BroCode\\PythonGUI", 
                                      title="File Selct any one? ", 
                                      filetypes=(("text files","*.txt"), 
                                      ("openfile","*.*"))) 

                                                              
    # print(filepath)   #create a buttton for open filemanger
    file = open(filepath,'r')
    print(file.read())
    file.close()


window = Tk()
button = Button(text="Open", command=openFile)
button.pack()

window.mainloop()
