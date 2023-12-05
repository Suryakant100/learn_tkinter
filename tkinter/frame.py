from tkinter import *

root = Tk()
root.geometry("300x400")

frame = Frame(root,highlightthickness=10,highlightbackground="black",padx="15",pady="15")
frame.pack()

frame1 = Frame(root)
frame1.pack(side=BOTTOM)

button = Button(frame,text="Button1")
button1 = Button(frame1,text="Button2")
button.pack()
button1.pack(side=BOTTOM)

root.mainloop()
