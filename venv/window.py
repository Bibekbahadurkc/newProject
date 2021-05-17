from  tkinter import *
from PIL import  ImageTk, Image

root = Tk()
root.title('New Window')
root.iconbitmap('E:\img.ico')

def open():
    top = Toplevel()
    top.iconbitmap('E:\img.ico')

    btn2 = Button(top, text="Close Window", command = top.destroy).pack()

btn = Button(root, text="Open", command=open).pack()

root.mainloop()
