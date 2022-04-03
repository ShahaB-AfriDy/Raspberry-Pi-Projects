import cv2
from numpy import array
x_medium = 0
y_medium = 0
y_deviation = 0
x_deviation = 0
def Initial(Width=1280,Height=720):
    cap = cv2.VideoCapture(0)
    # cap.set(3, Width)
    # cap.set(4, Height)
    _, frame = cap.read()
    cols, rows,ch = frame.shape
    # print(f'Row: {rows} Col: {cols}')
    return cap,cols,rows,int(cols/2),int(rows/2)


def getContours(Image,mask):
    global x_medium,y_medium,x_deviation,y_deviation
    contours_red, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    contours = sorted(contours_red, key=lambda x:cv2.contourArea(x), reverse=True)
    for cnt in contours:
        (x,y,w,h) = cv2.boundingRect(cnt)
        cv2.rectangle(Image, (x , y) , (x + w, y + h) , (0, 255, 0), 2)
        # x_medium = int((x + x + w) / 2) # another way int(x + (w/2))
        # y_medium = int((y + y + h) / 2) # another way int(y + (h/2))
        x_medium = int(x+(w/2))
        y_medium = int(y+(h/2))
        cv2.circle(Image, (x_medium, y_medium), 15, (250, 0, 0), -1)
        # print(f'x:  {x_medium} and y: {y_medium}')
        # cv2.circle(Image, (x+w,y+h), 15, (250, 255, 0), -1)

        x_diff = w-x
        y_diff = h-y
        obj_x_center = x + (x_diff / 2)
        obj_x_center = round(obj_x_center, 3)
        obj_y_center = y + (y_diff / 2)
        obj_y_center = round(obj_y_center, 3)
        # print("[",obj_x_center, obj_y_center,"]")
        x_deviation = round((640.5 - obj_x_center), 3)
        y_deviation = round((240.5 - obj_y_center), 3)
        # print("{", x_deviation*0.3, y_deviation*0.1, "}")
        break

def Masking(Image):
    hsv_frame2 = cv2.cvtColor(Image, cv2.COLOR_BGR2HSV)
    low_red = array([55, 175, 133])
    high_red = array([121, 255, 255])
    red_mask = cv2.inRange(hsv_frame2, low_red, high_red)
    red = cv2.bitwise_and(Image,Image, mask=red_mask)
    return red_mask,red

def Putting_Text(frame,Text):
    x,y = frame.shape[1],frame.shape[0]
    if Text == 'Stop':
        cv2.putText(frame, Text, ((x //2)-40, (y//2)-50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
    elif Text == "Right":
        cv2.putText(frame, Text, ((2*(x//3)+x)//2,(((y//3)+((y//3)*2)))//2), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
    elif Text == "Left":
        cv2.putText(frame, Text, ((x//3)//2,(((y//3)*2)+y//3)//2), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
    elif Text == "Forward":
        cv2.putText(frame, Text, ((((x//3)+((x//3)*2))//2)-50,(y//3)//2), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
    elif Text == "Backward":
        cv2.putText(frame, Text, ((((x//3)+(x//3)*2)//2)-50,((y//3)*2+(y))//2), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)

def Rectangle_Fill(frame2,y_medium,Wd,Ht,Side):
    if Side == 'Left':
        if y_medium < Ht // 3:
            cv2.rectangle(frame2, (0, 0), ((Wd // 3), (Ht // 3)), (160, 231, 125), -1)
        elif y_medium < (Ht // 3) * 2:
            cv2.rectangle(frame2, (0, (Ht // 3)), ((Wd // 3), (Ht // 3) * 2), (160, 231, 125), -1)
        else:
            cv2.rectangle(frame2, (0, (Ht // 3) * 2), ((Wd // 3), Ht), (160, 231, 125), -1)
    elif Side == 'Right':
        if y_medium < Ht//3:
            cv2.rectangle(frame2,((Wd//3)*2,0),(Wd,(Ht//3)),(160, 231, 125), -1)
        elif y_medium < (Ht // 3)*2:
            cv2.rectangle(frame2, ((Wd//3)*2,(Ht//3)),(Wd, (Ht // 3)*2), (160, 231, 125), -1)
        else:
            cv2.rectangle(frame2, ((Wd//3)*2, (Ht//3)*2), (Wd,Ht), (160, 231, 125), -1)
    elif Side == 'Forward':
        cv2.rectangle(frame2, ((Wd // 3), 0), ((Wd // 3) * 2, (Ht // 3)), (160, 231, 125), -1)
    elif Side == 'Backward':
        cv2.rectangle(frame2, ((Wd // 3), (Ht // 3) * 2), ((Wd // 3) * 2, Ht), (160, 231, 125), -1)
    else:
        cv2.rectangle(frame2, ((Wd // 3), (Ht // 3)), ((Wd // 3) * 2, (Ht // 3) * 2), (0, 0, 255), -1)