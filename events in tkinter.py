from tkinter import*


def yash(event):
    print(f"You Clicked on the button at {event.x}, {event.y}")
root= Tk()
root.title("Events in Tkinter")
root.geometry("644x334")

Widget= Button(root, text="click me ")
Widget.pack()

#events ke through hum apne program ko hansal kar sakte hai...

Widget.bind("<Button-1>", yash)      #yhe apke mouse ke bare mai batarha h ki, click karne pr apka mouse kha move kar rha h
Widget.bind("<Double-1>", quit)     #yhe duble click karne pr window band kar dega..
root.mainloop()