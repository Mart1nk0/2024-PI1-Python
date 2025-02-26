# palin dron je retazec, ktory je rovnaky pri citani od zaciatku alebo od konca
ret = input("Zadaj retazec")
obrateny = ret[::-1]
if ret == obrateny:
    print("Retazec", ret , "je palindrom")
else:
    print("Retazec", ret , "nie je palindrom")