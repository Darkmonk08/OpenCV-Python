import cv2
import numpy as np

#resizing images
image1=cv2.imread(r"C:\Users\ragha\OneDrive\Desktop\Jetlearn Python\OpenCv-Python\Images\pikachu.png",cv2.IMREAD_COLOR)
imageA=cv2.imread(r"C:\Users\ragha\OneDrive\Desktop\Jetlearn Python\OpenCv-Python\Images\view1.jpg",cv2.IMREAD_COLOR)
cv2.imshow("Pikachu",image1)
image2=cv2.resize(image1,(418,250))
cv2.imshow("Shorter Pikachu",image2)

#changing color spaces
image3=cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Pikachu",image3)

#blurring image
image4=cv2.blur(image1,(15,15))
cv2.imshow("Blur Pikachu",image4)

#erosion
cv2.imshow("eroded pikachu",cv2.erode(image1,np.ones((15,15))))

#Border on Image
cv2.imshow("Pikachu Border",cv2.copyMakeBorder(image1,20,20,20,20,cv2.BORDER_CONSTANT,value=(255,0,0)))

#Border reflect
cv2.imshow("Pikachu Border",cv2.copyMakeBorder(image1,300,300,300,300,cv2.BORDER_REFLECT))

#Rotating an image
width,height,channel=image1.shape
matrix=cv2.getRotationMatrix2D((width/2,height/2),90,2)
cv2.imshow("Rotated Pikachu",cv2.warpAffine(image1,matrix,(width,height)))

#edge detection
cv2.imshow("Edge detection",cv2.Canny(imageA,20,40))
cv2.waitKey(0)
