from shutil import rmtree
from os import listdir,getcwd

# deleting the entire folder
def Delete_Video():
    if 'Video Folder' in listdir(getcwd()):
        rmtree('Video Folder')
        print("Deleted")
    else:
        print("There is no Video Folder")

if __name__ == "__main__":
    Delete_Video()