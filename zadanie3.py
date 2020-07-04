from turtle import goto, up, down, shape, done 
''' 
z grafiki żółwia zaciągamy współrzędne, podnoszenie i opuszczanie pióra,  
kształt i zakończenie
'''
from random import choice    # z funckji random zaciągamy moduł wyboru

ilość_kroków = 100000     # jest to ilość kroków jaką pokona zółw

skala = 20     # przeskalowanie kroku +-1 na piksele

odwiedzone = {}

(x, y) = (0, 0) # początek układu współrzędnych 
up()
goto(x * skala, y * skala) # poruszanie o 20 pikseli względem osi x i y
down()

for k in range(ilość_kroków):
    for j in range(100):
        (dx, dy)  = choice([(-1, 0), (1, 0), 
                           (0, 1), (0, -1)])
        '''
        żółw porusza się w losowo wybranym kierunku 
        '''
        nowe_miejsce = (x + dx, y + dy)
        
        # print(k, j, nowe_miejsce)
                        
        if nowe_miejsce not in odwiedzone:
            odwiedzone[nowe_miejsce] = 0
            
        if odwiedzone[nowe_miejsce] < 3: 
            odwiedzone[nowe_miejsce] += 1
            x, y = nowe_miejsce
            goto(x * skala, y * skala)           
        '''
        zółw trzykrotnie może odwiedzić to samo miejsce, jeśli odwiedzi je
        czwarty raz to się zatrzyma.
        '''
        break
    else:
        break
        
done() # zakończenie programu 