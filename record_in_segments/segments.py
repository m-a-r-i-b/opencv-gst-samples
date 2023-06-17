import cv2

cap = cv2.VideoCapture('/dev/video0',cv2.CAP_V4L2)

out = cv2.VideoWriter('appsrc ! videoconvert ! x264enc tune=zerolatency ! '
                      'mpegtsmux ! hlssink location=./segment-%05d.ts '
                      'playlist-location=./index.m3u8 max-files=2 target-duration=3',
                      0, 30, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        out.write(frame)
    else:
        break

# Release everything if job is finished
cap.release()
out.release()