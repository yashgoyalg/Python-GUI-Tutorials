import tkinter
from tkinter import*

root=Tk()
root.title("Digital Calculator")
root.geometry("370x400")
root.resizable(False,False)
root.configure(bg="#000")            #color code

equation = ""

def show(value):
    global equation
    equation+=value
    Label_result.configure(text=equation)

def clear():
    global equation
    equation = ""
    Label_result.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result= eval(equation)
        except:
            result= "ERROR"
            equation =""

    Label_result.config(text=result)

Label_result = Label(root,width=25, height=2,text="",font=("arial",30))
Label_result.pack()

Button(root, text="C", width=5, height=1, font=("arial",18,"bold"), bd=2, fg="#fff", bg="#3697f5", command=lambda: clear()).place(x=6,y=100)
Button(root, text="/", width=5, height=1, font=("arial",18,"bold"), bd=2, fg="#fff", bg="#2a2d36",command=lambda: show("/")).place(x=96,y=100)
Button(root, text="%", width=5, height=1, font=("arial",18,"bold"), bd=2, fg="#fff", bg="#2a2d36",command=lambda: show("%")).place(x=186,y=100)
Button(root, text="*", width=5, height=1, font=("arial",18,"bold"), bd=2, fg="#fff", bg="#2a2d36",command=lambda: show("*")).place(x=276,y=100)


Button(root, text="7", width=5, height=1, font=("arial",18,"bold"), bd=2, fg="#fff", bg="#2a2d36",command=lambda: show("7")).place(x=6,y=160)
Button(root, text="8", width=5, height=1, font=("arial",18,"bold"), bd=2, fg="#fff", bg="#2a2d36",command=lambda: show("8")).place(x=96,y=160)
Button(root, text="9", width=5, height=1, font=("arial",18,"bold"), bd=2, fg="#fff", bg="#2a2d36",command=lambda: show("9")).place(x=186,y=160)
Button(root, text="-", width=5, height=1, font=("arial",18,"bold"), bd=2, fg="#fff", bg="#2a2d36",command=lambda: show("-")).place(x=276,y=160)


Button(root, text="4", width=5, height=1, font=("arial",18,"bold"), bd=2, fg="#fff", bg="#2a2d36",command=lambda: show("4")).place(x=6,y=220)
Button(root, text="5", width=5, height=1, font=("arial",18,"bold"), bd=2, fg="#fff", bg="#2a2d36",command=lambda: show("5")).place(x=96,y=220)
Button(root, text="6", width=5, height=1, font=("arial",18,"bold"), bd=2, fg="#fff", bg="#2a2d36",command=lambda: show("6")).place(x=186,y=220)
Button(root, text="+", width=5, height=1, font=("arial",18,"bold"), bd=2, fg="#fff", bg="#2a2d36",command=lambda: show("+")).place(x=276,y=220)


Button(root, text="1", width=5, height=1, font=("arial",18,"bold"), bd=2, fg="#fff", bg="#2a2d36",command=lambda: show("1")).place(x=6,y=280)
Button(root, text="2", width=5, height=1, font=("arial",18,"bold"), bd=2, fg="#fff", bg="#2a2d36",command=lambda: show("2")).place(x=96,y=280)
Button(root, text="3", width=5, height=1, font=("arial",18,"bold"), bd=2, fg="#fff", bg="#2a2d36",command=lambda: show("3")).place(x=186,y=280)
Button(root, text="0", width=11, height=1, font=("arial",18,"bold"), bd=2, fg="#fff", bg="#2a2d36",command=lambda: show("0")).place(x=6,y=340)


Button(root, text=".", width=5, height=1, font=("arial",18,"bold"), bd=2, fg="#fff", bg="#2a2d36",command=lambda: show(".")).place(x=186,y=340)
Button(root, text="=", width=5, height=3, font=("arial",18,"bold"), bd=2, fg="#fff", bg="#2a2d36",command=lambda: calculate()).place(x=276,y=280)


root.mainloop()
