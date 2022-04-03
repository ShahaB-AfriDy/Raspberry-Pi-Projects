import cv2
from time import time
import Utils
rect_size =64 # for Center Rectangle Size
ptime = 0
deadzone = 100  # this is for to no shacking the Robot
tolerance = 0.1
cap, Ht, Wd, y_center, x_center = Utils.Initial()  # also check with different pixel size
#-------------------------------------------------
while True:
    _, frame2 = cap.read()
    # ----------------------------------Flip The Frame-----------------------------------------------------
    frame2 = cv2.flip(frame2,0)
    frame2 = cv2.flip(frame2,1)
# --------------------Masking Function-----------------------------------------------------
    red_mask, red = Utils.Masking(frame2)
# ------------------------------------------Controllng-----------------------------------------------------
#     if Utils.x_medium < (Wd // 2) - deadzone:...
#     elif Utils.x_medium > (Wd // 2) + deadzone:...
#     elif Utils.y_medium < (Ht // 2) - deadzone:...
#     elif Utils.y_medium > (Ht // 2) + deadzone:...




# ----------------------------------------Frame  Lines-----------------------------------------------------------------------
    cv2.line(frame2, (x_center, 0), (x_center, Ht), (255, 255, 0), 3)
    cv2.line(frame2, (0, y_center), (Wd, y_center), (255, 255, 0), 3)
                    # Connected Line From Center to Object
    cv2.line(frame2, (x_center,y_center),(Utils.x_medium,Utils.y_medium), (0, 0, 0), 3)
    # cv2.rectangle(frame2,(x_center-rect_size,y_center-rect_size),(x_center+rect_size,y_center+rect_size),(0,255,0),2)
    cv2.rectangle(frame2, (int(Wd / 2 - tolerance * Wd), int(Ht / 2 - tolerance * Ht)),(int(Wd / 2 + tolerance * Wd), int(Ht / 2 + tolerance * Ht)), (0, 255, 0), 2)
    # cv2.circle(frame2, (x_center, y_center), 15, (0, 0, 0), -1)
    # cv2.rectangle(frame2,(x_center-rect_size,y_center-rect_size+16),(x_center+rect_size,y_center+rect_size-16),(0,255,0),2)
    # print(f'x_c: {}')
    # print(f'xt: {(Wd / 2 - tolerance * Wd)}')
    cv2.circle(frame2,(int(Wd/2-tolerance*Wd),(int(Ht/2-tolerance*Ht)+int(Ht/2+tolerance*Ht))//2), 10, (0, 0, 0), -1)
    # print(f"x:{x_center-(Wd/2-tolerance*Wd)}")
    # print(f'xt: {Wd*tolerance}')
    # if Utils.x_medium > (Wd/2-Wd*tolerance) and Utils.y_medium > (Ht/2-Ht*tolerance):print("Stop")

# -------------------------------------------------------------------------------------------------------

    xt = (Utils.x_medium-Wd)*tolerance
    xt = round(0.5-xt/(Wd*0.1),3)
    yt = (Utils.y_medium-Ht)*tolerance
    yt = round(0.5-yt/(Ht*0.1),3)
    xt = round(1 - xt, 3)
    yt = round(1 - yt, 3)

    if (abs(xt) < tolerance and abs(yt) < tolerance):
        print("Shop!!!")
    else:
        if (abs(xt) > abs(yt)):
            if (xt >= tolerance):
                print("Move Left")
            if (xt <= -1 * tolerance):
                print("Move Right")
        else:

            if (yt >= tolerance):
                print("Move Forward")
            if (yt <= -1 * tolerance):
                print("Move Backward")

    cv2.rectangle(frame2, (0, Ht-45), (Wd,Ht), (0, 0, 0), -1)
    cv2.putText(frame2, f'tol: {tolerance}', (40, Ht - 13), cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 255, 0), 2)
    cv2.putText(frame2,f'x: {xt}',(200,Ht-13),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv2.putText(frame2, f'y: {yt}', (400, Ht - 13), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)


# ------------------------------Contours Function----------------------------------------------------
    Utils.getContours(frame2, red_mask)
# ----------------------------------------------------------------------------------------------------------
    cv2.imshow("Streaming", frame2)
    key = cv2.waitKey(1)
# ----------------------------------------------------------------------------
    if key == 27:
        print("Quit key", key)
        break

cv2.destroyAllWindows()
cap.release()
