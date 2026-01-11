import cv2

image1=cv2.imread(r"C:\Users\ragha\OneDrive\Desktop\Jetlearn Python\OpenCv-Python\Images\pikachu.png",cv2.IMREAD_COLOR)
print(image1)
cv2.imshow("Pikachu",image1)
cv2.waitKey(0)

image2=cv2.imread(r"C:\Users\ragha\OneDrive\Desktop\Jetlearn Python\OpenCv-Python\Images\pikachu.png",cv2.IMREAD_GRAYSCALE)
print(image2)
cv2.imshow("Pikachu",image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
returnvalue=cv2.imwrite(r"C:\Users\ragha\OneDrive\Desktop\Jetlearn Python\OpenCv-Python\Images\pikachu-GreyScale.png",image2)
print(returnvalue)

image3=cv2.imread(r"C:\Users\ragha\OneDrive\Desktop\Jetlearn Python\OpenCv-Python\Images\view1.jpg",cv2.IMREAD_COLOR)
image4=cv2.imread(r"C:\Users\ragha\OneDrive\Desktop\Jetlearn Python\OpenCv-Python\Images\view2.jpg",cv2.IMREAD_COLOR)

cv2.imshow("View1",image3)
cv2.imshow("View2",image4)
cv2.waitKey(0)

imageadd=cv2.add(image3,image4)
cv2.imshow("addition",imageadd)
cv2.waitKey(0)

imageadd2=cv2.addWeighted(image3,0.5,image4,0.3, 0)
cv2.imshow("addition",imageadd2)
cv2.waitKey(0)

imagesubtract=cv2.subtract(image3,image4)
cv2.imshow("Subtraction",imagesubtract)
cv2.waitKey(0)