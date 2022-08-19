from time import sleep
import mouse
from random import randint

mouse.move(-500,-500,absolute=True)

while True:
    x = randint(20,300)
    y = randint(20,300)

    mouse.move(x,y)
    print("mouse now at " + str(mouse.get_position()))
    sleep(45)