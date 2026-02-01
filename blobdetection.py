import cv2
import numpy as np

blobs=cv2.imread(r"C:\Users\ragha\OneDrive\Desktop\Jetlearn Python\OpenCv-Python\Images\blobs.jpg",cv2.IMREAD_COLOR)
params=cv2.SimpleBlobDetector_Params()
params.filterByArea=True
params.minArea=50
params.filterByCircularity=True
params.minCircularity=0.9
params.filterByConvexity=True
params.minConvexity=0.9
params.filterByInertia=True
params.minInertiaRatio=0.7
numberofcircles=0

detector=cv2.SimpleBlobDetector_create(params)
circles=detector.detect(blobs)
print(circles)
numberofcircles=len(circles)
cv2.putText(blobs,str(numberofcircles),(100,40),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),thickness=2)
final_image=cv2.drawKeypoints(blobs,circles,np.zeros((1,1)),(0,0,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("detected blobs",final_image)
cv2.waitKey(0)
