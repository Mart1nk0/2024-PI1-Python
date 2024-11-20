import tkinter

canvas = tkinter.Canvas(width = 650 , height = 450)

canvas.pack()

def cislo(x ,y):

    canvas.create_rectangle(x + 10 , y , x + 20 , y + 10 ,fill= "cyan")
    canvas.create_rectangle(x + 20 , y , x + 30 , y + 10,fill= "cyan")
    canvas.create_rectangle(x + 30 , y , x + 40 , y + 10,fill= "cyan")
    canvas.create_rectangle(x + 40 , y , x + 50 , y + 10,fill= "cyan")
    canvas.create_rectangle(x + 50 , y , x + 60 , y + 10,fill= "cyan")
    canvas.create_rectangle(x + 50 , y + 10 , x + 60 , y + 20,fill= "cyan")
    canvas.create_rectangle(x + 40 , y + 20 , x + 50 , y + 30,fill= "cyan")
    canvas.create_rectangle(x + 30 , y + 30 , x + 40 , y + 40,fill= "cyan")
    canvas.create_rectangle(x + 20 , y + 40, x + 30 , y + 50,fill= "cyan")
    canvas.create_rectangle(x + 20 , y + 50, x + 30 , y + 60,fill= "cyan")
    canvas.create_rectangle(x + 20 , y + 60, x + 30 , y + 70,fill= "cyan")





    canvas.create_rectangle(x + 70 , y + 10 , x + 80 , y+20 ,fill= "cyan")
    canvas.create_rectangle(x + 70 , y + 20 , x + 80 , y + 30,fill= "cyan")
    canvas.create_rectangle(x + 80 , y , x + 90 , y + 10,fill= "cyan")
    canvas.create_rectangle(x + 90 , y , x + 100 , y + 10,fill= "cyan")
    canvas.create_rectangle(x + 100 , y, x + 110 , y + 10,fill= "cyan")
    canvas.create_rectangle(x +90 , y +30 , x+100 , y+40 ,fill= "cyan")
    canvas.create_rectangle(x +100 , y +30 , x+110 , y+40 ,fill= "cyan")
    canvas.create_rectangle(x +80 , y +30 , x+90 , y+40 ,fill= "cyan")
    canvas.create_rectangle(x +110 , y +40 , x+120 , y+50 ,fill= "cyan")
    canvas.create_rectangle(x +110 , y +50 , x+120 , y+60 ,fill= "cyan")
    canvas.create_rectangle(x +110 , y +10 , x+120 , y+20 ,fill= "cyan")
    canvas.create_rectangle(x +110 , y +20 , x+120 , y+30 ,fill= "cyan")
    canvas.create_rectangle(x +70 , y +40 , x+80 , y+50 ,fill= "cyan")
    canvas.create_rectangle(x +70 , y +50 , x+80 , y+60 ,fill= "cyan")
    canvas.create_rectangle(x +80 , y +60 , x+90 , y+70 ,fill= "cyan")
    canvas.create_rectangle(x +90 , y +60 , x+100 , y+70 ,fill= "cyan")
    canvas.create_rectangle(x +100 , y +60 , x+110 , y+70 ,fill= "cyan")



def rad_cisla(x , y , pocet):
    for i in range(pocet):
        cislo(x ,y)
        x+=120

def rady_cisla(x , y , pocet , pocet_raidkov):
    for i in range(pocet_raidkov):
        rad_cisla(x , y , pocet)
        y+=80


rady_cisla(10 , 10, 5 , 5)
























tkinter.mainloop()