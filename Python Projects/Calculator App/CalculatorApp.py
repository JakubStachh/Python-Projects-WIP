from tkinter import *

def calculate():
    try:
        result.set(eval(entry.get()))
    except:
        result.set("Error")

root = Tk()
root.title("Calculator")
entry = Entry(root)
entry.pack()
result = StringVar()
Label(root, textvariable=result).pack()
Button(root, text="Calculate", command=calculate).pack()
root.mainloop()
