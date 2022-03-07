from tkinter import *
import tkinter

def save():
    save.test = entry.get()
    print(save.test)
    
def open_window():
    window = Toplevel(root)
    window.title("calculated!")
    label = Label(window, text=f"your age is: " + save.test)
    label.pack(padx=10, pady=10)

root = Tk()
entry = Entry(root)
root.title("calculate your age!")
lbl = Label(root, text="input your age here!")
btn = Button(root, text="calculate age", command=lambda:[save(), open_window()])
lbl.pack(padx=10, pady=10)
entry.pack(padx=10, pady=10)
btn.pack(padx=10, pady=10)

root.mainloop()


