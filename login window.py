'''simple login page with tkinter module '''

from tkinter import*

root = Tk()
root.title("HELLO")
root.geometry("655x333")

Label(root, text="Login", font="camberia 13 bold underline").grid(row=0, column=3)

user = Label(root, text= "Username")
passward = Label(root, text= "Passward")

user.grid(row=1, column=0)
passward.grid(row=2, column=0)  #.pack() bhi use kar sakte h

def go():
    print(uservalue.get())
    print(passvalue.get())              
    #print statment nhi likhna chahte tu pass kar sakte hai, print statment is use to get value from user 

# varible classes in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable= uservalue)
passentry = Entry(root, textvariable= passvalue)

userentry.grid(row=1, column=2)
passentry.grid(row=2, column=2)

Button(text="Submit", command= go).grid(row=5 ,column=2)

#checkbox 

techservises = Checkbutton(text="Do you agree with our T&C")
techservises.grid(row=4, column=2)
root.mainloop()