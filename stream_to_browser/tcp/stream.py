import cv2

cap = cv2.VideoCapture('/dev/video0',cv2.CAP_V4L2)


# theoraenc ! oggmux

out = cv2.VideoWriter('appsrc ! videoconvert ! videoscale ! video/x-raw,width=320,height=240 \
        ! theoraenc ! oggmux ! tcpserversink host=127.0.0.1 port=8080',
                      0, 10, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        out.write(frame)
    else:
        break

# Release everything if job is finished
cap.release()
out.release()