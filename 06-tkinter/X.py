import tkinter
canvas = tkinter.Canvas(width=320 ,height=320)
canvas.pack()

canvas.create_rectangle(10,10,20,20,fill="black")
canvas.create_rectangle(10,20,20,30,fill="black")
canvas.create_rectangle(20,30,30,40,fill="black")
canvas.create_rectangle(30,40,40,50,fill="black")
canvas.create_rectangle(40,30,50,40,fill="black")
canvas.create_rectangle(50,20,60,30,fill="black")
canvas.create_rectangle(50,10,60,20,fill="black")
canvas.create_rectangle(20,50,30,60,fill="black")
canvas.create_rectangle(10,60,20,70,fill="black")
canvas.create_rectangle(10,70,20,80,fill="black")
canvas.create_rectangle(40,50,50,60,fill="black")
canvas.create_rectangle(50,60,60,70,fill="black")
canvas.create_rectangle(50,70,60,80,fill="black")


tkinter.mainloop()




