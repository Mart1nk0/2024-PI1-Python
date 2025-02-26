# String v pythone je immutable, tzv. nemenny
ret = "Ahoj svet"
#ret[0] = "a"  toto neni možne lebo je to immutable
ret = "a" + ret[1:] # ak chceme zmeniť znak, musímr to urobiť takto
print(ret)



# retazce vieme porovnavat
print("a" == "b")
print(ord("a"))
print(ord("A"))