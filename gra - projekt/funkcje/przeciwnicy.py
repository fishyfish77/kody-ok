from random import choice
def losowi_przeciwnicy():
    #hp atk
    przeciwnicy = [
        ['japko', 100, 20],
        ['durian', 100, 19],
        ['pomarancza', 100, 18],
        ['ananas', 100, 17],
        ['mandarynka', 100 , 16],
        ['liczi', 100, 15]
    ]
    return choice(przeciwnicy)
def potwor_bagien():
    return ['niche meowl', 150, 25]
def jaskiniowy_potwor():
    return ['tim cheese', 250, 35]
def potwory_ruiny():
    potwory=[
        ['vex', 170, 30],
        ['zombiak', 150, 25],
        ['john pork', 200, 35],
        ['adam', 165, 20],
        ['ghost', 100, 15],
        ['twin', 250, 40]
    ]
    return choice(potwory)
def boss():
    return ['meowl.exe', 1000, 167]
