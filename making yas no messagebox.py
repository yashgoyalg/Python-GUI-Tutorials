from tkinter import*
from tkinter import ttk
from tkinter import messagebox

def buttonwork():
    a = messagebox.askyesno("Are you sure you want to exit ?")
    if(a):
        root.destroy()

root = Tk()
root.title("NOTIFICATION")

root.geometry("800x200")
root.resizable(False,False)
yash= ttk.Button(root, text="exit", command=buttonwork)

yash.pack()
root.mainloop()