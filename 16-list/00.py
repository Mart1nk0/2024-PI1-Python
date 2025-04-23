import random
teploty = [random.uniform(-10, 35) for _ in range(30)]
pocet_dni = 31
# Výpočet priemernej, maximálnej a minimálnej teploty
priemerna_teplota = sum(teploty) / len(teploty)
max_teplota = max(teploty)
min_teplota = min(teploty)

def vypisteplot():
    for i in range(pocet_dni):
        print(f"{i}.deň - {teploty[i]}°C")


print("Teploty za 30 dní:")
print(", ".join(f"{t:.2f}°C" for t in teploty))
print(f"\nPriemerná teplota: {priemerna_teplota:.2f}°C")
print(f"Maximálna teplota: {max_teplota:.2f}°C")
print(f"Minimálna teplota: {min_teplota:.2f}°C")
vypisteplot()