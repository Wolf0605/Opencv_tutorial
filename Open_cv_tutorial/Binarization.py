import cv2

def nothing(x):
    pass

# 이름이 Binary 인 window 창 만들고 trackbar 만들기
cv2.namedWindow('Binary')
cv2.createTrackbar('threshold', 'Binary', 0, 255, nothing)
# 초기값 설정
cv2.setTrackbarPos('threshold', 'Binary', 169)

img_color = cv2.imread("Resources/redball.jpg", cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
cv2.imshow("Redball", img_color)
cv2.imshow("Gray_Ball", img_gray)
cv2.waitKey(0)
while(True):
    # track bar의 현재값을 가져온다
    low = cv2.getTrackbarPos('threshold', 'Binary')
    ret, img_binary = cv2.threshold(img_gray, low, 255, cv2.THRESH_BINARY_INV)

    cv2.imshow("Binary", img_binary)

    img_result = cv2.bitwise_and(img_color, img_color, mask = img_binary)
    cv2.imshow('Result', img_result)
    if cv2.waitKey(1)&0xFF == 27:
        break
cv2.dstroyAllWindows()