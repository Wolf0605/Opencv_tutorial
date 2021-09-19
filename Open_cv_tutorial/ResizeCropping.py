import cv2

path = "Resources/road.jpg"
img = cv2.imread(path)
# print(img)
print(img.shape)
print(img.shape[1]) # width
print(img.shape[0]) # height
width ,height = 400 ,400
# width ,height
imgResize = cv2.resize(img, (width, height))
# print(imgResize.shape)

# img[ height, width ]
imgCropped = img[:, 430: 530]

# width, height
imgCropResize = cv2.resize(imgCropped, (img.shape[1], img.shape[0]))

cv2.imshow("road", img)
cv2.imshow("road2", imgResize)
cv2.imshow("road3", imgCropped)
cv2.imshow("road resize", imgCropResize)
cv2.waitKey(0)