import cv2
import numpy as np

img = cv2.imread("Resources/bookcovers.jpg")

width, height = 250, 350

pts1 = np.float32([[45 ,38],[390, 8],[79, 526],[428, 497]])
pts2 = np.float32([[0,0], [width,0], [0, height], [width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)  # ??
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

# print(int(pts1[1][0]))
# print(type(pts1[1][1]))

for x in range(0,4):
    cv2.circle(img, (int(pts1[x][0]),int(pts1[x][1])), 5, (0,0,255), cv2.FILLED)


cv2.imshow("Original Image", img)
cv2.setMouseCallback("Original Image", mousePoints)
cv2.imshow("Output Image", imgOutput)
cv2.waitKey(0)