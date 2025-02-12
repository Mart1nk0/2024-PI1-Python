import turtle
t = turtle.Turtle()
t.speed(0)

def n_uholnik(n , d ):
    for i in range(n):
        t.fd(d)
        t.lt(360/ n)

for n in range(3 , 16):

    n_uholnik(n,50)

turtle.done()