import cv2.cv2 as cv2
from os import mkdir,getcwd,listdir
from datetime import datetime
from time import time
def Video_Record():
    if "Video Folder" not in listdir(getcwd()):
        mkdir('Video Folder')

    Current_Path = getcwd()+"\\Video Folder"

    Time_Now = datetime.now()
    File_Name = Current_Path+'\\'+Time_Now.strftime('%H_%M_%S')+'.mp4'

    Video = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    OutPut = cv2.VideoWriter(File_Name, fourcc, 20.0, (640,  480))

    stime = time()
    while Video.isOpened():
        Flag, Image = Video.read()
        inTime = abs(stime - time())
        cv2.putText(Image,f'Seconds: {int(inTime)}',(30,100),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,55),2)
        cv2.imshow('Image',Image)
        OutPut.write(Image)
        if cv2.waitKey(1) == 27:
            print("Video Saved!!!")
            break

    # Release everything if job is finished
    Video.release()
    OutPut.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    Video_Record()