import cv2
import numpy as np
import Utils


kernel = np.ones((5,5), np.uint8)
print(kernel)

path = r'Resources/gp1.jpg'
img = cv2.imread(path)
# Convert img to Gray
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# Img Blur ( You can handle this scale )
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(imgBlur, 70,100)
imgDilation = cv2.dilate(imgCanny, kernel, iterations = 1)
imgEroded =cv2.erode(imgDilation, kernel, iterations=1)

StackedImages = Utils.stackimages(0.5, ([img, imgGray],
                                        [imgBlur, imgCanny]))

cv2.imshow("Stacked Imgaes", StackedImages)
# cv2.imshow("Lena", img)
# cv2.imshow("GrayScale", imgGray)
# cv2.imshow("Img Blur", imgBlur)
# cv2.imshow("imgCanny", imgCanny)
# cv2.imshow("Img Dialation", imgDilation)
# cv2.imshow("Img Erosion", imgEroded)
cv2.waitKey(0)