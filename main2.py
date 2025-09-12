import math
PI=math.pi
print(PI)

print("a - plaskie b - bryły")
inp = input("a / b ?")
if "a" == inp:
    print('''
    a - pp kwadatu
    b - pp prostokata
    c - pp rownolegloboka
    d - pp trapezu
    e - pp trojkata
    f - pp trojkata rownobocznego
    g - pp kola
    h - pp rombu
    ''')
    inp = input("? ")
    if inp == "a":
        a = float(input())
        print(f"ppKwadratu o boku {a} = {a**2}")
    elif inp == "b":
        a = float(input("a = "))
        b = float(input("b = "))
        print(f"ppProstokata o bokach {a} i {b} = {a*b}")
    elif inp == "c":
        a=float(input("a="))
        h=float(input("h="))
        print(f"pprownolegloboka o boku {a} i wysokosci {h} = {a*h}")
    elif inp == "d":
        a=float(input("a="))
        b=float(input("b="))
        h=float(input("h="))
        print(f"ppTrapezu o bokach {a} i {b} i wysokosci {h} = {(a*b)*h/2}")
    elif inp == "e":
        a=float(input("a="))
        h=float(input("h="))
        print(f"ppTrojkata o podstawie {a} i wysokosci {h} = {(a*h)/2}")
    elif inp == "f":
        a=float(input("a="))
        print(f"ppTrojkataRownobocznego o boku {a} = {(a**2)*math.sqrt(3)/4}")
    elif inp=="g":
        r=float(input("r="))
        print(f"ppKola o promieniu {r} = {PI*(r**2)}")
    elif inp=="h"
        a=float(input("a="))
        h=float(input("h="))
        print(f"ppRombu o boku {a} i wysokosci {h} = {a*h}")

elif "b" == inp:
    print('''
    a - pp szescianu
    b - pp prostopadloscianu
    ...

    ''')
    inp = input("?")
    if inp == "a":
        a = float(input("a = "))
        print(f"ppSzecianu dla a={a} = {a**2*6}")   
    inp = input("?")
    if inp == "b":
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        print(f"ppProstopadloscianu dla a={a}, b={b}, c={c} = {2*(a*b+b*c+a*c)}")

else:
    print("Nie ma takiej komendy")
