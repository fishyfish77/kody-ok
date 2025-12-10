from . import statystyki as s
from random import randint
def zwykly_atk():
    return randint(20,50)
def atk_z_luku():
    if 'luk' in s.inv:
        return randint(20,50)
    else:
        print('nie masz luku')
        return 0
def fireball():
    if  s.MANA <10:
        print('nie masz wystarczajaco many')
        return 0
    s.MANA -= 10
    return randint(20,50)
def piorun():
    if  s.MANA <10:
        print('nie masz wystarczajaco many')
        return 0
    s.MANA -= 10
    return randint(20,50)
def whoosh():
    if  s.MANA <5:
        print('nie masz wystarczajaco many')
        return 0
    s.MANA -= 5
    return randint(10,30)
def lodowka():
    if  s.MANA <15:
        print('nie masz wystarczajaco many')
        return 0
    s.MANA -= 15
    return randint(30,60)
def glaz():
    if  s.MANA <20:
        print('nie masz wystarczajaco many')
        return 0
    s.MANA -= 20
    return randint(40,60)
def magia_biala():
    if  s.MANA <50:
        print('nie masz wystarczajaco many')
        return 0
    s.MANA -= 50
    return randint(50,80)
def magia_ciemna():
    if  s.MANA <50:
        print('nie masz wystarczajaco many')
        return 0
    s.MANA -= 50
    return randint(50,80)
def ataki()->None:
    while True:
        print('wybierz atak: n - zwykly atak / l - atak z luku / f - fire ball / p - piorun / w - wiatr / d - lodowka / g - glaz / b - magia biala / c - magia ciemna / x - wyjdz') 
        inp = input().lower()
        if inp =='x':
            break
        elif inp =='n':
            return zwykly_atk
        elif inp =='l':
            return atk_z_luku
        elif inp =='f':
            return fireball
        elif inp =='p':
            return piorun
        elif inp =='w':
            return whoosh
        elif inp =='d':
            return lodowka
        elif inp =='g':
            return glaz
        elif inp =='b':
            return magia_biala
        elif inp =='c':
            return magia_ciemna