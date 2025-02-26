# string je retazec znakov napr. "Ahoj"
# retazec zaciname a koncime "" alebo ''
# \n - nový riadok, \t - tabulator , \" -  "
# funkcia len() - vrati dlzku retazca (počet znakov)
# znaky rertazcov sú indexované - prvý znak ma index 0
# index píšeme do hranatých zatvoriek [] - p.alf+f , p.alf+g




retazec = "Ahoj Svet"
print(retazec)
print(len(retazec))
#print[retazec[0]]
#print[retazec[1]]
 
#for i in range(len(retazec)):
#   print(retazec[i])

for znak in retazec: # postupne vyberá znaky z retazca do premennej znak
    print(znak)