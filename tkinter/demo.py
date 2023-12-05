from tkinter import *

root = Tk()  # Main window creating using the Tk() class of tkinter library
root.geometry("300x400")  # Default size of wizard window will be 300x400px
# hello = Label(root,text="Hello World!",fg="red",bg="white",font=("Arial",26))  # Label widget which can display text and bitmaps.
# hello.pack()

entry = Entry(root)  # taking input from user with the help of the root window
entry.pack()

def display():
    data = entry.get()
    print(data)

butoon = Button(root,text="Click here",command=display)
butoon.pack()



root.mainloop()  # the created window will be in loop un till we don't stop manually
