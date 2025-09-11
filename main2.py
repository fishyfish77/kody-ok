print("a - plaskie b - bryły")
inp = input("a / b ?")
if "a" == inp:
    print('''
    a - pp kwadatu
    b - pp prostokata
    ...

    ''')
    inp = input("? ")
    if inp == "a":
        a = float(input())
        print(f"ppKwadratu o boku {a} = {a**2}")
    inp = input("? ")
    if inp == "b":
        a = float(input("a = "))
        b = float(input("b = "))
        print(f"ppProstokata o bokach {a} i {b} = {a*b}")

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
