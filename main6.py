from random import randint
import time

# hp atk magia gold
hero = [300,20,20,20]
inventory = ["drewniany miecz", "rozdzka"]
print("a - idz do lasu // b - idz nad jezioro // c - idz do miasta")
while hero[0]>0:
    enemy = [randint(10,170), randint(15,80), randint(10,75)]
    print(f"hero ; hp: {hero[0]}  atk: {hero[1]}  magia: {hero[2]}  gold: {hero[3]}")
    print(f"ekwipunek ; {inventory}")
    print("---"*5)
    inp = input("gdzie idziesz? - ")
    if inp == "a":
            while True:
                if hero[0]<=0:
                    print("umarles, gra zakonczona")
                    break
                if enemy[0]<=0:
                    print(f"znalazles zloto. ilosc - {enemy[2]}")
                    hero[3] += enemy[2]
                    break
                print(f"enemy ; hp: {enemy[0]}  atk: {enemy[1]}")
                print(f"hero ; hp: {hero[0]}  atk: {hero[1]}")
                print("a - normalny atak // b - magiczny atak // c - leczenie")
                inp = input("")
                if inp == "a":
                    hero[0] -= enemy[1]
                    enemy[0] -= hero[1]
                elif inp == "b":
                    hero[0] -= enemy[1]
                    enemy[0] -= hero[2]
                elif inp == "c":
                    print("nie posiadasz takiego eliksiru. mozesz go kupic w miescie lub zebrac jagody nad rzeka.")
                    hero[0] -= enemy[1]
                else:
                    print("nic nie robisz i stoisz w miejscu.")
                    hero[0] -= enemy[1]
                    time.sleep(1)
    elif inp == "b":
        print("dotarles bezpiecznie nad jezioro. co chcialbys teraz zrobic?")
        print("a - wejsc do wody // b - lowic ryby // c - zebrac jagody")
        inp = input("")
        if inp == "a":
            print("ajajaj, nie umiesz plywac! utonales w jeziorze i umierasz")
            break
        elif inp == "b":
            print("niestety nie posiadasz jeszcze wedki, mozesz ja zakupic w miescie.")
            pass
        elif inp == "c":
            print("znalazles jagody, ktore maja wartosc lecznicza!")
            inventory += ["5 jagod"]
            pass
    elif inp == "c":
        print("dotarles do miasta. jest to bardzo zywe miasto, w ktorym jest pelno rzeczy do roboty. w ktora strone najpierw pojdziesz?")
        print("a - centrum miasta, pelne roznych sklepow // b - prawa strona, bardziej pusta. idealna do wypoczynku i zrelaksowania // c - lewa strona, jest tutaj kowal, ktory moze zrobic bron")
        inp = input("")
        if inp == "a":
            print("znalazles sie w centrum miasta. wokol siebie widzisz wiele sklepow, ale pewne dwa zwracaja twoja szczegolna uwage")
            print("e - sklep z eliksirami // j - sklep z jedzeniem")
            inp = input("")
            if inp == "e":
                print("wchodzac do sklepu, zauwazasz na polkach wiele kolorowych mikstur. mila sprzedawczyni za lada pyta sie, czego potrzebujesz. co odpowiadasz?")
                print("l - eliksir leczacy +50hp za 10 gold // a - eliksir dajacy permanentnie +20atk za 10 gold // m - eliksir dajacy permanentnie +20magii za 10 gold")
                inp = input("")
                koszt = 10
                atk = 20
                magia = 20
                if inp == "l" and hero[3] >= koszt:
                    hero[3] -= koszt
                    inventory += ["eliksir leczacy"]
                    pass
                elif inp == "a" and hero[3] >= koszt:
                    hero[3] -= koszt
                    hero[1] += atk
                    pass
                elif inp == "m" and hero[3] >= koszt:
                    hero[3] -= koszt
                    hero[2] += magia
                    pass
            elif inp == "j":
                print("podchodzac do stoiska z roznymi owocami, warzywami itp, starsza pani sprzedajaca to pyta sie, czy chcialbys cos do jedzenia. na co masz ochote?")
                print("j - jablko 1gold // ch - bochenek chleba 3gold // w - worek warzyw 10gold ")
                koszt_j = 1
                koszt_ch = 3
                koszt_w = 10
                if inp == "j":
                    hero[3] -= koszt_j
                    inventory += ["jablko"]
                elif inp == "ch":
                    hero[3] -= koszt_ch
                    inventory += ["bochenek chleab"]
                elif inp == "w":
                    hero[3] -= koszt_w
                    inventory += ["worek warzyw"]
                    pass
        elif inp == "b":
            print("wybrales prawa strone. odpoczywasz przez 10s")
            time.sleep(10)
        elif inp == "c":
            print("dotarles do kowala, tutaj mozesz kupic nowa bron.")
            print("z - zelazny miecz , 50 gold , +15atk // zl - zloty miecz , 100 gold , +30 atk // d - diamentowy miecz 150 golld , +40atk")
            zkoszt = 50
            zlkoszt = 100
            dkoszt = 150
            zatk = 15
            zlatk = 30
            datk = 40
            if inp == "z":
                hero[3] -= zkoszt
                hero[1] += zatk
                inventory += ["zelazny miecz"]
            elif inp == "zl":
                hero[3] -= zlkoszt
                hero[1] += zlatk
                inventory += ["zloty miecz"]
            elif inp == "d":
                hero[3] -= dkoszt
                hero[1] += datk
                inventory += ["diamentowy miecz"]
