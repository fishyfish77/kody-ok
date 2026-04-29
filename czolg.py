class Czolg:
    def __init__(self,nazwa,rok_stworzenia,masa_kg):
        self.nazwa=nazwa
        self.rok_stworzenia=rok_stworzenia
        self.masa=masa_kg

class Wiezyczka:
    def __init__(self) -> None:
        pass
    def wiezyczka(self):
        print("tutaj siedzi glownwy komander")

class Armata:
    def __init__(self) -> None:
        pass
    def strzal(self):
        print("strzelasz. mocne.")

class Gasienice:
    def __init__(self) -> None:
        pass
    def chodzenie(self):
        print("czolgasz sie")

class Pancerz_slaby:
    def __init__(self) -> None:
        pass
    def obrona_s(self):
        print("nie obrania. nie super.")

class Pancerz_normalny:
    def __init__(self) -> None:
        pass
    def obrona_n(self):
        print("obrania. super.")

class Wyrzutnie_granatow:
    def __init__(self) -> None:
        pass
    def rzuca(self,nazwa):
        print(f"czolg {nazwa} wyrzuca granaty")

class Silnik:
    def __init__(self) -> None:
        pass

class Karabin_maszynowy:
    def __init__(self) -> None:
        pass
    def strzela(self):
        print("strzelasz z karabinu maszynowego, super")

class Czolg_lekki(Czolg):
    def __init__(self,nazwa,rok_stworzenia,masa_kg):
        super().__init__(nazwa,rok_stworzenia,masa_kg)
        self.wiezyczka=Wiezyczka()
        self.armata=Armata()
        self.gasienice=Gasienice()
        self.pancerz=Pancerz_slaby()
        self.silnik=Silnik()
        self.karabin=Karabin_maszynowy()

class Czolg_sredni(Czolg):
    def __init__(self,nazwa,rok_stworzenia,masa_kg):
        super().__init__(nazwa,rok_stworzenia,masa_kg)
        self.wiezyczka=Wiezyczka()
        self.armata=Armata()
        self.gasienice=Gasienice()
        self.pancerz=Pancerz_normalny()
        self.wyrzutnie=Wyrzutnie_granatow()
        self.silnik=Silnik()
        self.karabin=Karabin_maszynowy()

class Czolg_ciezki(Czolg):
    def __init__(self,nazwa,rok_stworzenia,masa_kg):
        super().__init__(nazwa,rok_stworzenia,masa_kg)
        self.wiezyczka=Wiezyczka()
        self.armata=Armata()
        self.gasienice=Gasienice()
        self.pancerz=Pancerz_normalny()
        self.wyrzutnie=Wyrzutnie_granatow()
        self.silnik=Silnik()
        self.karabin=Karabin_maszynowy()

class Czolg_podstawowy(Czolg):
    def __init__(self, nazwa, rok_stworzenia, masa_kg):
        super().__init__(nazwa, rok_stworzenia, masa_kg)
        self.wiezyczka = Wiezyczka()
        self.armata = Armata()
        self.gasienice = Gasienice()
        self.pancerz = Pancerz_normalny()
        self.wyrzutnie = Wyrzutnie_granatow()
        self.silnik = Silnik()
        self.karabin = Karabin_maszynowy()

siedemTP=Czolg_lekki("7TP",1935,9900)
T34=Czolg_sredni("T-34",1941,26500)
PzKpfw_VI_Tiger=Czolg_ciezki("PzKpfw VI Tiger I",1942,56900)
Leopard_2=Czolg_podstawowy("Leopard_2A5",1995,57700)

T34.karabin.strzela()