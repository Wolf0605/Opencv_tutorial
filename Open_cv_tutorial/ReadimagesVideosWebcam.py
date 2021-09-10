import cv2

frameWidth = 840
frameHeight = 680


#  ' ' -> 0   : WebCam
cap = cv2.VideoCapture('Resources/KakaoTalk_20200715_210347411.mp4')
# cap.set(3, frameWidth)
# cap.set(4,frameHeight)

# Caputre each frame video
while True:
    # if sucess, cap frame is save in img
    sucess, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("Video", img)

    # 1 -> Runs video by frame by frame
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
