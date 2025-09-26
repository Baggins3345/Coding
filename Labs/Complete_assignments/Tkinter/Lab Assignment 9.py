from tkinter import*
root = Tk()

root.title("Lab 9 Program 1")
root.config(bg="grey")

label1 = Label(root,text="My first name is Benjamin.", bg="light sky blue", fg="blue", font="arial 30")
label1.pack()
label2 = Label(root,text="My last name is Strong.", bg="light sky blue", fg="blue", font="arial 30")
label2.pack()
label3 = Label(root,text="My faculty is IT.", bg="light sky blue", fg="blue", font="arial 30")
label3.pack()
label4 = Label(root,text="My year is Second.", bg="light sky blue", fg="blue", font="arial 30")
label4.pack()

root.mainloop()