import cv2
import os 
import numpy as nm

folder="OpenCV-Python//faces"

print(list(os.walk(folder)))

width=120
height=140

images=[]
labels=[]
names={}

counter=0

for root,sub,files in list(os.walk(folder)):
    for i in sub:
        names[counter]=i
        folderpath=os.path.join(folder,i)
        for file in os.listdir(folderpath):
            image=cv2.imread(os.path.join(folderpath,file),cv2.IMREAD_GRAYSCALE)
            images.append(image)
            labels.append(counter)
        counter=counter+1

labels=nm.array(labels)
images=nm.array(images) 

model=cv2.face.LBPHFaceRecognizer_create()
model.train(images,labels)
webcam=cv2.VideoCapture(0)
classifier=cv2.CascadeClassifier(r"C:\Users\ragha\OneDrive\Desktop\Jetlearn Python\OpenCv-Python\haarcascade_frontalface_default.xml")
while True:
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
            prediction=model.predict(resizedimage)
            cv2.putText(frame,prediction,(250,250),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),thickness=3)
            print(prediction)
    cv2.imshow("frame", frame)
    waitkey=cv2.waitKey(100)
    if waitkey==27:
        break
