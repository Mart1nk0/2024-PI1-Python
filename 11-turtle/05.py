import turtle

t = turtle.Turtle()
t.shape('turtle')
t.shapesize(10, 10, 18)
t.color('cyan', 'magenta')
for i in range(1000):
    t.fd(6)
    t.rt(6)
turtle.done()
