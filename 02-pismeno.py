import turtle


t = turtle.Turtle()   # premenne t sa priradi korytnačka
d = 15


def stvorec():
     for i in range(4):
      t.forward(d)
      t.left(90)
    
def pismenoM():
        stvorec()
        t.left(90)
        t.forward(d)
        t.rt(90)    
        
        
        
for i in range(4):
    stvorec()         
    t.left(90)
    t.forward(d)
    pismenoM()
t.right(90)
t.forward(30)
t.left(90)
t.forward(15)
stvorec()
t.penup()
t.right(90)
t.forward(30)
t.left(90)
t.forward(15)
t.pendown()
stvorec()
t.left(90)
t.forward(15)
t.right(90)
stvorec()
t.penup()
t.forward(15)
t.left(90)
t.forward(15)
t.right(90)
t.pendown()
stvorec()
t.forward(15)
stvorec()
t.left(90)
t.forward(15)
t.right(90)
stvorec()
t.penup
t.right(90)
t.forward(90)
t.left(90)
t.pendown
for i in range(5):
    stvorec()
    t.left(90)
    t.forward(d)
    t.right(90)


turtle.mainloop()