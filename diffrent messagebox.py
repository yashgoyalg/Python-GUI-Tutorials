from tkinter import*
from tkinter import ttk
from tkinter import messagebox

root = Tk()

root.title("HELLO")
root.geometry("655x333")
def buttonwork():
    messagebox.showinfo("YASH G Tech Farm, you are not active in the group:")

def buttonwork1():
    messagebox.showinfo("send your ss in your group:")

def buttonwork2():
    messagebox.showerror("Error- 40452 Button not found")

#below code is for creating frame or background on blank window 
f1= Frame(root, bg="grey", borderwidth=6, pady=5, relief= SUNKEN)
f1.pack(side=LEFT, anchor= "nw")

#below code is only for creating buttons
b = Button(f1, fg="red", text="show info", command= buttonwork)
b.pack(side=LEFT)
b1 = Button(f1, fg="red", text="show notification", command=buttonwork1)
b1.pack(side=LEFT)
b2 = Button(f1, fg="red", text="error", command=buttonwork2)
b2.pack(side=LEFT)
b3 = Button(f1, fg="red", text="PLAY")
b3.pack(side=LEFT)
b4 = Button(f1, fg="red", text="account")
b4.pack(side=LEFT)
b5 = Button(f1, fg="red", text="SHARE")
b5.pack(side=LEFT)
b6 = Button(f1, fg="red", text="FA&Q")
b6.pack(side=LEFT)
b7 = Button(f1, fg="red", text="LOGIN")
b7.pack(side=LEFT)

root.mainloop()