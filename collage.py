import cv2
import os 

folderpath=r"C:\Users\ragha\OneDrive\Desktop\Jetlearn Python\OpenCv-Python\images-collage"
print(os.listdir(folderpath))
imgwidth=700
imgheight=800
videoname=os.path.join(folderpath,"video.avi")
video=cv2.VideoWriter(videoname,0,1,(imgwidth,imgheight),)

for file in os.listdir(folderpath):
    if file.endswith(".png") or file.endswith(".jpeg") or file.endswith("jpg"):
        print(file)
        image=cv2.imread(os.path.join(folderpath,file),cv2.IMREAD_COLOR)
        image=cv2.resize(image,(imgwidth,imgheight))
        video.write(image)