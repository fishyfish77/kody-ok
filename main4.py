from random import randint

# srednia z losowan
# wylosuj 10 liczb 1-50, wypisz srednia oraz ile jest podzielnych przez 5.

# i=0
# ile_podzielnych_przez_5 = 0
# suma=0
# while i<10:
#     r=randint(1,50)
#     suma+=r
#     if r % 5 == 0:
#         ile_podzielnych_przez_5 += 1
#     i+=1
# print(ile_podzielnych_przez_5)
# print(suma/10)

# wczytaj k. losuj liczby 1-100 az trafisz liczbe podzielna przez k. zlicz proby.

# k=int(input())
# proby=0
# while k>0:
#     r=randint(1,100)
#     if r % k == 0:
#         break
#     else:
#         proby += 1
# print(proby)
# print(r)

# liczenie cyfr w liczbie
# podaj ile cyfr ma liczba dodatnia n bez zmiany na string

# k = int(input())
# ile=0
# while k>0:
#     k//=10
#     ile+=1
# print(ile)

# silnia z kontrola wejscia
# policz n! petla while. dla n<0 wypisz blad

# n=int(input())
# if n<0:
#     print("blad")
# else:
#     s=1
#     while n>0:
#         s*=n
#         n-=1
#     print(f"silnia wynosi {s}")

# potega dwojki
# wczytaj n i sprawdz, czy jest potega 2, dzielac n przez 2 dopoki n%2==0

# n=int(input())
# if n<0:
#     print("nie jest potęgą dwójki")
# else:
#     while n%2==0:
#         n//=2
#     if n==1:
#         print("jest potęgą dwójki")
#     else:
#         print("nie jest potęgą dwójki")
