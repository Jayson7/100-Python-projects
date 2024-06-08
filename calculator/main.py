from tkinter import * 
root = Tk()

root.title("Simple calculator - Jayson")
entry = Entry(root, width=30, borderwidth=7 )
entry.grid(row=0, column=0, columnspan=3, padx=20, pady=40)


def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, END)


def button_add():
    first_number = entry.get()
    global f_num
    global maths
    maths = 'addition'
    f_num = int(first_number)
    entry.delete(0, END)


def button_divide():
    first_number = entry.get()
    global f_num
    global maths
    maths = 'division'
    f_num = int(first_number)
    entry.delete(0, END)
    
def button_multiply():
    first_number = entry.get()
    global maths
    maths = 'multiplication' 
    global f_num
    f_num = int(first_number)
    entry.delete(0, END)
    

def button_subtract():
    first_number = entry.get()
    global f_num
    global maths
    maths = 'subtraction'
    f_num = int(first_number)
    entry.delete(0, END)
    
def button_equal():
    second_number = entry.get()
    entry.delete(0, END)
    if maths == 'addition':
        entry.insert(0, f_num + int(second_number))
   
    if maths == 'subtraction':
        entry.insert(0, f_num - int(second_number))
   
    if maths == 'multiplication':
        entry.insert(0, f_num * int(second_number))
   
    if maths == 'division':
        entry.insert(0, f_num / int(second_number))
   
   
# Author - Jayson

# all buttons needed

button_1 = Button(root, text="1", padx=25, pady=10, command=lambda: button_click(1) )
button_2 = Button(root, text="2", padx=25, pady=10, command=lambda: button_click(2) )
button_3 = Button(root, text="3", padx=25, pady=10, command=lambda: button_click(3) )
button_4 = Button(root, text="4", padx=25, pady=10, command=lambda: button_click(4) )
button_5 = Button(root, text="5", padx=25, pady=10, command=lambda: button_click(5) )
button_6 = Button(root, text="6", padx=25, pady=10, command=lambda: button_click(6) )
button_7 = Button(root, text="7", padx=25, pady=10, command=lambda: button_click(7) )
button_8 = Button(root, text="8", padx=25, pady=10, command=lambda: button_click(8) )
button_9 = Button(root, text="9", padx=25, pady=10, command=lambda: button_click(9) )
button_0 = Button(root, text="0", padx=25, pady=10, command=lambda: button_click(0) )
button_add = Button(root, text="+", padx=25, pady=20, command=button_add )
button_equal = Button(root, text="=", padx=66, pady=20, command=button_equal )
button_clear = Button(root, text="Clear", padx=56, pady=10, command=button_clear )
button_subtract = Button(root, text="-", padx=25, pady=20, command=button_subtract )
button_multiply = Button(root, text="x", padx=25, pady=20, command=button_multiply )
button_divide = Button(root, text="/", padx=30, pady=20, command=button_divide )

# activating button to the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=1)
button_8.grid(row=1, column=0)
button_9.grid(row=1, column=2)
# Author - Jayson
button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0, columnspan=1 )
button_equal.grid(row=5, column=1, columnspan=2 )
button_divide.grid(row=6, column=0, columnspan=1 )
button_subtract.grid(row=6, column=1, columnspan=1 )
button_multiply.grid(row=6, column=2, columnspan=1 )





# loop em up
root.mainloop()