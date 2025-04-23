subor = open("subor2.txt", "w") # ak subor neexistuje tak sa vytvorí , ak existuje ecelý sa zmaže
# subor.write("Ahoj\n")
# subor.write("ako\n")
# subor.write("sa\n")
# subor.write("mas\n?")
print("Ahoj" , file = subor)


subor.close()