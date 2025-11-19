import plaskie
import bryly
import math

while True:
    inp:str = input().lower()
    if inp == "wyjdz":
        break
    elif inp == "a":
        a:float = float(input("a: "))
        b:float = float(input("b: "))
        wynik = plaskie.pp_prostokat(a,b)
        print(f"ppProstokata = {wynik}")
    elif inp == "b":
        a:float = float(input("a: "))
        h:float = float(input("h: "))
        wynik = plaskie.pp_rownoleglobok(a,h)
        print(f"ppRownolegloboka = {wynik}")
    elif inp == "c":
        a:float = float(input("a: "))
        h:float = float(input("h: "))
        wynik = plaskie.pp_romb(a,h)
        print(f"ppRomba = {wynik}")
    elif inp == "d":
        a:float = float(input("a: "))
        wynik = plaskie.pp_kwadrat(a)
        print(f"ppKwadratu = {wynik}")
    elif inp == "e":
        a:float = float(input("a: "))
        wynik = bryly.pp_szescian(a)
        print(f"ppSzescianu = {wynik}")
    elif inp == "f":
        a:float = float(input("a: "))
        b:float = float(input("b: "))
        c:float = float(input("c: "))
        wynik = bryly.pp_prostopadloscian(a,b,c)
        print(f"ppProstopadloscianu = {wynik}")
    elif inp == "g":
        pp:float = float(input("pp: "))
        pb:float = float(input("pb: "))
        wynik = bryly.pp_graniastoslup(pp,pb)
        print(f"ppGraniastoslupa = {wynik}")
    elif inp == "h":
        pp:float = float(input("pp: "))
        pb:float = float(input("pb: "))
        wynik = bryly.pp_ostroslup(pp,pb)
        print(f"ppOstroslupa = {wynik}")
    elif inp == "i":
        r:float = float(input("r: "))
        H:float = float(input("H: "))
        wynik = bryly.pp_walec(r,H)
        print(f"ppWalca = {wynik}")
    elif inp == "j":
        r:float = float(input("r: "))
        l:float = float(input("l: "))
        wynik = bryly.pp_stozek(r,l)
        print(f"ppStozka = {wynik}")
    elif inp == "k":
        ar:float = float(input("r: "))
        wynik = bryly.pp_kula(r)
        print(f"ppKuli = {wynik}")
