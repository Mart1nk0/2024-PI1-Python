import tkinter

def klik(event):
    canvas.create_line(100, 20, event.x, event.y)

canvas = tkinter.Canvas()
canvas.pack()
canvas.bind('<ButtonPress>', klik)

tkinter.mainloop()