import random

TEPLOTY= []
dni = 30
for i in range(30):
    TEPLOTY.append(random.randint(10 , 30))
suma =0
for i in range(dni):
    print(f"{i +1 }.den - {TEPLOTY[i]} C")
priemerna = suma / dni




print(f"priemerna teplota v mesiaci je { priemerna:.2f}°C") # naformatuje vystup





print("Dni s podpriemernu teplotou:")