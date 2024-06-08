from  tkinter import *
from PIL import ImageTk, Image
from click import command

root = Tk()

root.title("Jayson - Gallery")
root.geometry("370x430")
# favicon
# root.iconbitmap("/home/favicon.ico")

my_img = ImageTk.PhotoImage(Image.open("./4.jpg").resize((370, 350), Image.ANTIALIAS) )

my_img2 = ImageTk.PhotoImage(Image.open('./11.jpg').resize((370, 350), Image.ANTIALIAS) )

my_img3 = ImageTk.PhotoImage(Image.open('./5.jpg').resize((370, 350), Image.ANTIALIAS) )

my_img4 = ImageTk.PhotoImage(Image.open('./3.jpg').resize((370, 350), Image.ANTIALIAS) )

my_img5 = ImageTk.PhotoImage(Image.open('./2.jpg').resize((370, 350), Image.ANTIALIAS) )

my_img6 = ImageTk.PhotoImage(Image.open('./1.jpg').resize((370, 350), Image.ANTIALIAS) )

image_list = [my_img, my_img2, my_img3, my_img4, my_img5, my_img6]

status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief= SUNKEN, pady=10, padx=10, anchor=W )

my_img = ImageTk.PhotoImage(Image.open('./4.jpg').resize((370, 350), Image.ANTIALIAS) )

my_label = Label(image=my_img)
my_label.grid(row=0, column=0, columnspan=3)

  

def back(image_number):
    global my_label
    global button_forward 
    global button_back
    my_label.grid_forget()
    my_label = Label(image = image_list[image_number -1] )
    button_forward = Button(root, text=">>", command=lambda:forward(image_number+1))
   
    button_back = Button(root,  text="<<", command=lambda: back(image_number-1)   )
    
    
    # print(image_number)
    if image_number == 0:
        button_back = Button(root, text=">>", state=DISABLED )
    
    button_forward.grid(row=1, column=1)
    button_back.grid(row=1, column=0)
    my_label.grid(row=0, column=0, columnspan=3)
    
    
    
def forward(image_number):
    global my_label
    global button_forward 
    global button_back
   
    my_label.grid_forget()
    my_label = Label(image = image_list[image_number -1] )
    button_forward = Button(root, text=">>", command=lambda:forward(image_number+1))
   
    button_back = Button(root,  text="<<", command=lambda: back(image_number-1)   )
    
    
    # print(image_number)
    if image_number == 6:
        button_forward = Button(root, text=">>", state=DISABLED )
    
    button_forward.grid(row=1, column=1)
    button_back.grid(row=1, column=0)
    my_label.grid(row=0, column=0, columnspan=3)

button_back = Button(root,  text="<<", command= lambda: back(5), state=DISABLED ) 
button_quit = Button(root, text="Exit program", command=root.quit)
button_forward = Button(root,  text=">>", command=lambda: forward(2))


button_forward.grid(row=1, column=1)
button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=2)
status.grid(row=2, column=0, columnspan=3, sticky=W+E )

# exit button



root.mainloop()