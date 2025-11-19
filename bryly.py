import math
PI = math.pi

def pp_szescian(a:float)->float:
    return 6*a**2
def pp_prostopadloscian(a:float, b:float, c:float)->float:
    return (2*a*b)+(2*a*c)+(2*b*c)
def pp_graniastoslup(pp:float,pb:float)->float:
    return (2*pp)+pb
def pp_ostroslup(pp:float,pb:float)->float:
    return pp+pb
def pp_walec(r:float,H:float)->float:
    return (2*PI*r**2)+(2*PI*r*H)
def pp_stozek(r:float,l:float)->float:
    return (PI*r**2)+(PI*r*l)
def pp_kula(r:float)->float:
    return 4*PI*r**2
