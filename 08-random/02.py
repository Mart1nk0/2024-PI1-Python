import tkinter
import random


pocet = int(input("Zadaj počet jednotie"))



def jednotka(x, y ):
    canvas.create_rectangle(x+20 , y , x +30 , y+ 10 , fill = random.choice(["red", "blue", "black" , "blue"]))
    canvas.create_rectangle(x+20 , y+ 10  , x +30 , y+ 20 , fill = random.choice(["red", "blue", "black" , "blue"]))
    canvas.create_rectangle(x+20 , y+ 20  , x +30 , y+ 30 , fill = random.choice(["red", "blue", "black" , "blue"]))
    canvas.create_rectangle(x+20 , y+ 30  , x +30 , y+ 40 , fill = random.choice(["red", "blue", "black" , "blue"]))
    canvas.create_rectangle(x+20 , y+ 40  , x +30 , y+ 50 , fill = random.choice(["red", "blue", "black" , "blue"]))
    canvas.create_rectangle(x+20 , y+ 50  , x +30 , y+ 60 , fill = random.choice(["red", "blue", "black" , "blue"]))
    canvas.create_rectangle(x+20 , y+ 60  , x +30 , y+ 70 , fill = random.choice(["red", "blue", "black" , "blue"]))
    canvas.create_rectangle(x+10 , y+ 10  , x +20 , y+ 20 , fill = random.choice(["red", "blue", "black" , "blue"]))
    canvas.create_rectangle(x+10 , y+ 60  , x +20 , y+ 70 , fill = random.choice(["red", "blue", "black" , "blue"])) 
    canvas.create_rectangle(x+30 , y+ 60  , x +40 , y+ 70 , fill = random.choice(["red", "blue", "black" , "blue"]))
 













canvas = tkinter.Canvas(width= 500 , height= 500)
canvas.pack()

for i in range(pocet):
    x = random.randint(3 , 457)
    y = random.randint(3 , 427)
    
    
    jednotka(x ,y )









tkinter.mainloop()







































































