import pygame
import cv2

def init():
    pygame.init()
    win = pygame.display.set_mode((200,200))

def getKey(keyName):
    Flag = False
    for eveent in pygame.event.get():pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame,'K_{}'.format(keyName))
    if keyInput[myKey]:
        Flag = True
    pygame.display.update()
    return Flag

Cap = cv2.VideoCapture(0)
Cap.set(3,640)
Cap.set(4,480)


def Main():
    _,Img = Cap.read()
    cv2.imshow("Video: ",Img)
    # key S + UP or Down Right and Left else
    if getKey('s'):
        if getKey('UP'):print("Pressed UP")
        if getKey('DOWN'):print("Pressed: DOWN")
        if getKey('RIGHT'):print("Pressed: RIGHT")
        if getKey('LEFT'): print("Pressed: LEFT")
        # if getKey('c'):print("Quit!!!");break
    else:
        print("Stop!!!")
#     =====================Note always click on pygame window


# this is for Showcase the code
if __name__== '__main__':
    init()
    while True:
        Main()

