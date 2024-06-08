from tkinter import *

root = Tk()

def text_respond():
    text_res = Label(root, text="button triggered!")
    text_res.pack()
    

button = Button(root, text="click me", padx=20, command=text_respond, fg="grey", bg="#445" )

button.pack()

root.mainloop()