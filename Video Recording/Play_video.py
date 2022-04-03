import cv2.cv2 as cv2
from os import getcwd,listdir
def Video_Player():
    if "Video Folder" in listdir(getcwd()):

        Video_Files = listdir(getcwd()+'\\Video Folder') # return list of directories
        print(Video_Files)
        # playing the first one in the video folder
        VideoFile = getcwd()+"\\Video Folder"+'\\'+Video_Files[0]
        print(VideoFile)
        Video = cv2.VideoCapture(VideoFile) # playing the first one in the video folder
        while Video.isOpened():
            Flag,Image = Video.read()
            if Flag or cv2.waitKey(1) == 27:
                cv2.imshow('Video',Image)
                cv2.waitKey(50) # delay
            else:
                break
        Video.release()
        cv2.destroyAllWindows()
    else:
        print("Video Folder is empty!!!")

Video_Player()
