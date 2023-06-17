import pyvirtualcam
import numpy as np
import os
import cv2

cap = cv2.VideoCapture('udp://127.0.0.1:1234')


# tcpdump -i lo -n udp port 1234



# modprobe v4l2loopback
# ls -1 /sys/devices/virtual/video4linux

# ,device='/dev/video2'

fmt = pyvirtualcam.PixelFormat.BGR

with pyvirtualcam.Camera(width=640, height=480, fps=30,device='/dev/video2',fmt=fmt) as cam:
    print(f'Using virtual camera: {cam.device}')
    
    # frame = np.zeros((cam.height, cam.width, 3), np.uint8)  # RGB

    while True:
        ret, frame = cap.read()
        # cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        # cv2.putText(frame, 'OpenCV', (50,50), cv2.FONT_HERSHEY_SIMPLEX, 
        #            2, (0,0,255), 5, cv2.LINE_AA)
        # frame[:] = cam.frames_sent % 255  # grayscale animation
        cam.send(frame)
        cam.sleep_until_next_frame()