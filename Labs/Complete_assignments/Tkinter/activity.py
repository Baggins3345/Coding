import tkinter as tk

parent = tk.Tk()
parent.config(bg="lightblue")

parent.title("Python tkinter Exercises")

label = tk.Label(parent, text="Hello World", font=("Arial Bold", 40), fg="white", bg="black")
label.pack()

def on_button_click():
    label.config(text="Button Clicked!")

button = tk.Button(parent, text="Click Me", font=("Helvetica", 14), fg="white", bg="red", command=on_button_click)
button.pack()

parent.mainloop()

parent.mainloop()