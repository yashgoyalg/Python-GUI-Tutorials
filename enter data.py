from tkinter import*

root = Tk()
root.title("HELLO")
root.geometry("250x200")

#the below code is for writing somthging in the window as a label
Label(root, text="WINDOW RESIZER !!", font="comicsansms 11 bold").grid(row=0 , column=2)

#the below code is to create input window
width = Label(root, text="Width:")
height = Label(root, text="Height:")


width.grid(row=1, column=0)
height.grid(row=2, column=0)

#the below code is for geting value from user....

def setsize():
    print(width_value.get())
    print(height_value.get())
#below code is use to craete a canatiner
width_value = StringVar()
height_value = StringVar()

widthentry = Entry(root, textvariable= width_value)
heightentry = Entry(root, textvariable= height_value)

widthentry.grid(row=1, column=2)
heightentry.grid(row=2, column=2)

#below code is for creating frame or background on blank window 
button = Button(text="Apply",command=setsize , borderwidth=2,relief= SUNKEN, pady=0, font= "comicsansms 10 bold").grid(row=5, column= 2)

root.mainloop()