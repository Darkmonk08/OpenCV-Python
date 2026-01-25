import cv2
import numpy as nm

eyes=cv2.imread(r"C:\Users\ragha\OneDrive\Desktop\Jetlearn Python\OpenCv-Python\Images\eyes.jpg",cv2.IMREAD_COLOR)
greyscaleeyes=cv2.imread(r"C:\Users\ragha\OneDrive\Desktop\Jetlearn Python\OpenCv-Python\Images\eyes.jpg",cv2.IMREAD_GRAYSCALE)
blurredeyes=cv2.blur(greyscaleeyes,(15,15))
cv2.waitKey(0)
detectedcircles=cv2.HoughCircles(blurredeyes,cv2.HOUGH_GRADIENT,1,10,param1=60,param2=30,minRadius=20,maxRadius=100)
print(detectedcircles)

if detectedcircles is not None:
    nodecimal=nm.around(detectedcircles)
    print(nodecimal)
    circles=nm.uint(nodecimal)
    print(circles)
    print(circles[0])