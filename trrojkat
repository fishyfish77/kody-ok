# a:float = int(input("a"))
# b:float = int(input("b"))
# c:float = int(input("c"))


def trojkat(a:float, b: float, c:float)->None:
    if a**2 + b**2 == c**2 or b**2 + c**2 == b**2 or c**2 + b**2 == a**2:
        return print("Tak")
    else:
        return print("Nie")

from typing import List
from random import randint

def n_poteg_2(n:int)->List:
    x = []
    for i in range(n):
        x.append(2**i)
    return x

# x = n_poteg_2(10)
# print(x)
# print(len(x))
# print(n_poteg_2(10))
# -----------------------------------------------------------
def n_poteg_2(n:int) -> List:
    return [2**i for i in range(n)]
x = n_poteg_2(10)
print(x)
print(len(x))
print(n_poteg_2(10))
# ------------------------------------------------------------
def liczb_losowych_od_do(od:int, do:int, ile:int) -> List:
    return [randint(od, do) for _ in range(ile)]
# ---------------------------------------------------------------
def list_iteration(lst:List) -> None:
    for index, value in enumerate(lst):
        print(f"index {index} ----- v {value}")

print(n_poteg_2(10))
list_iteration(n_poteg_2(10))
print(liczb_losowych_od_do(-100,100,10))
list_iteration(liczb_losowych_od_do(-100,100,10))