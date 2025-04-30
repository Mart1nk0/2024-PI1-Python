
import tkinter as tk
import random

canvas = tk.Canvas(width = 800 , height=800 )
canvas.pack()
ftvary = open("tvary.txt", "w")
tvary = ["o","r","l"]

def farba():
    return f"#{random.randint(0 , 255):02x}{random.randint(0,255)}{random.randint(0 , 255):02x}"

for i in range(10):
    print(random.choice(tvary) , random.randint(3 ,797),random.randint(3,797),random.randint(3 , 797),random.randint(3 , 797),farba())

for i in range(10):
    print(random.choice(tvary) , random.randint(3 ,797),random.randint(3,797),random.randint(3 , 797),random.randint(3 , 797),farba(),file=ftvary)





tk.mainloop()










