import turtle


def narysuj_liczbę(liczba):
    """
    Rysowanie liczby przy pomocy kresek.
    """
    DŁUGOŚĆ_KRESKI = 50
    DŁUGOŚĆ_ODSTĘPU = 20

    for k in range(liczba):
        turtle.left(90)    
        turtle.forward(DŁUGOŚĆ_KRESKI)
        turtle.up()
        turtle.back(DŁUGOŚĆ_KRESKI)
        turtle.right(90)
        turtle.forward(DŁUGOŚĆ_ODSTĘPU)
        turtle.down()
    

if __name__ == '__main__':
    
    turtle.shape('turtle')
    
    narysuj_liczbę(47)
    
    turtle.done()
    
