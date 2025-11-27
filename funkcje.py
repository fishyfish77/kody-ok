main.py

from funkcje import statystyki as s

s.xxxx()
s.xxxx()
s.xxxx()
s.xxxx()
print(s.HP)


statystyki

HP = []

def xxxx()->None:
    HP.append("A")


xxxx()
xxxx()
print(HP)

--

from funkcje import statystyki as s
from funkcje import ksiega_zaklec as k



x = k.fire_ball()
y = k.ksiega_zaklec()
print(x)
print(y)

ksiega zaklec


from . import statystyki as s
from random import randint

print(s)

def fire_ball()->None:
    if s.MANA >= 30:
        s.MANA -= 30
        return 6*randint(1,8)
    else:
        print("nie ma many")

def ksiega_zaklec()->None:
    while True:
        print("ss")
        inp:str = input().lower()
        if inp =="e":
            break
        elif inp == "f":
            return fire_ball()
