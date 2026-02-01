import cv2
import numpy as nm

eyes=cv2.imread(r"C:\Users\ragha\OneDrive\Desktop\Jetlearn Python\OpenCv-Python\Images\pacman.png",cv2.IMREAD_COLOR)
greyscaleeyes=cv2.cvtColor(eyes,cv2.COLOR_BGR2GRAY)
blurredeyes=cv2.blur(greyscaleeyes,(15,15))
cv2.waitKey(0)
detectedcircles=cv2.HoughCircles(blurredeyes,cv2.HOUGH_GRADIENT,1,5,param1=60,param2=30,minRadius=10,maxRadius=40)
print(detectedcircles)

if detectedcircles is not None:
    nodecimal=nm.around(detectedcircles)
    print(nodecimal)
    circles=nm.uint(nodecimal)
    print(circles)
    print(circles[0])
    for x,y,r in circles[0]:
        cv2.circle(eyes,(x,y),r,(255,0,0),10)
    
cv2.imshow("eyes with circle",eyes)
cv2.waitKey(0)
