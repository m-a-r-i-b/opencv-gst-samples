import cv2


# cap = cv2.VideoCapture(2,cv2.CAP_V4L2)
# cap = cv2.VideoCapture(0,cv2.CAP_V4L2)


# ffmpeg -re -i samplevideo.mp4 -f mpegts "udp://127.0.0.1:2000"
# cap = cv2.VideoCapture('udpsrc port=1234 ! application/x-rtp,payload=96,encoding-name=H264 ! rtpjitterbuffer mode=1 ! rtph264depay ! h264parse ! decodebin ! videoconvert ! appsink')
# cap = cv2.VideoCapture('udp://127.0.0.1:1234')
# cap = cv2.VideoCapture('udp://127.0.0.1:1234',cv2.CAP_FFMPEG)
# cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('M','J','P','G'))


cap = cv2.VideoCapture('udp://127.0.0.1:1234')


while True:
    ret, frame = cap.read()
    if ret is True:
        
        cv2.imshow("frame_read",frame)
        cv2.waitKey(1)
    else:
        print("frame not found")