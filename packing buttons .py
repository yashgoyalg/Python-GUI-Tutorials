from tkinter import*

root = Tk()

root.title("HELLO")
root.geometry("655x333")

#below code is for creating frame or background on blank window 
f1= Frame(root, bg="grey", borderwidth=6, pady=5, relief= SUNKEN)
f1.pack(side=LEFT, anchor= "nw")

#below code is only for creating buttons
b = Button(f1, fg="red", text="EXIT")
b.pack(side=LEFT)
b1 = Button(f1, fg="red", text="HOME")
b1.pack(side=LEFT)
b2 = Button(f1, fg="red", text="ACCOUNT")
b2.pack(side=LEFT)
b3 = Button(f1, fg="red", text="PLAY")
b3.pack(side=LEFT)
b4 = Button(f1, fg="red", text="COINS")
b4.pack(side=LEFT)
b5 = Button(f1, fg="red", text="SHARE")
b5.pack(side=LEFT)
b6 = Button(f1, fg="red", text="FA&Q")
b6.pack(side=LEFT)
b7 = Button(f1, fg="red", text="LOGIN")
b7.pack(side=LEFT)

root.mainloop()