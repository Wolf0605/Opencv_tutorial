import cv2

img = cv2.imread("Resources/Lenna.png")

# Popup images
cv2.imshow("Lenna", img)

cv2.waitKey(10000) # Hold images (0 = inf)