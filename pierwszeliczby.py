from math import sqrt
from typing import List

def czy_pierwsza(m:int)->bool:
    if m< 2:
        return False
    elif m==2 or m==3:
        return True
    elif m%2==0:
        return False
    i=3
    while i <= sqrt(m):
        if m%i==0:
            return False
    return True

# x=[]
# for i in range(100):
#     print(f"{i} -------- {czy_pierwsza(i)}")
#     if czy_pierwsza(i):
#         x.append(i)
# print(x)

def ile_pierwszych(m:int)->int:
    ile=0
    for i in range(m):
        if czy_pierwsza(i):
            ile += 1
        return ile
    
def lista_liczb_pierwszych(m:int)->int:
    list =[]
    for i in range(m):
        if czy_pierwsza(i):
            list.append(i)
    return list

def iteration(list:List)->None:
    for i, v in enumerate(list):
        print(f"{i} ------- {v}")

iteration(lista_liczb_pierwszych(100))
