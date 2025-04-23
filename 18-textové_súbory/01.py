subor = open("subor.txt","r") # súbor text je relatívna cesta k súboru (musí býť v tom istom priečinku ako samostatný kód)
# otvorí subor na čítanie , pre zápis sa používa "w" , r = read , w = write
#subor = open("c:/dokumenty/subor.txt" , "w") - toto je absolútna cesta "c:/dokumenty/subor.txt"
# subor = open("../16-list/subor.txt"/ , "r") .. je  o prierčínok vyššie
 # zatvorí súbor

# for i in range(4):
#     riadok = subor.readline()
#     print(riadok)


# riadok = subor.readline()
# while riadok != "":
#     print(riadok)
#     riadok = subor.readline()

subor = open("subor.txt,  ")
while True:
        riadok = subor.readline
        if riadok == "":
            break
        print(riadok.strip())



subor.close()