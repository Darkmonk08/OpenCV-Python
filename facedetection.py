import cv2
import os 

folder="OpenCV-Python//faces"
subfolder="raghav"

path=os.path.join(folder,subfolder)
if not os.path.isdir(path):
    os.makedirs(path)
    print("hello world")

width=120
height=140

classifier=cv2.CascadeClassifier(r"C:\Users\ragha\OneDrive\Desktop\Jetlearn Python\OpenCv-Python\haarcascade_frontalface_default.xml")
webcam=cv2.VideoCapture(0)
picamnt=1
while picamnt<=40:
    print("hello")
    status,frame=webcam.read()
    if not status:
        continue
    gframe=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=classifier.detectMultiScale(gframe,1.3,4)
    print(faces)
    if len(faces)>0:
        for x,y,w,h in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),4)
            image=gframe[y:y+h,x:x+w]
            resizedimage=cv2.resize(image,(width,height))
            cv2.imwrite(os.path.join(path,f"{picamnt}.png"),resizedimage)
        picamnt=picamnt+1
    cv2.imshow("feed",frame)
    waitkey=cv2.waitKey(100)
    if waitkey==27:
        break
