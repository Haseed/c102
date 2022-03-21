
from importlib.resources import open_binary
import cv2
import dropbox
import time
import random
start_time=time.time()

def takeScreenshot():
    # intializing open cv module
    # 0 represents camera permission
    randomNumber=random.randint(1,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        imageName="image"+ str(randomNumber)+".png"
        cv2.imwrite("C:/Users/asus/OneDrive/Desktop/whjr.classes/c102/",imageName)
        start_time=time.time
        result=False

    return imageName
    print("screenshot capture")
    # release the camera
    videoCaptureObject.release()        
    cv2.destroyAllWindows()
    

def uploadFiles(imageName):
    access_token="sl.BEMsnuzRnDVD4ewPYlh_QCtt9x67VzkxTHpjtW0gMUoUaDeZWu73xwcTUPvybsosUEY9T4oLaecWEvpV8d0LvuW4oDIbTWAOKH4Pa-IeyIfPWgNIWzKSamSyk4gjbIJszTbjUXzIh0cR"
    file=imageName
    sourcePath=file
    fileTo="/test"+(imageName)
    dbx=dropbox.Dropbox(access_token)


    with open(sourcePath,"rb")  as f :
        dbx.files_upload(f.read(),fileTo,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")


def main():
    while(True):
       if ((time.time() - start_time) >= 5):
            name=takeScreenshot()
            uploadFiles(name)
main()            
            
