from tkinter import*
root=Tk()
root.title("Canvas Line")

canvas1 = Canvas (root, width=400, height=400, bg="white")

canvas1.create_polygon(200,50,50,350,350,350, fill="blue", outline="red", width=10, activefill="green", activeoutline="cyan")

canvas1.pack()

root.mainloop()