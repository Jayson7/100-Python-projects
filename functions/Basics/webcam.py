import cv2
capt = cv2.VideoCapture(0)
if capt.isOpened():
    ret, frame = capt.read()
while True :
    ret, frame = capt.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
capt.release()