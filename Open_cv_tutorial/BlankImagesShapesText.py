import cv2
import numpy as np

# np.uint8 -> [0. 0. 0.] -> [0 0 0]
img = np.zeros((512, 512, 3), np.uint8)

# 0 255
print(img)
# img[ :30, : 80 ] = 165, 100, 100

# from (0, 0) to (100, 100) color(0,255,0), thickness ( 10 )
cv2.line(img, (0,0), (img.shape[0],img.shape[1]),(0,255,0),2)
cv2.rectangle(img, (350,100), (450,200), (0,0,255),cv2.FILLED)
cv2.circle(img, (150, 400), 50, (255,0,0), cv2.FILLED)
# cv2.font... ,fontsize, color, thickness
cv2.putText(img, "Draw Shapes ", (75, 50), cv2.FONT_HERSHEY_COMPLEX,1.5,(255,255,255),3)

cv2.imshow("Image", img)

cv2.waitKey(0)