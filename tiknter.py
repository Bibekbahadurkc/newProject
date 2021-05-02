from tkinter import *

root = Tk()

redbutton = Button(root, text = "Left", fg = "green")

redbutton.pack(side = LEFT)

greenbutton = Button(root, text = "RIGHT", fg ="black")
greenbutton.pack(side = RIGHT)

bluebutton = Button(root, text = "TOP", fg ="blue")
bluebutton.pack(side = TOP)

blackbutton = Button(root, text = "BOTTOM", fg ="red")
blackbutton.pack(side = BOTTOM)


root.mainloop()