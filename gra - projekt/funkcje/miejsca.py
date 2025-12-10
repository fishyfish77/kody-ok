from random import randint
import time
from . import statystyki as s
from . import walka as w
def las():
    print('jestes w lesie. co chcesz zrobic?')
    print('1 - isc na polowanie / 2 - isc na zbieranie ziol / 3 - pojsc gleboko w las / 4 - odpoczynek')
    while True:
        inp = input().lower()
        if inp =='1':
            print('idziesz na polowanie.')
            time.sleep(2)
            print('znalazles zwierzynę i ja upolowales. dostajesz mieso oraz skore, ktore mozesz sprzedac w miescie.')
            s.inv.append('mieso')
            s.inv.append('skora')
            return 'polowanie'
        elif inp =='2':
            print('idziesz na zbieranie ziol.')
            time.sleep(2)
            print('znalazles kilka ziol, moga ci sie przydac do robienia mikstur')
            s.inv.append('ziola')
            return 'zbieranie ziol'
        elif inp =='3':
            print('idziesz gleboko w las.')
            time.sleep(2)
            print('zgubiles sie w lesie i natknales sie na potwora bagien. zostajesz przez niego zaatakowany.')
            w.walka_z_bagiennym_potworem()
            return 'gleboko w lesie'
        elif inp =='4':
            print('odpoczywasz w lesie.')
            time.sleep(2)
            s.HP += 10
            print(f'siedzac na duzym kamieniu niedaleko sciezki, odpoczywasz i odzyskujesz 10 hp. masz teraz {s.HP} hp.')
            return 'odpoczynek'
def jaskinia():
    print('jestes w jaskini. co chcesz zrobic?')
    print('1 - szukac skarbow / 2 - walka z potworem / 3 - odpoczynek')
    while True:
        inp = input().lower()
        if inp =='1':
            print('szukasz skarbow.')
            time.sleep(2)
            print('znalazles kilka ladnych kryształów, które możesz sprzedać w mieście.')
            s.inv.append('krysztaly')
            return 'eksploracja'
        elif inp =='2':
            print('przechodzisz do walki z jaskiniowym potworem.')
            w.walka_z_jaskiniowym_potworem
            time.sleep(2)
            return 'walka z jaskiniowym potworem'
        elif inp =='3':
            print('odpoczywasz w jaskini.')
            time.sleep(2)
            s.HP += 10
            print(f'przygladajac sie skalistym scianom jaskini, odpoczywasz i odzyskujesz 10 hp. masz teraz {s.HP} hp.')
            return 'odpoczynek'
def miasto():
    print('jestes w miescie. co chcesz zrobic?')
    print('1 - sprzedac przedmioty / 2 - kupic mikstury / 3 - zrobic mikstury / 4 - odwiedzic kowala / 5 - odwiedzic tawerne')
    while True:
        inp = input().lower()
        if inp =='1' and len(s.inv)>2 and s.EXP>=200:
            print('sprzedajesz przedmioty ze swojego ekwipunku.')
            time.sleep(2)
            sprzedane = []
            for item in s.inv:
                if item in ['mieso','skora','krysztaly','ryby']:
                    sprzedane.append(item)
                    s.GOLD += 20
            for item in sprzedane:
                s.inv.remove(item)
            print(f'sprzedales: {sprzedane} masz teraz {s.GOLD} golda.')
            return 'sprzedaz przedmiotow'
        elif inp =='2':
            print('kupujesz mikstury.')
            print('do wyboru masz: 1 - miksture zdrowia za 75 golda / 2 - miksture many za 75 golda / 3 - miksture obrony za 60 golda.')
            time.sleep(2)
            inp = input().lower()
            if inp == '1' and s.GOLD >= 75:
                s.GOLD -= 75
                s.HP += 50
                s.inv.append('mikstura zdrowia')
                print(f'kupiles miksture zdrowia. zostalo ci {s.GOLD} golda i odzyskujesz 50 hp,  dzieki czemu masz teraz {s.HP} hp.')
                return 'zakup mikstury zdrowia'
            elif inp == '2' and s.GOLD >= 75:
                s.GOLD -= 75
                s.MANA += 50
                s.inv.append('mikstura many')
                print(f'kupiles miksture many. zostalo ci {s.GOLD} golda i dostales +50 many, co rowna sie {s.MANA} many.')
                return 'zakup mikstury many'
            elif inp == '3' and s.GOLD >= 60:
                s.GOLD -= 60
                s.DEF += 10
                s.inv.append('mikstura obrony')
                print(f'kupiles miksture obrony. zostalo ci {s.GOLD} golda i dostales +20 obrony, co rowna sie {s.DEF} def.')
                return 'zakup mikstury obrony'
            else:
                print('nie masz wystarczajaco golda.')
                break
        elif inp =='3':
            print('robisz mikstury ze swoich ziol.')
            time.sleep(2)
            if 'ziola' in s.inv and s.EXP >=200:
                s.inv.remove('ziola')
                s.HP += 30
                s.inv.append('mikstura zdrowia')
                print('zrobiles miksture zdrowia ze swoich ziol i dodales ja do ekwipunku.')
                return 'robienie mikstur'
            else:
                print('nie masz wystarczajaco ziol.')
                break
        elif inp =='4':
            print('odwiedzasz kowala.')
            time.sleep(2)
            print('kowal oferuje ci luk za 100 golda i set zbroji za 200 golda. co chcesz kupic?')
            print('1 - kupic luk / 2 - kupic set zbroji / x - nic nie kupowac')
            inp = input().lower()
            if inp == '1' and s.GOLD >=100:
                s.GOLD -=100
                s.inv.append('luk')
                print(f'kupiles luk. zostalo ci {s.GOLD} golda.')
                return 'zakup luku'
            elif inp == '2' and s.GOLD >=200:
                s.GOLD -=200
                s.DEF +=30
                s.inv.append('set zbroji')
                print(f'kupiles set zbroji. zostalo ci {s.GOLD} golda i dostales +50 obrony, co rowna sie {s.DEF} def.')
                return 'zakup zbroji'
            else:
                print('nie masz wystarczajaco golda.')
                break
        elif inp =='5':
            print('odwiedzasz tawerne i odpoczywasz.')
            time.sleep(2)
            s.HP += 10
            print(f'odpoczywasz i odzyskujesz 10 hp. masz teraz {s.HP} hp.')
            return 'tawerna'
def rzeka():
    print('jestes nad rzeka. co chcesz robc?')
    print('1 - lowic ryby / 2 - kapac sie / 3 - zrobic tratwe i poleciec z pradem rzekki')
    while True:
        inp = input().lower()
        if inp =='1':
            print('lowisz ryby.')
            time.sleep(2)
            print('zlowiles kilka ryb, ktore mozesz sprzedac w miescie.')
            s.inv.append('ryby')
            return 'lowienie ryb'
        elif inp =='2':
            print('kapiesz sie w rzece.')
            time.sleep(2)
            s.HP += 10
            print(f'kapiesz sie w zimnej rzece, co orzezwia twoje ciało. odzyskujesz 10 hp. masz teraz {s.HP} hp.')
            return 'kapiel'
        elif inp =='3':
            print('budujesz tratwe i odplywasz z pradem rzeki.')
            time.sleep(2)
            print(f'poplynales na drugi koniec swiata. brawo {s.NAME}!')
            break
def ruiny():
    print('wchodzac do ruin, czujesz dziwna energie. gdzie idziesz?')
    print('1 - prosto, jest to mroczna droga, ktora wydaje sie nie miec konca / 2 - prawo, widzisz lekki odblask swiatla w oddali / 3 - lewo, widac tam biblioteke z starozytnymi ksiazkami')
    while True:
        inp = input().lower()
        if inp == '1':
            print('idziesz prosto w mroczna droge.')
            time.sleep(2)
            print('zgubiles sie w ciemnosciach ruin i natknales sie na horde potworow. zostajesz przez nich zaatakowany.')
            w.walka_z_potworami_ruiny()
            return 'mroczna droga'
        elif inp == '2':
            print('idziesz w strone swiatla.')
            time.sleep(2)
            i = randint(0,300)
            s.GOLD += i
            if i>150:
                print(f'gratulacje {s.NAME}! znalazles wielka skrzynie!')
            else:
                print(f'niestety, {s.NAME}, skrzynia okazala sie byc mala :(')
            print(f'zdobywasz {i} golda.')
            print(f'masz teraz {s.GOLD} golda.')
            return 'skrzynia ze skarbem'
        elif inp == '3':
            print('idziesz do biblioteki.')
            time.sleep(2)
            print('znalazles starozytne ksiazki pelne wiedzy o maggii, o ktorej istnieniu nikt inny nie mial pojecia.')
            s.MANA += 40
            s.inv.append('starpzytne ksiazki')
            print(f'dzieki nim twoja mana wzrosla o 40 pkt i teraz masz {s.MANA} many.')
            return 'biblioteka'
def tajemnicze_miejsce():
    print('wchodzisz do tajemniczego miejsca, gdzie po srodku widzisz duze drzwi, ktore wymagaja kodu do otwarcia. co robisz?')
    print('1 - probujesz otworzyc drzwi / 2 - wracasz spowrotem')
    while True:
        inp = input().lower()
        if inp == '1':
            print('probojesz otwizyc drzwi.')
            time.sleep(2)
            kod = input('podaj kod:')
            i = randint(1000,9999)
            if kod == i:
                print(f'kod jest poprawny, brawo {s.NAME}!! drzwi sie otwieraja i widzisz w srodku ogromnego potwora, czekajacego na ciebie.')
                w.walka_z_bossem()
                return 'walka z bossem'
            else:
                print('kod jest nniepoprawny. drzwi pozostaja zamkniete.')
                continue
        elif inp == '2':
            print('wracasz spowrotem, przeczuwajac niebezpieczenstwo za sekretnymi drzwiaami.')
            time.sleep(2)
            return 'powrot'
def wybierz_miejsce():
    print('wybierz miejsce do ktorego chcesz sie teraz udac:')
    while True:
        print('1 - las / 2 - jaskinia / 3 - miasto / 4 - rzeka / 5 - ruiny / 6 - ??? / x - wyjdz')
        inp = input().lower()
        if inp =='1':
            print('udajesz sie do lasu')
            return 'las'
        elif inp =='2':
            print('udajesz sie do jaskini')
            return 'jaskinia'
        elif inp =='3':
            print('udajesz sie do miasta')
            return 'miasto'
        elif inp =='4':
            print('udajesz sie nad rzeke')
            return 'rzeka'
        elif inp =='5':
            if s.EXP <500:
                print('nie masz wystarczajaco exp, aby odwiedzic ruiny. potrzebujesz minimum 500 exp.')
                continue
            else:
                print('udajesz sie do ruin')
                return 'ruiny'
        elif inp =='6':
            if s.EXP <1000:
                print('nie masz wystarczajaco exp, aby odwiedzic to miejsce. potrzebujesz minimum 1000 exp.')
                continue
            else:
                print('udajesz sie do tajemniczego miejsca')
                return 'tajemnicze miejsce'
        elif inp =='x':
            return None