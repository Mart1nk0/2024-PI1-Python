teploty = [10,13,15,20]
print(teploty)
print(teploty[0])


nakup = ["chlieb" , "maslo" , "treska"]
print(nakup)
print(nakup[1])

zviera = ("Turtle , Mbappe , 1998 , hnedá, 80kg") # Do listu môžeme vkladať hodnoti rôznych typov(int , str , bool...)
print(zviera)
print(zviera[2])

# v Pythonr sú listy dynamické, to znamená, že nemusia mať definovanu velkosť (POčET PRVKOV)

prazdny = []
print(prazdny)
prazdny.append(25)
print(prazdny)
prazdny.append("Ahoj")
print(prazdny)
prazdny.append("100")
print(prazdny)
print(prazdny[-1])

# listy vieme aj zretaziť (spočitat)

nakupyzvierat = nakup + zviera
print(nakupyzvierat)
print(3*zviera)

print("Mbappe" in zviera)

# narozdiel od stringu môzeme prepisat hodnotu

prazdny[0] = 1000
print(prazdny)
hodnoty = [15,30,25,20,30]