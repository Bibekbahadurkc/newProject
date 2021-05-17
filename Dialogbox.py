from tiknter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title('Dialog Box')
root.iconbitmap('E:/img.ico')

def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="/Downloads", title="Select a a file", filetypes=(("png files", "*.png"), ("all files", "*.*")))

    my_label = Label(root, text=root.filename).pack()

    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()

my_btn = Button(root, text="Open File", command=open).pack()

mainloop()