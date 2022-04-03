import cv2.cv2
from numpy import array
from time import  time
import Angle_Util as ut
Video = cv2.VideoCapture(0)
angle = 0
while Video.isOpened():
    Checker ,Frame = Video.read()
    Frame = cv2.cv2.flip(Frame,0)
    Frame = cv2.cv2.flip(Frame,1)

    red_mask ,red = ut.Masking(Frame)
    ut.getContours(Frame,red_mask)

    y,x,_ = Frame.shape
    if ut.x_medium > x//2:
        cv2.cv2.line(Frame, (x // 2, (y // 2) - 100), (ut.x_medium, (y//2)-100), (220, 0, 20), 2)
        cv2.cv2.line(Frame, (x // 2, (y // 2) + 150), (ut.x_medium, (y//2)-100), (0, 0, 200), 2)
        angle = 90-ut.x_medium*0.5
    elif ut.x_medium < x//2:
        cv2.cv2.line(Frame, (x // 2, (y // 2) - 100), (ut.x_medium, (y//2)-100), (220, 0, 20), 2)
        cv2.cv2.line(Frame, (x // 2, (y // 2) + 150), (ut.x_medium, (y//2)-100), (0, 0, 200), 2)
        angle = 180-ut.x_medium*0.5

    ut.Draw_Line(Frame)
    cv2.cv2.putText(Frame,f'X: {int(angle)}',(50,70),cv2.cv2.FONT_ITALIC,2,(0,0,144),2)
    cv2.cv2.circle(Frame, (ut.x_medium,(y//2)-100), 10, (255,255,255),-1)

    cv2.imshow("Video",Frame)

    if cv2.waitKey(1) == 27:
        break


Video.release()
cv2.destroyAllWindows()