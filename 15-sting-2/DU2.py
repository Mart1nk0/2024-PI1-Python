

import random
import tkinter

def random_color():
    return f"#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}"

def start():
    entered_text = entry.get()
    words = entered_text.split(" ")
    canvas.create_rectangle(-10,-10,710,410,fill="white")
    if entered_text:
        for word in words:
            x = random.randint(75,625)
            y = random.randint(20, 380)

            for char in word:
                canvas.create_text(x,y, text=char, fill=random_color(), font=("arial",18))
                x += 15

root = tkinter.Tk()
root.geometry("800x600")
root.title("Homework")


tkinter.Label(text="Enter your sentence: ", font=("arial",18)).pack(pady=20)
entry = tkinter.Entry(width=600, font="arial, 18")
entry.pack(pady=0, padx=50)
start_btn = tkinter.Button(root, text="START", font=("arial",15), command=start).pack(pady=15)

canvas = tkinter.Canvas(root, width=700, height=400, background="white",highlightthickness=1, highlightbackground="black")
canvas.pack()


tkinter.mainloop()