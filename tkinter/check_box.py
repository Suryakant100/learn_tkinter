from tkinter import *

root = Tk()
root.geometry("300x400")

def selected():
    label.config(text=check_value.get())

check_value = BooleanVar()
checkBox = Checkbutton(root,text="Accept T&C",variable=check_value,command=selected)
checkBox.pack()

label = Label(root)
label.pack()
root.mainloop()
