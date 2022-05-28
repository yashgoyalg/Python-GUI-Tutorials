from tkinter import*

root = Tk()

root.title("HELLO")
root.geometry("655x333")
f1= Frame(root, bg="grey", borderwidth=6, pady=122, relief= SUNKEN)
f1.pack(side=LEFT, fill="y")
f2= Frame(root, bg="grey", borderwidth=8, padx=40, pady=50, relief= SUNKEN)
f2.pack(side=TOP, fill="x")
l  = Label(f1, text="Project")
l.pack()
l  = Label(f2, text="Welcome in python tutorial", font="helvetica 16 bold", fg="red")
l.pack()
root.mainloop()