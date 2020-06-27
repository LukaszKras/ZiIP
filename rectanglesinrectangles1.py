#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Program rysujący kwadraty wewnątrz kwadratów wewnątrz...

Rysowanie jest rozdzielone od obliczeń. Rysowanie polega po prostu na rysowaniu
wieloboków funkcją narysuj_wielobok(). Obliczanie gdzie są wierzchołki funkcją
oblicz_następny_wielobok().

Kwadrat jest wielobokiem. Wielobok w tym programie jest ciągiem - zapisywanym
jako lista punktów.Punkt jest - w tym programie - parą współrzędnych (x, y).  
Taka para współrzędnych daje się zapisać jako krotka.

CC-BY-NC-ND 2020 Sławomir Marczyński
"""

import turtle


def narysuj_wielobok(wielobok):
    n = len(wielobok)
    turtle.up()
    turtle.goto(wielobok[0])
    turtle.down()
    for i in range(1, n + 1):
        j = i % n
        turtle.goto(wielobok[j])
    
        
def oblicz_następny_wielobok(wielobok):
    n = len(wielobok)
    nowy_wielobok = []; 
    for i in range(n):
        j = (i + 1) % n
        x1, y1 = wielobok[i]
        x2, y2 = wielobok[j]
        środek_odcinka = (x1 + x2) / 2,  (y1 + y2) / 2
        nowy_wielobok.append(środek_odcinka)
    return nowy_wielobok
    

def narysuj_wieloboki(wielobok, liczba_wieloboków_do_narysowania):
    if liczba_wieloboków_do_narysowania > 0:
        narysuj_wielobok(wielobok)    
        nowy_wielobok = oblicz_następny_wielobok(wielobok)
        narysuj_wieloboki(nowy_wielobok, liczba_wieloboków_do_narysowania - 1)
        


if __name__ == '__main__':
   
    liczba_kwadratów = 25
    a = 550  # długość boku największego kwadratu
    kwadrat = [ (0, 0), (a, 0), (a, a), (0, a) ]
    narysuj_wieloboki(kwadrat, liczba_kwadratów)
    
    turtle.color('red')
    
    liczba_pięciokątów = 25
    bok = 350
    pięciokąt = [ (-bok, -bok), (bok/2, bok), (bok, bok/2),
                 (2*bok, bok*2), (2.5*bok, bok/1.5)]
    narysuj_wieloboki(pięciokąt, liczba_pięciokątów)

    turtle.done()
