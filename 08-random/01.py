import random # knižnica na generovanie náhodných hodnôt



nahodne_cislo = random.randint(1 , 10) # vygeneruje náhodné celé čislo z rozsahu 1..10
print(nahodne_cislo)


nahodna_farba = random.choice(["red ", "green" ," blue ", "cyan ", "black" , "grey"]) # vygeneruje náhodnu hodnotu zo zoznamu hodnôt , zoznam ohraničime [] = plavy alt + f alebo pravy alt + g
print(nahodna_farba)

nahodne_pismeno = random.choice("delfk")
print(nahodne_pismeno)