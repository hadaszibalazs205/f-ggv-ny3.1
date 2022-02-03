'''
3.1 Feladat
Írj egy programot, amely tartalmaz egy 'harommal_oszthatok' nevű függvényt, amely a paraméterként átvett listában megvizsgálja, hogy hány darab hárommal osztható szám van, és ezzel az értékkel tér vissza! 
A program tartalmazza a függvény hívását is!
'''

def harommal_oszthatok(x, y):
    lista = []
    parosak = []
    lista.append(x)
    lista.append(y)
    for i in lista:
        if i % 3 == 0:
            parosak.append(i)
    return len(parosak)
print(harommal_oszthatok(6, 9))