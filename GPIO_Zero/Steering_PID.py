import pygame
from gpiozero import AngularServo
from time import sleep


def init():
    pygame.init()
    win = pygame.display.set_mode((200, 200))


def getKey(keyName):
    Flag = False
    for eveent in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        Flag = True
    pygame.display.update()
    return Flag



servo = AngularServo(13, min_angle=-45, max_angle=45) # 45-> 90 <-135

if __name__ == "__main__":
    init()
    while True:
        if getKey('LEFT'):
            servo.angle = -45
            servo.value = -0.5
            sleep(1)
        elif getKey('RIGHT'):
            servo.angle = 45
            servo.value = 0.5
            sleep(1)
        # if not press Left or Right key then it will be the mid position
        else:
            servo.angle = 0
            servo.value = 0  # or set the None
            sleep(1)
        if getKey('s') and getKey('c'):
            break
