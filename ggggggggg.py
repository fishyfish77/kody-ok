import plaskie

while True:
    inp:str = input().lower()
    if inp == "x":
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



def pp_prostokat(a:float,b:float)->float:
    return a*b
def pp_rownoleglobok(a:float,h:float)->float:
    return a*h
def pp_romb(a:float,h:float)->float:
    return a*h
def pp_kwadrat(a:float)->float:
    return a**2
def pp_romb(a:float,h:float)->float:
    return (a*h)*0.5
