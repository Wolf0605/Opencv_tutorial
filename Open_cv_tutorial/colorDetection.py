import cv2
import numpy as np


frameWidth = 400
frameHeight = 680
cap = cv2.VideoCapture(1)
cap.set(3, frameWidth)
cap.set(4,frameHeight)

def empty(a):
    pass


# Makes track bars
cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 640, 240)
cv2.createTrackbar("HUE Min", "HSV", 0, 179, empty)
cv2.createTrackbar("HUE Max", "HSV", 179, 179, empty)
cv2.createTrackbar("SAT Min", "HSV", 0, 255, empty)
cv2.createTrackbar("SAT Max", "HSV", 255, 255, empty)
cv2.createTrackbar("VALUE Min", "HSV", 0, 255, empty)
cv2.createTrackbar("VALUE Max", "HSV", 255, 255, empty)


while True:
    # if sucess, cap frame is save in img
    _, img = cap.read()
    # It makes to dectect color more clearly
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("HUE Min", "HSV")
    h_max = cv2.getTrackbarPos("HUE Max", "HSV")
    s_min = cv2.getTrackbarPos("SAT Min", "HSV")
    s_max = cv2.getTrackbarPos("SAT Max", "HSV")
    v_min = cv2.getTrackbarPos("VALUE Min", "HSV")
    v_max = cv2.getTrackbarPos("VALUE Max", "HSV")
    print(h_min)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    # Give mask What is maks?
    mask = cv2.inRange(imgHsv, lower, upper)
    # Merge Mask and Original Image
    result = cv2.bitwise_and(img, img, mask = mask)

    mask = cv2.cvtColor(mask ,cv2.COLOR_GRAY2BGR)
    hstack = np.hstack([img, mask ,result])



    # cv2.imshow("Original", img)
    # cv2.imshow("HSV Color Space", imgHsv)
    # cv2.imshow("Mask", mask)
    # cv2.imshow("Result", result)
    cv2.imshow("Horizontal Stacking", hstack)
    # 1 -> Runs video by frame by frame
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.realease()
cap.destroyAllwindows()