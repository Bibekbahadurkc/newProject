from tkinter import *

root = Tk()

e1 = Entry(root, width = 50, fg = "blue", bg = "white", borderwidth = 5)
e1.pack()

def myClick():
    textoutput = "Hello" + e1.get()

    myLevel = Label(root, text=textoutput)

    myLevel.pack()

myButton = Button(root, text="Click Me!", command=myClick, fg="white", bg="gray")
myButton.pack()

root.mainloop()