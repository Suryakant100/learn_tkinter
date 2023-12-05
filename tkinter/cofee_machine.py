from tkinter import *

root = Tk()
root.geometry("300x400")

def selected():
    suger = suger_var.get()
    ice = ice_var.get()
    cream = cream_var.get()

    # print(suger, ice,cream)

    if suger:
        suger = "Suger"
    else:
        suger="No suger"

    if ice:
        ice = "Ice"
    else:
        ice="No ice"

    if cream:
        cream = "cream"
    else:
        cream="No cream"
    lablel.config(text="Options selected are: "+ "\n" +  suger + "\n" + ice + "\n" + cream)

suger_var=BooleanVar()
ice_var=BooleanVar()
cream_var=BooleanVar()

suger_checkbox = Checkbutton(root,text="Suger",variable=suger_var,command=selected)
ice_checkbox = Checkbutton(root,text="Ice",variable=ice_var,command=selected)
cream_checkbox = Checkbutton(root,text="Cream",variable=cream_var,command=selected)

lablel = Label(root)

suger_checkbox.pack()
ice_checkbox.pack()
cream_checkbox.pack()

lablel.pack()
root.mainloop()
