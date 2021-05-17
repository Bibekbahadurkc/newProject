from tiknter import *

root = Tk()
root.title('Dialog Box')
root.iconbitmap('E:/img.ico')

def show():
    myLevel = Label(root, text=var.get()).pack()

var = StringVar()

checkButton = Checkbutton(root, text="Check this box!", variable = var, onvalue="On", offvalue="Off")
checkButton.deselect()
checkButton.pack()

myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()