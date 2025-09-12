import math
PI=math.pi
print(PI)

print("a - plaskie b - bryły")
inp = input("a / b ?")
if "a" == inp:
    print('''
    a - pp kwadrratu
    b - pp prostokata
    c - pp rownolegloboka
    d - pp trapezu
    e - pp trojkata
    f - pp trojkata rownobocznego
    g - pp kola
    h - pp rombu
          
    A - obw kwadratu
    B - obw prostokata
    C - obw rownolegloboka
    D - obw trapezu
    E - obw trojkata
    F - obw trojkata rownobocznego
    G - obw kola
    H - obw rombu
    
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
    elif inp=="h":
        a=float(input("a="))
        h=float(input("h="))
        print(f"ppRombu o boku {a} i wysokosci {h} = {a*h}")
    elif inp=="A":
        a=float(input("a="))
        print(f"obwKwadratu o boku {a} = {4*a}")
    elif inp=="B":
        a=float(input("a="))
        b=float(input("b="))
        print(f"obwProstokata o bokach {a} i {b} = {2*(a+b)}")
    elif inp=="C":
        a=float(input("a="))
        b=float(input("b="))
        print(f"obwRownolegloboka o bokach {a} i {b} = {2*(a+b)}")
    elif inp=="D":
        a=float(input("a="))
        b=float(input("b="))
        c=float(input("c="))
        d=float(input("d="))
        print(f"obwTrapezu o bokach {a}, {b}, {c} i {d} = {a+b+c+d}")
    elif inp=="E":
        a=float(input("a="))
        b=float(input("b="))
        c=float(input("c="))
        print(f"obwTrojkata o bokach {a}, {b} i {c} = {a+b+c}")
    elif inp=="F":  
        a=float(input("a="))
        print(f"obwTrojkataRownobocznego o boku {a} = {3*a}")
    elif inp=="G":
        r=float(input("r="))
        print(f"obwKola o promieniu {r} = {2*PI*r}")
    elif inp=="H":
        a=float(input("a="))
        print(f"obwRombu o boku {a} = {4*a}")

elif "b" == inp:
    print('''
    a - pc szescianu
    b - pc prostopadloscianu
    c - pc graniastoslupa
    d - pc ostroslupa
    e - pc walca
    f - pc stozka
    g - pc kuli
          
    A - vol szescianu
    B - vol prostopadloscianu
    C - vol graniastoslupa
    D - vol ostroslupa
    E - vol walca
    F - vol stozka
    G - vol kuli

    ''')
    inp = input("? ")
    if inp == "a":
        a = float(input("a = "))
        print(f"pcSzecianu o boku a={a} = {a**2*6}")   
    elif inp == "b":
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        print(f"pcProstopadloscianu o bokach a={a}, b={b}, c={c} = {2*(a*b+b*c+a*c)}")
    elif inp == "c":
        a=float(input("a="))
        H=float(input("H="))
        Pp=float(input("Pp="))
        print(f"pcGraniastoslupa o polu podstawy Pp={Pp} i wysokości H={H} = {2*Pp+a*H}")
    elif inp == "d":
        Pp=float(input("Pp="))
        a=float(input("a="))
        h=float(input("h="))
        n=float(input("n="))
        print(f"pcOstroslupa o polu podstawy Pp={Pp} i boku a={a} i wysokosci sciany trojkata h={h} i liczbie scian bocznych n={n} = {Pp+(n*a*h/2)}")
    elif inp == "e":
        r=float(input("r="))
        H=float(input("H="))
        print(f"pcWalca o promieniu r={r} i wysokosci H={H} = {2*PI*r**2+2*PI*r*H}")
    elif inp== "f":
        r=float(input("r="))
        l=float(input("l="))
        print(f"pcStozka o promieniu r={r} i tworzacej stozka l={l} = {PI*r**2+PI*r*l}")
    elif inp=="g":
        r=float(input("r="))
        print(f"pcKuli o promieniu r={r} = {4*PI*r**2}")
    elif inp == "A":
        a=float(input("a="))
        print(f"volSzescianu o boku a={a} = {a**3}")
    elif inp == "B":
        a=float(input("a="))
        b=float(input("b="))
        c=float(input("c="))
        print(f"volProstopadloscianu o bokach a={a} b={b} c={c} = {a*b*c}")
    elif inp == "C":
        Pp=float(input("Pp="))
        H=float(input("H="))
        print(f"volGraniastoslupa o polu podstawy Pp={Pp} i wysokosci H={H} = {Pp*H}")
    elif inp == "D":
        Pp=float(input("Pp="))
        H=float(input("H="))
        print(f"volOstroslupa o polu podstawy Pp={Pp} i wysokosci H={H} = {Pp*H/3}")
    elif inp == "E":
        r=float(input("r="))
        H=float(input("H="))
        print(f"volWalca o promieniu r={r} i wysokosci H={H} = {PI*r**2*H}")
    elif inp == "F":
        r=float(input("r="))
        H=float(input("H="))
        print(f"volStozka o promieniu r={r} i wysokosci H={H} = {PI*r**2*H/3}")
    elif inp == "G":
        r=float(input("r="))
        print(f"volKuli o promieniu r={r} = {4/3*(PI*r**3)}")
else:
    print("Nie ma takiej komendy")
