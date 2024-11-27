import tkinter , random
n = int(input("zadaj počet štvorcov :"))
m1 = int(input("zadaj sírku plátna :"))
m2 = int(input("zadaj výšku plátna :"))
canvas = tkinter.Canvas(width=m1 , height=m2)




canvas.pack()





for i in range(n + 1):
    random_dlzka = random.randint(1 , 30)
    x = random.randint(3 , m1-3-random_dlzka)
    y = random.randint(3 , m2-3-random_dlzka)
    
    if random_dlzka < 10:
        canvas.create_rectangle(x , y , x + random_dlzka , y + random_dlzka , fill="magenta")
    elif 10  < random_dlzka < 20:
       canvas.create_rectangle(x , y , x + random_dlzka , y + random_dlzka , fill="navy")
    elif 20  < random_dlzka < 30:
        canvas.create_rectangle(x , y ,  x + random_dlzka , y + random_dlzka , fill= "gold")












































































tkinter.mainloop()