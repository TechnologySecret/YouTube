import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk()

# Adjust the path as needed
img = PhotoImage(file="hot.png")

label = tk.Label(root, 
                 image=img)
label.pack()

root.mainloop()
