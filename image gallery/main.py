from  tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title("Jayson - software developer")

# favicon
# root.iconbitmap("/home/favicon.ico")

my_img = ImageTk.PhotoImage(Image.open('./4.jpg').resize((750, 550), Image.ANTIALIAS) )

my_label = Label(image=my_img)
# print(dir(my_label))
my_label.pack()










# exit button
button_quit = Button(root, text="Exit program", command=root.quit)
button_quit.pack()




root.mainloop()
