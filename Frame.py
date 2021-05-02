from tkinter import *

root = Tk()


Frame = LableFrame(root, text="My Frame", padx=5, pady=5)
Frame.pack(padx=10,pady=10)

button1 = Button(Frame, text="click this")
button1.grid(row=0, column=0)
button2 = Button(Frame, text="Click me")
button2.grid(row=1,column=0)


root.mainloop()