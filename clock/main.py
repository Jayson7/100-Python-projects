from tkinter import *
from tkinter.ttk import * 
from time import strftime 

# import datetime
# from datetime import datetime
root = Tk()
t = "Jayon's Python Clock"

root.title(t)
label = Label(root, font=("cursive", 120), background = "black", foreground="cyan")
label.pack(anchor="center")

def time(): 
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000, time)
time()
mainloop()
# >>>>jayson>>>>>>#
#Twitter: jay_b_jayon