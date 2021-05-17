from tkinter import *

from tkinter import messagebox

root = Tk()
root.title('Message Box')
root.iconbitmap('E:\img.ico')

def popup():

    messagebox.showinfo("This is my Popup", "Hello world!")

Button(root, text="Popup",command=popup).pack()


root.mainloop()