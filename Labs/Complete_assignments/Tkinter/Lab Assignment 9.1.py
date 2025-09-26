from tkinter import*
root=Tk()
root.title("Lab 9 Program 2")

canvas1 = Canvas(root, width=1000, height=700, bg="grey")
canvas1.create_rectangle(100,100,800,600, fill="SpringGreen4", width=5, outline="spring green")
canvas1.create_oval(400,150,550,400, fill="salmon", width=5, outline="red")
canvas1.create_polygon(600,150,600,400,750,250, fill="salmon", width=5, outline="red")
canvas1.create_polygon(350,150,350,400,200,250, fill="salmon", width=5, outline="red")
canvas1.create_polygon(350,430,250,550,450,550, fill="salmon", width=5, outline="red")
canvas1.create_polygon(600,430,750,550,480,550, fill="salmon", width=5, outline="red")
canvas1.pack()

root.mainloop()