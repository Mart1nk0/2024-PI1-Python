a = int(input("Zadaj číslo a: "))
b = int(input("Zadaj číslo b: "))
if a > b:
    print("Väčšie je číslo" , a)
else:
    print("Väčšie je číslo" , b) 
# if je podmienený príkaz
# najskvôr zistí splnenie podmienky, ak platí, tak sa vykonajú príkazy za dvojbodkou (odsadené od kraja)
# ak podmienka nepatrí, vykonajú sa príkazy za else: (odsadené od kraja)