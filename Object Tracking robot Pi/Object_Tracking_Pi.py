import cv2.cv2
from time import time
import Util
from Robot_Tracking import Car
# ---------------------------------------GPIO PIN setting ----------------------------------------
# Directions pins
N1, N2, N3, N4 = 11, 13, 16, 18
# Enable pins
EnA, EnB = 32, 33
Start_Car = Car(N1, N2, N3, N4, EnA, EnB) # create object of car class
# ---------------------------------------Initial -------------------------------------------------------
rect_size = 60 # for Center Rectangle Size
ptime = 0
deadzone = 100  # this is for to no shacking the Robot
tolerance = 0.1
cap, Ht, Wd, y_center, x_center = Util.Initial()  # also check with different pixel size
#-------------------------------------------------
while True:
    _, frame2 = cap.read()
    # ----------------------------------Flip The Frame-----------------------------------------------------
    frame2 = cv2.flip(frame2,0)
    frame2 = cv2.flip(frame2,-1) # use 1 instead of -1 for backward seting
# --------------------Masking Function-----------------------------------------------------
    red_mask, red = Util.Masking(frame2)
# ------------------------------------------Controllng-----------------------------------------------------
    # for this  sample set in Util module x_medium and y_medium
    if Util.x_medium < (Wd // 2) - deadzone:
        Util.Rectangle_Fill(frame2, Util.y_medium, Wd, Ht, 'Left')
        Util.Putting_Text(frame2, "Left")
        Start_Car.Left_Side()
    elif Util.x_medium > (Wd // 2) + deadzone:
        Util.Rectangle_Fill(frame2, Util.y_medium, Wd, Ht, 'Right')
        Util.Putting_Text(frame2, "Right")
        Start_Car.Right_Side()
    elif Util.y_medium < (Ht // 2) - deadzone:
        Util.Rectangle_Fill(frame2, Util.y_medium, Wd, Ht, 'Forward')
        Util.Putting_Text(frame2, "Forward")
        Start_Car.Forward()
    elif Util.y_medium > (Ht // 2) + deadzone:
        Util.Rectangle_Fill(frame2, Util.y_medium, Wd, Ht, 'Backward')
        Util.Putting_Text(frame2, "Backward")
        Start_Car.Backward()
    else:
        Util.Rectangle_Fill(frame2, Util.y_medium, Wd, Ht, 'Stop')
        Util.Putting_Text(frame2, "Stop")
        Start_Car.Stop_Car()

# ----------------------------------------Frame  Lines-----------------------------------------------------------------------
#     cv2.line(frame2, (x_center - 1, 0), (x_center + 1, Ht), (255, 255, 0), 3)
#     cv2.line(frame2, (0, y_center - 1), (Wd, y_center + 1), (255, 255, 0), 3)
                    # Vertical Lines
    cv2.line(frame2, (Wd//3,0), (Wd//3,Ht), (255, 255, 0), 3)
    cv2.line(frame2, (2*(Wd//3),0), (2*(Wd//3),Ht), (255, 255, 0), 3)
    #                 # Horizontal Lines
    cv2.line(frame2, (0,(Ht//3)), (Wd,(Ht//3)), (255, 255, 0), 3)
    cv2.line(frame2, (0,(Ht//3)*2), (Wd,(Ht//3)*2), (255, 255, 0), 3)
                    # Connected Line From Center to Object
    cv2.line(frame2, (x_center,y_center),(Util.x_medium,Util.y_medium), (0, 0, 0), 3)
    # cv2.rectangle(frame2,(x_center-rect_size,y_center-rect_size),(x_center+rect_size,y_center+rect_size),(0,0,255),3)
    # cv2.rectangle(frame2, (int(Wd / 2 - tolerance * Wd), int(Ht / 2 - tolerance * Ht)),(int(Wd / 2 + tolerance * Wd), int(Ht / 2 + tolerance * Ht)), (0, 255, 0), 2)
    cv2.circle(frame2, (x_center, y_center), 15, (0, 0, 0), -1)
# ------------------------------------Per Frame Second-----------------------------------------------------------
    ctime = time()
    fps = 1 / (ctime - ptime)
    ptime = ctime
    cv2.putText(frame2, f'FPS: {int(fps)}', (30, 60), cv2.FONT_HERSHEY_COMPLEX, 1, (55, 55, 233), 1)

# ------------------------------Contours Function----------------------------------------------------
    Util.getContours(frame2, red_mask)
# ----------------------------------------------------------------------------------------------------------
    cv2.imshow("Streaming", frame2)
    key = cv2.waitKey(1)
# ----------------------------------------------------------------------------
    if key == 27:
        print("Quit key", key)
        break

cv2.destroyAllWindows()
cap.release()
