from tkinter import *
root = Tk()

ent = Entry(root, width=50, borderwidth=1, background="#fff")
ent.pack()

def acts():
    mylabel = Label(root, text=ent.get())
    mylabel.pack()

myButton = Button(root, text="Click", padx=50, command=acts)
myButton.pack()





root.mainloop() 