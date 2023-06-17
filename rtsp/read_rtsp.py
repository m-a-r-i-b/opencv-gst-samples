import cv2
import time
from rtsp_credentials import USR, PASS,IP

usr = USR
pwd = PASS
ip = IP


# Base 
# cap = cv2.VideoCapture('rtsp://USR:PASS@@ip')

# Channel
cap = cv2.VideoCapture(f'rtsp://{USR}:{PASS}@{IP}/cam/realmonitor?channel=2&subtype=0')

fps = cap.get(cv2.CAP_PROP_FPS)
width  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)   # float `width`
height  = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)   # float `width`

print(width,height,fps)

t1 = time.time()
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow("frame",frame)
        cv2.waitKey(1)
    else:
        break

# Release everything if job is finished
cap.release()