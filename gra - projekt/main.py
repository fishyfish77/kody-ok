from funkcje import miejsca as m
def gra():
    while True:
        wybor = m.wybierz_miejsce()
        if wybor == 'las':
            m.las()
        elif wybor == 'jaskinia':
            m.jaskinia()
        elif wybor == 'miasto':
            m.miasto()
        elif wybor == 'rzeka':
            m.rzeka()
        elif wybor == 'ruiny':
            m.ruiny()
        elif wybor == 'tajemnicze miejsce':
            m.tajemnicze_miejsce()
        elif wybor == None: 
            print('brak wybory.')
            break
gra()