import random
import turtle

turtle.shape('turtle')

for i in range(100):
    a =  random.randrange(1, 3, 1)
    b = random.randrange(1, 3, 1)
    if a==1:
     
        turtle.left(90)
    
    turtle.forward(10)
    
    
    if b==2:
        turtle.left(270)
        turtle.forward(10)
turtle.done()
