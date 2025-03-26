# print(oct(255)) # Vypíše číslo v binárnej podobe
# print(hex(255)) # Vypíše čislo v hexadecimnalnej podobe
# print(0b111111111) # Vypíše binerne čislo v desitkovej podobe
# print(0xFF)  # vypíše hexadecimalne čísla v desiatkovej podobe
def dec_bin(cislo):
    binarne =""
    while cislo > 0:
        zvysok = cislo % 2
        binarne = str(zvysok) + binarne
        
        cislo = cislo // 2 
    return binarne
    

def dec_hex(cislo):
    hexadecimalne = ""
    while cislo > 0:
        zvysok = cislo % 2
        hexadecimalne = str(zvysok) + hexadecimalne
        print(hexadecimalne)
        # cislo = cislo // 16
        # if zvysok == 10:
        #     zvysok = "a"
        # elif zvysok == 11:
        #     zvysok = "b"
        # elif zvysok == 12:
        #     zvysok = "c"
        # elif zvysok == 12:
        #     zvysok = "c"
        # elif zvysok == 13:
        #     zvysok = "d"
        # elif zvysok == 14:
        #     zvysok = "e"
        # elif zvysok == 15:
        #     zvysok = "f"
    if zvysok < 10:
        hexadecimalne = str(zvysok) + hexadecimalne
    else:
        hexadecimalne = chr(55 + zvysok) + hexadecimalne
    cislo = cislo //16
    return hexadecimalne

cislo = 255
print(dec_bin(cislo))
print(dec_hex(cislo))