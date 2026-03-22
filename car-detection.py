import cv2
import numpy as np

classifier=cv2.CascadeClassifier(r"C:\Users\ragha\OneDrive\Desktop\Jetlearn Python\OpenCv-Python\cars.xml")
video=cv2.VideoCapture(r"C:\Users\ragha\OneDrive\Desktop\Jetlearn Python\OpenCv-Python\car-video.avi")
caramnt=0

while True:
    status,frame=video.read()
    if not status:
        continue
    cars=classifier.detectMultiScale(frame,1.2,2)
    caramnt=len(cars)
    for x,y,w,h in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),4)
        image=frame[y:y+h,x:x+w]
    cv2.putText(frame,str(caramnt),(20,20),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),thickness=3)
    cv2.imshow("feed",frame)
    waitkey=cv2.waitKey(100)
    if waitkey==27:
        break