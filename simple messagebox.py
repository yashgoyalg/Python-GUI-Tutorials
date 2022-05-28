from tkinter import*
from tkinter import ttk
from tkinter import messagebox

def buttonwork():
    messagebox.showinfo("Hello,'welcome to the YASH G Tech Farm :)")

root = Tk()
root.title("NOTIFICATION")

root.geometry("800x200")
root.resizable(False,False)
yash= ttk.Button(root, text="push", command=buttonwork)

yash.pack()
root.mainloop()