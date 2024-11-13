import tkinter

canvas = tkinter.Canvas()          
canvas.pack() 
def xko(x ,y): #definície funkcie , xko - názov (to dávame my) , sú to takzvané parametre funkcie
    
   
    canvas.create_rectangle(x,  y , x+10 , y+10 , fill= "Red" )
    canvas.create_rectangle(x , y+10 , x+10 , y+20 , fill= "Red" )
    canvas.create_rectangle(x+10 , y+20 , x+20 , y+30 , fill= "Red" )
    canvas.create_rectangle(x+20,  y+30 , x+30 , y+40 , fill= "Red" )
    canvas.create_rectangle(x+10,  y+40 , x+20 , y+50 , fill= "Red" )
    canvas.create_rectangle(x , y+50 ,  x+10 , y+60  , fill= "Red" )
    canvas.create_rectangle(x , y+60 , x+10 , y+70 , fill= "Red" )
    canvas.create_rectangle(x+30 , y+20 , x+40 , y+30 , fill= "Red" )
    canvas.create_rectangle(x+30 , y+40 , x+40 ,y+50  , fill= "Red" )
    canvas.create_rectangle(x+40 , y , x+50 , y+10 , fill= "Red" )
    canvas.create_rectangle(x+40 , y+10 , x+50 , y+20 , fill= "Red" )
    canvas.create_rectangle(x+40 , y+50 , x+50 , y+60 , fill= "Red" )
    canvas.create_rectangle(x+40 , y+60, x+50 , y+70 , fill= "Red" )
# def riadok  ( x , y pocet):
#     for i in range(pocet):
#         xko(x , y)
#         x += 60

# def riadky_x(x ,y, pocet_riadkov , pocet_stlpcov):
#     for i in range(pocet_riadkov):
        
#         riadok_x(x , y, pocet_stlpcov)
#         x+= 90 




x=10
y=10

pocet = 6
for i in range(pocet):
     xko(x , y)
x = x +60 
x += 60
xko(x-60, y+80)
xko(x-60 , y + 160)
tkinter.mainloop()