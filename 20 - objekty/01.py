class Ziak:
    def __init__(self, meno, priezvisko, rok_narodenia, oblubene_auto, oblubene_zviera, farba, cislo):
        self.meno = meno
        self.priezvisko = priezvisko
        self.rok_narodenia = rok_narodenia
        self.oblubene_auto = oblubene_auto
        self.oblubene_zviera = oblubene_zviera
        self.farba = farba
        self.cislo = cislo

    def __str__(self):
        return f"{self.meno} {self.priezvisko}, narodený {self.rok_narodenia}, " \
               f"obľúbené auto: {self.oblubene_auto}, obľúbené zviera: {self.oblubene_zviera}, " \
               f"obľúbená farba: {self.farba}, číslo: {self.cislo}"

    def uloz_do_suboru(self, nazov_suboru):
        with open(nazov_suboru, "a", encoding="utf-8") as subor:
            subor.write(f"\n{'-'*40}\n")
            subor.write(f"Meno: {self.meno}\n")
            subor.write(f"Priezvisko: {self.priezvisko}\n")
            subor.write(f"Rok narodenia: {self.rok_narodenia}\n")
            subor.write(f"Obľúbené auto: {self.oblubene_auto}\n")
            subor.write(f"Obľúbené zviera: {self.oblubene_zviera}\n")
            subor.write(f"Obľúbená farba: {self.farba}\n")
            subor.write(f"Číslo: {self.cislo}\n")
            subor.write(f"{'-'*40}\n")

# Funkcia na načítanie existujúcich žiakov zo súboru
def nacitaj_ziakov(nazov_suboru):
    ziaci = []
    try:
        with open(nazov_suboru, "r", encoding="utf-8") as subor:
            obsah = subor.read().strip()
            if obsah:
                print(f"\n--- Existujúci žiaci ---\n{obsah}")
            else:
                print("Zatiaľ žiadni žiaci nie sú uložení.")
    except FileNotFoundError:
        pass  # Ak súbor neexistuje, nič sa nedeje

# Cesta k súboru
subor = "ziaci.txt"

# Načítanie a vypísanie existujúcich žiakov
nacitaj_ziakov(subor)

# Zadanie nového žiaka
print("\n--- Zadaj nového žiaka ---")
meno = input("Zadaj meno: ")
priezvisko = input("Zadaj priezvisko: ")
rok = input("Zadaj rok narodenia: ")
auto = input("Zadaj obľúbené auto: ")
zviera = input("Zadaj obľúbené zviera: ")
farba = input("Zadaj obľúbenú farbu: ")
cislo = input("Zadaj svoje číslo (napr. telefónne číslo alebo iné): ")

novy_ziak = Ziak(meno, priezvisko, rok, auto, zviera, farba, cislo)
novy_ziak.uloz_do_suboru(subor)

print("\nŽiak bol úspešne pridaný!")

# Vypísanie nových žiakov zo súboru
nacitaj_ziakov(subor)
