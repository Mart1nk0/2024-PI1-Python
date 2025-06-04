import datetime

class  Osoba: # triedy , vzdy piseme prvým veľkým písmenom
    def __init__(self, meno , priezvisko , rok): # konštruktor, zavolá sa pri vzniku objektu
        self.meno = meno # aktribút objektu (vlastnosť)
        self.priezvisko = priezvisko
        self.rok = rok
        self.vek = datetime.date.today().year - self.rok

    def pozdrav(self): # metóda , (čo vie objekt robiť)
        print(f"Ahoj , ja som {self.meno} {self.priezvisko} a narodil som sa v roku {self.rok} a mam {self.vek} rokov")


    def vypis_meno(self):
        print(self.meno , self.priezvisko)



    def vypis_vek(self):
        print(self.vek)

    def vypis_rok(self):
        print(self.rok)

class Stundent(Osoba): # trieda dostane atributy od Osoby
    def __init__(self, meno, priezvisko, rok, trieda):
        super().__init__(meno, priezvisko, rok ) # super - znamená , že použije atribúty z rodičovskej triedy osoba
        self.trieda = trieda

    def pozdrav(self):
        super().pozdrav()
        print(f"Som študentom {self.trieda} triedy")
        # polymorfizmus - meníme metodu pozdrav z rodičovskej triedy



# Martinko = Osoba("Martinečko ","Mitka",2009)
# Martinko.pozdrav()  # Metoda objektu pozdrav
# Alex = Osoba("Alexik ","Slivka",2009)
# Alex.pozdrav()

# Martinko.vypis_meno()
# Martinko.vypis_vek()
# Martinko.vypis_rok()

student = Stundent("Ján", "študent", 2008 , "I.AT")
student.pozdrav()
student.vypis_meno()
student.vypis_rok()
student.vypis_vek()

clovek = Osoba("Jurko", "Mrkva", 2000,)