import cv2
import sys

cap = cv2.VideoCapture(0)

if not(cap.isOpened()):
    print('didnt work :( ')

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)

while True:
    ret, frame = cap.read()  # capture frame by frame
    cv2.imshow('preview', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

