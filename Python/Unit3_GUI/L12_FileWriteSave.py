from tkinter import*
from tkinter import filedialog


def saveFile():
    file = filedialog.asksaveasfile(
                                    initialdir="D:\\Learning File\\BCA\\BCA 1st Sem\\YT\\BroCode\\PythonGUI",    #change save path directory
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text file",".txt"),
                                        ("HTML file",".html"),
                                        ("All files",".*")
                                    ])
    if file is None:
        return
    filetext= str(text.get(1.0,END))
    # filetext = input("Enter Some Text Here:- ")
    
    file.write(filetext)
    file.close()




window = Tk()
button = Button(text='save', command=saveFile)

button.pack()
text=Text(window)

text.pack()
window.mainloop()
