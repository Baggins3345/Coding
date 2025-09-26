from tkinter import*


def f1():
    gallons = float(E1.get())
    quarts = gallons * 4
    L3.config(text=f"Quarts = {int(quarts)}")
def f2():
    gallons = float(E1.get())
    pints = gallons * 8
    L3.config(text=f"Pints = {int(pints)}")
def f3():
    gallons = float(E1.get())
    liters = gallons * 3.785
    L3.config(text=f"Liters = {liters:.3f}")

root = Tk()
root.title("Test")
root.minsize(400,300)
root.config(bg="lightgrey")

L1 = Label(text="Gallons:",bg="lightgrey", font="Arial 10")
L1.place(x=10, y=10)
L2 = Label(text="Choose:", bg="lightgrey", font="Arial 10")
L2.place(x=10,y=50)
L3 = Label(text="Results = ",bg="lightgrey", font="Arial 10")
L3.place(x=10, y=130)

E1 = Entry(font="Arial 10")
E1.place(x=90,y=10)

B1 = Button(text="Quarts", bg="lightgrey", font="Arial 10", activebackground="lightgrey", command=f1)
B1.place(x=10, y=80)
B2 = Button(text="Pints", bg="lightgrey", font="Arial 10", activebackground="lightgrey", command=f2)
B2.place(x=90, y=80)
B3 = Button(text="Liters", bg="lightgrey", font="Arial 10", activebackground="lightgrey", command=f3)
B3.place(x=160, y=80)



root.mainloop()


