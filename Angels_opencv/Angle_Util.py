import cv2.cv2
from  numpy import  array
x_medium = 0
y_medium = 0
def Draw_Line(Frame):
    y,x,_ = Frame.shape
    cv2.cv2.line(Frame,(x//2,0),(x//2,y),(0,255,0),3)

def Masking(Image):
    hsv_frame2 = cv2.cvtColor(Image, cv2.COLOR_BGR2HSV)
    # for yellow ball HSV values
    low_red = array([71,51,209])
    high_red  = array([172,255,255])
    # low_red = array([55, 175, 133])
    # high_red = array([121, 255, 255])
    red_mask = cv2.inRange(hsv_frame2, low_red, high_red)
    red = cv2.bitwise_and(Image,Image, mask=red_mask)
    return red_mask,red

def getContours(Image,mask):
    global x_medium,y_medium
    contours_red, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    contours = sorted(contours_red, key=lambda x:cv2.contourArea(x), reverse=True)
    # if cv2.cv2.contourArea(contours) > 2000:...
    for cnt in contours:
        (x,y,w,h) = cv2.boundingRect(cnt)
        cv2.rectangle(Image, (x , y) , (x + w, y + h) , (0, 255, 0), 2)
        x_medium = int((x + x + w) / 2) # another way int(x + (w/2))
        y_medium = int((y + y + h) / 2) # another way int(y + (h/2))
        cv2.circle(Image, (x_medium, y_medium), 15, (250, 0, 0), -1)
        # print(f'x:  {x_medium} and y: {y_medium}')
        break



