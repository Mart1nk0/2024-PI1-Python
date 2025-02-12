import turtle
import random

turtle.bgcolor('black')
turtle.delay(0)
while True:
    n = random.randint(3, 8)
    t = []
    for i in range(n):
        nova = turtle.Turtle()
        nova.speed(0)
        nova.pu()
        nova.setpos(random.randint(-300, 300),
                    random.randint(-300, 300))
        farba = '#{:06x}'.format(random.randrange(256 ** 3))
        nova.pencolor(farba)
        nova.pd()
        nova.ht()
        t.append(nova)

    for k in range(100):
        for i in range(n):
            j = (i + 1) % n                # index nasledovnej
            uhol = t[i].towards(t[j])
            t[i].seth(uhol)
            vzdialenost = t[i].distance(t[j])
            t[i].fd(vzdialenost)
            t[i].fd(vzdialenost / 10 - vzdialenost)

    for tt in t:
        tt.clear()
        del tt                  