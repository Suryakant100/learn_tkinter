from tkinter import *

def selected():
    label.config(text="Fuel choice is: "+ fuel.get())


root = Tk()
root.geometry("300x400")

fuel = StringVar(value="Petrol")

radiobutton1 = Radiobutton(root,text="Petrol", variable=fuel, value="Petrol",command=selected)
radiobutton2 = Radiobutton(root, text="Diesel",variable=fuel, value="Diesel",command=selected)
radiobutton3 = Radiobutton(root, text="Electric",variable=fuel, value="Electric",command=selected)

radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()

label = Label(root)
label.pack()
root.mainloop()
