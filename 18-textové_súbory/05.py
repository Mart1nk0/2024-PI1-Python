import tkinter

canvas = tkinter.Canvas()
canvas.pack()

fbody = open("body.txt", "r")
for body in fbody:
    print (body)
    medzera = body


tkinter.mainloop()