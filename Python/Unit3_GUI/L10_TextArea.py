# text widget  = function like a text area, you can enter multiple line of text

from tkinter import*

def submit():
    input = text.get("1.0",END)
    print(input)



window = Tk()

text = Text(window, 
            bg='light yellow',
            font= ("Int Free ",25),
            height= 8, 
            width= 20,
            padx= 20,
            pady=20,
            fg='purple'  

            ) 
text.pack()

button =Button(window, text ="Submit",command=submit)
button.pack()


window.mainloop()