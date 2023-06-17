import cv2
import time

cap = cv2.VideoCapture('./firefly_bitrate_res_videos/640/4_640_7056.mp4')


out = cv2.VideoWriter('appsrc ! videoconvert ! nvh264enc bitrate=3000 ! h264parse ! qtmux ! filesink location=./firefly_bitrate_res_videos/640/4_640_.mp4',
                       cv2.CAP_GSTREAMER,0, 60, (640, 480))


# x264
# out = cv2.VideoWriter('appsrc ! videoconvert ! x264enc bitrate=3000 speed-preset=ultrafast ! h264parse ! qtmux ! filesink location=output_custombitrate_264.mp4',
#                        cv2.CAP_GSTREAMER,0, 30, (1920, 1080))

# x265
# out = cv2.VideoWriter('appsrc ! videoconvert ! x265enc bitrate=2500 speed-preset=ultrafast ! h265parse ! qtmux ! filesink location=output_custombitrate_265.mp4',
#                        cv2.CAP_GSTREAMER,0, 30, (1920, 1080))

t1 = time.time()
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        out.write(frame)
    else:
        break

t2 = time.time()
print("total time taken = ",t2-t1)
# Release everything if job is finished
cap.release()
out.release()