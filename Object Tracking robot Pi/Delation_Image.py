import cv2.cv2
import numpy as np

frameWidth = 200
frameHeight = 200

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

def empty(a):
    pass

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",640,240)
cv2.createTrackbar("Threshold1","HSV",150,255,empty)
cv2.createTrackbar("Threshold2","HSV",150,255,empty)

def getCountours(Image,ImageContour):
    contours,hierarcy = cv2.findContours(Image,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    # cv2.drawContours(ImageContour,contours,-1,(0,255,255),4) for all contours in Frame
    for cont in contours:
        Area = cv2.contourArea(cont)
        if Area > 1000:
            cv2.drawContours(ImageContour, cont, -1, (0, 255, 255), 4)
            # x,y,w,h = cv2.boundingRect(cont)
            # cv2.putText(ImageContour,f'Area: {int(Area)}',(x+w,y+50),(33,22,255),2)


while True:

    _, Frame = cap.read()
    ImageContours =  Frame.copy()
    Blur_Image = cv2.GaussianBlur(Frame,(7,7),1)

    Gray_Image = cv2.cvtColor(Blur_Image,cv2.COLOR_BGR2GRAY)

    Threshold1 = cv2.getTrackbarPos("Threshold1", "HSV")
    Threshold2 = cv2.getTrackbarPos("Threshold2", "HSV")
    Canny_Image = cv2.Canny(Gray_Image,Threshold1,Threshold2)
    Kernal = np.ones((5,5))
    Dilate_Image = cv2.dilate(Canny_Image,Kernal,iterations=1)

    # hStack = np.hstack([Gray_Image,Blur_Image,Canny_Image])
    # cv2.imshow('Horizontal Stacking', hStack)
    getCountours(Dilate_Image,ImageContours)
    cv2.imshow("Frame", Frame)
    cv2.imshow("Blue Image", Blur_Image)
    cv2.imshow("Gray Image", Gray_Image)
    cv2.imshow("Canny Image",Canny_Image)
    cv2.imshow("Dilation Image",Dilate_Image)
    cv2.imshow("Image Contours", ImageContours)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()