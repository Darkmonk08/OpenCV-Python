import cv2

pikachu=cv2.imread(r"C:\Users\ragha\OneDrive\Desktop\Jetlearn Python\OpenCv-Python\Images\pikachu.png",cv2.IMREAD_COLOR)

#drawing a line
cv2.line(pikachu,(20,20),(200,200),(0,0,0),9)
cv2.imshow("pikachu with line",pikachu)

#drawing a rectangle
cv2.rectangle(pikachu,(20,20),(200,200),(123,95,150),7,cv2.LINE_8)
cv2.imshow("pikachu with rectangle",pikachu)

#drawing a filled rectangle
cv2.rectangle(pikachu,(200,200),(380,380),(123,95,150),-17)
cv2.imshow("pikachu with filled rectangle",pikachu)

#drawing a circle
cv2.circle(pikachu,(200,80),15,(0,0,0),20)
cv2.imshow("pikachu with circle",pikachu)

#drawing a filled circle
cv2.circle(pikachu,(200,400),15,(0,0,0),-20)
cv2.imshow("pikachu with filled circle",pikachu)
cv2.waitKey(0)
