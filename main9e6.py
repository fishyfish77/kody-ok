# n = int(input())
# for i in range(n+1):
#     print(f"2^{i} == {2**i}")

x = "dsdaddsddad"
for el in x:
    print(el)
print("---"*10)

x = [1,2,3]
for el in x:
    print(el)
print("---"*10)

ccc = [1,1,1,2,3,4,5,6]

# i = 0
# while i < len(ccc):
#     print(f"pod ind {i} ---- {ccc[i]}")
#     i += 1

# for el in ccc:
#     print(el)

inp = int(input())
cz_jest = False
# for el in ccc:
#     if inp == el:
#         cz_jest = True
#         break
i = 0
while i < len(ccc):
    if inp ==  ccc[i]:
        cz_jest = True
        break
    i += 1

if cz_jest:
    print("jest")
else:
    print("nie ma")



# # wyswietl z pomoca for wszytskie indeksy i wartosci z listy

x = [5,5,5,3,2,1]
for i, v in enumerate(x):
    print(f"{i} --- {v}")

for i in range(len(x)):
    print(f"{i} --- {x[i]}")

# # napisz slowo n razy i zapisz wyniki do listy

slowo = input()
ile = int(input())
k = []
for _ in range(ile):
    print(slowo)
    k.append(slowo)
print(k)

slowo = input()
ile = int(input())
k = []
i = 0
while i < ile:
    print(slowo)
    k.append(slowo)
    i += 1
print(k)

# # znajdz maksymalny element w liscie liczb

x = [1,2,3,4,5,-10,2]
if len(x) == 0:
    print("lista jest pusta")
else:
    my_max = x[0]
    for el in x:
        if el > my_max:
            my_max = el
print(my_max)
print(max(x))

x = [1,2,3,4,5,-10,2]
if not x:
    print("lista jest pusta")
else:
    my_max = x[0]
    i = 1
    while i < len(x):
        if x[i] > my_max:
            my_max = x[i]
        i += 1
print(my_max)
print(max(x))

# # usuwaj elementy z listy tak aby w koncu nie zawierala rzadnych powtorzen

x = [1,1,1,1,2,2,2,3,3,3,3]
unikatowe = []
for el in x:
    if el not in unikatowe:
        unikatowe.append(el)
x = unikatowe
print(x)
print(list(set(x)))

x = [1,1,1,1,2,2,2,3,3,3,3]
unikatowe = []
i = 0
while i < len(x):
    if el not in unikatowe:
        unikatowe.append(el)
    i += 1
x = unikatowe
print(x)
print(list(set(x)))

# # wygeneruj n-elementowa liste liczb calkowitych z przedzialu [a,b]
from random import randint

n = int(input())
od = int(input())
do = int(input())
los = []
for _ in range(n):
    los.append(randint(od,do))
print(los)

n = int(input())
od = int(input())
do = int(input())
los = []
i = 0
while i < n:
    los.append(randint(od,do))
    i += 1
print(los)

# # policz ile podana liczba x wystepuje w liscie

x = [1,2,3,4,4,4,2]
ile = 0
liczba = int(input())
for el in ile:
    if liczba == el:
        ile += 1

x = [1,2,3,4,4,4,2]
i = 0
while i < len(x):
        if liczba == x[i]:
            ile += 1
        i += 1

# # oblicz srednia arytmetyczna liczb w liscie

x = [4,4,6]
if not x:
    print("lista jest pusta")
else:
    s = 0
    for el in x:
        s += el
print(s / len(x))
print(sum(x) / len(x))

x = [ 4,4,6]
if not x:
    print("lista jest pusta")
else:
    s = 0 
    i = 0 
    while i < len(x):
        s += x[i]
        i += 1
    print(s / len(x))
    
