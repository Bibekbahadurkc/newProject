from tiknter import *
from PIL import ImageTk, Image

root = Tk()

root.title('Images Insertion')

root.iconbitmap('E:\img.ico')

my_image = ImageTk.PhotoImage(Image.open("E:\m.JPG"))
my_Label = Label(image=my_image)
my_Label.pack()

button_quit = Button(root, text="Exit", command=root.quit,width=20)
button_quit.pack()

root.mainloop()