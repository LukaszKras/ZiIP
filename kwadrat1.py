import turtle
import random

turtle.shape('turtle')

a = ["red", "green", "blue"]

for i in range(8):
    #losowanie jednego z trzech kolorów
    turtle.fillcolor(a[0])
    turtle.begin_fill()





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
   
    liczba_kwadratów = 10
    a = 300  # długość boku największego kwadratu
    kwadrat = [ (0, 0), (a, 0), (a, a), (0, a) ]
    narysuj_wieloboki(kwadrat, liczba_kwadratów)
    
    turtle.done()