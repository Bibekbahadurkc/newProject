from tiknter import *

root = Tk()
root.title('Dialog Box')
root.iconbitmap('E:/img.ico')

def show():
    myLevel = Label(root, text=clicked.get()).pack()

clicked = StringVar()
clicked.set("Monday")

drop = OptionMenu(root, clicked,"Monday","Tuesday","Wednesday","Thursday","Friday")
drop.pack()

myButton = Button(root, text="Show selection", command=show).pack()
root.mainloop()