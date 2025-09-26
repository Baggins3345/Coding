import tkinter as tk

parent = tk.Tk()

parent.title("User Registration Form")

label1 = tk.Label(parent, text = "Name:", font = ("Arial Bold ", 15 ), width = 20)
label2 = tk.Label(parent, text = "Phone Number", font = ("Arial Bold ", 15), width =20)
label3 = tk.Label(parent, text = "Address:", font = ("Arial Bold ", 15 ), width = 20)
label4 = tk.Label(parent, text = "City:", font = ("Arial Bold ", 15 ), width = 20)
label5= tk.Label(parent, text = "Province:", font = ("Arial Bold ", 15 ), width = 20)
label6= tk.Label(parent, text = "Country:", font = ("Arial Bold ", 15 ), width = 20)

entry1 = tk.Entry(fg= "black", bg= "white", width = 50, bd = 5)
entry2 = tk.Entry(fg= "black", bg= "white", width = 50, bd = 5)
entry3 = tk.Entry(fg= "black", bg= "white", width = 50, bd = 5)
entry4 = tk.Entry(fg= "black", bg= "white", width = 50, bd = 5)
entry5 = tk.Entry(fg= "black", bg= "white", width = 50, bd = 5)
entry6 = tk.Entry(fg= "black", bg= "white", width = 50, bd = 5)

label1.grid(row = 0, column = 0)
entry1.grid(row = 0, column = 1)
label2.grid(row = 1, column = 0)
entry2.grid(row = 1, column = 1)
label3.grid(row = 2, column = 0)
entry3.grid(row = 2, column = 1)
label4.grid(row = 3, column = 0)
entry4.grid(row = 3, column = 1)
label5.grid(row = 4, column = 0)
entry5.grid(row = 4, column = 1)
label6.grid(row = 5, column = 0)
entry6.grid(row = 5, column = 1)

def on_button_click():
    button.config(text = "Submitted")

button =tk.Button(parent, text = "Click Me", font = ("Helvetica", 14), fg = "white", bg = "red", command = on_button_click)
button.grid(row = 6, column = 1)

parent.mainloop()

parent.mainloop()