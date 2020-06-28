import random
import turtle

turtle.shape('turtle')

for i in range(100):
    a = random.randint(1, 2)
    b = random.randint(1, 2)
    if a==1:

        turtle.left(90)

    turtle.forward(10)


    if b==2:
        turtle.left(270)
        turtle.forward(10)
turtle.done()
