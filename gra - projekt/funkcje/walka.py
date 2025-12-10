from . import statystyki as s
from . import ataki as a
from . import przeciwnicy as p
def walka()->None:
    przeciwnik = p.losowi_przeciwnicy()
    print(f'pojawil sie przeciwnik: {przeciwnik[0]} hp: {przeciwnik[1]} atk: {przeciwnik[2]}')
    while True:
        atk = a.ataki()
        obrazenia = atk()
        przeciwnik[1] -= obrazenia
        print(f'zadales {obrazenia} obrazen przeciwnikowi. Zostalo mu {przeciwnik[1]} hp')
        if przeciwnik[1]<=0:
            print(f'pokonales przeciwnika {przeciwnik[0]}')
            s.EXP += 25
            s.GOLD += 20
            print(f'zdobywasz 20 exp i 20 golda. masz teraz {s.EXP} exp i {s.GOLD} golda.')
            break
        s.HP -= przeciwnik[2]*(1-s.DEF/100)
        print(f'przeciwnik zaatakowal i zadaje ci {przeciwnik[2]*(1-s.DEF/100)} obrazen. zostalo ci {s.HP} hp')
        if s.HP <=0:
            print('zostales pokonany przez owocka. przegrywasz.')
            break
def walka_z_bagiennym_potworem()->None:
    przeciwnik = p.potwor_bagien()
    print(f'pojawil sie przeciwnik: {przeciwnik[0]} hp: {przeciwnik[1]} atk: {przeciwnik[2]}')
    while True:
        atk = a.ataki()
        obrazenia = atk()
        przeciwnik[1] -= obrazenia
        print(f'zadales {obrazenia} obrazen przeciwnikowi. Zostalo mu {przeciwnik[1]} hp')
        if przeciwnik[1]<=0:
            print(f'pokonales przeciwnika {przeciwnik[0]}')
            s.EXP += 150
            s.GOLD += 100
            print(f'zdobywasz 150 exp i 100 golda. masz teraz {s.EXP} exp i {s.GOLD} golda.')
            break
        s.HP -= przeciwnik[2]*(1-s.DEF/100)
        print(f'przeciwnik zaatakowal i zadaje ci {przeciwnik[2]*(1-s.DEF/100)} obrazen. zostalo ci {s.HP} hp')
        if s.HP <=0:
            print('zostales pokonany przez potwora bagien. przegrywasz.')
            break
def walka_z_jaskiniowym_potworem()->None:
    przeciwnik = p.jaskiniowy_potwor()
    print(f'pojawil sie przeciwnik: {przeciwnik[0]} hp: {przeciwnik[1]} atk: {przeciwnik[2]}')
    while True:
        atk = a.ataki()
        obrazenia = atk()
        przeciwnik[1] -= obrazenia
        print(f'zadales {obrazenia} obrazen przeciwnikowi. Zostalo mu {przeciwnik[1]} hp')
        if przeciwnik[1]<=0:
            print(f'pokonales przeciwnika {przeciwnik[0]}')
            s.EXP += 300
            s.GOLD += 150
            print(f'zdobywasz 300 exp i 150 golda. masz teraz {s.EXP} exp i {s.GOLD} golda.')
            break
        s.HP -= przeciwnik[2]*(1-s.DEF/100)
        print(f'przeciwnik zaatakowal i zadaje ci {przeciwnik[2]*(1-s.DEF/100)} obrazen. zostalo ci {s.HP} hp')
        if s.HP <=0:
            print('zostales pokonany przez jaskiniowego potwora. przegrywasz.')
            break
def walka_z_potworami_ruiny():
    przeciwnik = p.potwory_ruiny()
    print(f'pojawil sie przeciwnik: {przeciwnik[0]} hp: {przeciwnik[1]} atk: {przeciwnik[2]}')
    while True:
        atk = a.ataki()
        obrazenia = atk()
        przeciwnik[1] -= obrazenia
        print(f'zadales {obrazenia} obrazen przeciwnikowi. Zostalo mu {przeciwnik[1]} hp')
        if przeciwnik[1]<=0:
            print(f'pokonales przeciwnika {przeciwnik[0]}')
            s.EXP += 200
            s.GOLD += 120
            print(f'zdobywasz 200 exp i 120 golda. masz teraz {s.EXP} exp i {s.GOLD} golda.')
            break
        s.HP -= przeciwnik[2]*(1-s.DEF/100)
        print(f'przeciwnik zaatakowal i zadaje ci {przeciwnik[2]*(1-s.DEF/100)} obrazen. zostalo ci {s.HP} hp')
        if s.HP <=0:
            print('zostales pokonany przez potwora z ruin. przegrywasz.')
            break
def walka_z_bossem():
    boss = p.boss()
    print(f'pojawil sie boss: {boss[0]} hp: {boss[1]} atk: {boss[2]}')
    while True:
        atk = a.ataki()
        obrazenia = atk()
        boss[1] -= obrazenia
        print(f'zadales {obrazenia} obrazen bossowi. Zostalo mu {boss[1]} hp')
        if boss[1]<=0:
            print(f'pokonales bossa {boss[0]}')
            s.EXP += 10000
            s.GOLD += 500
            print(f'zdobywasz 10000 exp i 500 golda. masz teraz {s.EXP} exp i {s.GOLD} golda.')
            break
        s.HP -= boss[2]*(1-s.DEF/100)
        print(f'boss zaatakowal i zadaje ci {boss[2]*(1-s.DEF/100)} obrazen. zostalo ci {s.HP} hp')
        if s.HP <=0:
            print('zostales pokonany przez bossa. przegrywasz.')
            break