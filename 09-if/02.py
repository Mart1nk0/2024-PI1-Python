import tkinter , random

m1 = int(input("zadaj sírku plátna :"))
m2 = int(input("zadaj výšku plátna :"))
canvas = tkinter.Canvas(width=m1 , height=m2)
canvas.pack()
for i in range(1000):
    a= 10
    x = random.randint(3 , m1 - 3-a)
    y = random.randint(3 , m2 -3-a)



    if x < m1 / 2 :
        if y < m2 / 2 :
            farba = "blue"
        else:
            farba= "red"
    else:
        if y < m2 // 2:
            farba = "gold"
        else:
            farba= "green"


canvas.create_oval(x , y , x+10 , y +10 , width= 0 )

tkinter.mainloop()