from Pygame_Module import getKey,init
import cv2.cv2
from Robot_Streaming import Car
#___________________________________________________________________
# Directions pins
N1, N2, N3, N4 = 11, 13, 16, 18
# Enable pins
EnA, EnB = 32, 33
#_____________________________________________________________________
Cap = cv2.VideoCapture(0)
Cap.set(3,640)
Cap.set(4,480)
#---------------------------------------------------------------------

if __name__== '__main__':
    init()  # Init method
    Start_Car = Car(N1, N2, N3, N4, EnA, EnB)

    while True:
# --------------------------------Video Stream----------------------------------
        _, Img = Cap.read()
        cv2.imshow("Video: ", Img)
        # cv2.waitKey(1)
# ------------------------------------------------------------------------
        # key s + UP or Down Right and Left else
        if getKey('s'):
            if getKey('UP'): print("Forward");Start_Car.Forward()
            if getKey('DOWN'): print("DOWN");Start_Car.Backward()
            if getKey('RIGHT'): print("RIGHT");Start_Car.Right_Side()
            if getKey('LEFT'): print("LEFT");Start_Car.Left_Side()
            if getKey('c'):print("Quit");break # key [s + c] for quit
        else:
            print("Stop!!!");Start_Car.Stop_Car()
# ---------------------Note always click on pygame window-----------------
        # cv2.waitKey(1)

