from tkinter import *

# initialize tk
root = Tk()

# a simple hello world message 
my_label = Label(root, text="Hello world jayson")
my_label2 = Label(root, text="Hello world jayson 2")

# send the label to the tk
# my_label.pack()

# positioning 

my_label.grid(row=1, column=1)
my_label2.grid(row=0, column=0)


# intiate the loop
root.mainloop() 