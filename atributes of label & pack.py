from tkinter import*
root = Tk()

root.geometry("500x400")
root.title("My GUI with Harry")

root_label = Label(text='''Microprocessor 8085 Test 2 (24th June, 2021)

1)	A microprocessor is the heart of the microcomputer. 
a) Receiving input b) Performing computations. c) Storing data & instructions d) All of the above.
Ans:d)All of the above
2)	A device, which enables a microcomputer to perform the first of the above-mentioned tasks is known as the input device.
a) Keyboard b) Mousec) Toggled) All of the above.
Ans:d)All of the above
3)	The task of displaying the result computed by the microprocessor is performed by an output device, some of the commonly used output device.
a) Cathode Ray Tube(CRT)b) Light-Emitting diodes(LED’S)c) Laser printerd) All of the above.
Ans:d)All of the above
4)	n instruction essentially consists of an
a) Operation codeb) Address of the data c) Instruction operates d) None of the above.
Ans:a)Operating code
5)	The 8085A has interrupt pins:- a) TRAP, RST7.5 b) RST6.5, RST5.5 c) TNTR(pin 10)
d) All of the above.
Ans:d)All of the above
''', bg= "red", fg= "white", padx=100, pady=20, font=("comicsansms",12 , "bold"), borderwidth= 3, relief= SUNKEN)


# Important pack option 
# anchor = nw       (nw matlab north west)
# side = Toplevel, BOTTOM, LEFT,RIGHT

root_label.pack(side=TOP ,anchor="nw", fill=X)
root.mainloop()