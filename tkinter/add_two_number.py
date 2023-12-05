from tkinter import *

root = Tk()
root.geometry("300x400")

def add_two_number():
    n1=int(number1.get())
    n2=int(number2.get())
    # print(n1+n2)   # It will print the result in the console
    result = str(n1 + n2)
    answer.config(text="Sum is: " + result)  # It will print the result in the Windows wizzard using lable class of tkinter


number1 = Entry(root)
number2 = Entry(root)

number1.pack()
number2.pack()

button = Button(root,text="Add",command=add_two_number)
button.pack()

answer = Label(root)
answer.pack()


root.mainloop()
