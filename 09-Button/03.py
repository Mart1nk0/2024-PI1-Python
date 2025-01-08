import tkinter as tk
import random
root = tk.Tk()
root.geometry("200x200")
pokus = 1
random_cislo = random.randint(0, 9 )


def akciaTlacidlo():
    global pokus
    cisloMOJE = text =  textbox.get()
    if int(cisloMOJE) < random_cislo:
        label.config(text= f"Dal si menšie číslo pokus:{pokus} )")
        pokus += 1
    elif int(cisloMOJE) > random_cislo:
        label.config(text=f"Dal si väčšie číslo pokus :{pokus} )")
        pokus += 1 

    elif int(cisloMOJE) == random_cislo:
        label.config(text=f"Uhadol si číslo pokus :{pokus} )")







label = tk.Label(root, text= "Hadaj")
label.pack() 
textbox = tk.Entry(root)
textbox.pack()

button= tk.Button(root, text= "Hádaj" , command=akciaTlacidlo )
button.pack()

root.mainloop()