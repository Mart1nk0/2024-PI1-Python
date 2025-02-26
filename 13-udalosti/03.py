import tkinter
canvas = tkinter.Canvas(width=5000, height=5000)
def klik(event):
    x , y = event.x , event.y
    canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill='red')

canvas = tkinter.Canvas()
canvas.pack()
canvas.bind('<ButtonPress>', klik)

tkinter.mainloop()