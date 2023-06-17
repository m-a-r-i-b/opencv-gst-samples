import cv2

VideoWriter = cv2.VideoWriter(
    """appsrc ! videoconvert ! {encoder} bitrate=2000 !
    rtph264pay ! udpsink host=127.0.0.1 port=5000""", 
    cv2.CAP_GSTREAMER, 0, 60, (1920,1080))