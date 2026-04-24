class Istota:
    def __init__(self,imie, rok_urodzenia):
        self.imie = imie
        self.dt_urodzenia = rok_urodzenia

class KonczynaPrzednia:
    def __init__(self):
        pass

class KonczynaTylna:
    def __init__(self):
        pass

class Glowa:
    def __init__(self, iq:int):
        self.iq = iq

class Ogon:
    def __init__(self):
        pass

    def merda(self):
        print("Merda merda ognkiem jak cie widzi !!!!!!!!!!!!!!!!!!!!!!")

class Tors:
    def __init__(self):
        pass

class Kot(Istota):
    def __init__(self,imie,rok_urodzenia,iq):
        super().__init__(imie,rok_urodzenia)
        self.glowa = Glowa(iq)
        self.konczyna_p_p = KonczynaPrzednia()
        self.konczyna_p_l = KonczynaPrzednia()
        self.tors = Tors()
        self.ogon = Ogon()

mateusz_napieraj = Kot("mateusz",2010, 200)
mateusz_napieraj.ogon.merda()
