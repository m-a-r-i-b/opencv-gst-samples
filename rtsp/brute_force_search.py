import cv2
from rtsp_credentials import USR, PASS,IP

usr = USR
pwd = PASS
ip = IP

# I took the url patterns and also included some variations, just to be sure...
urls = [
        f'rtsp://{usr}:{pwd}@{ip}/cam/realmonitor?channel=1&subtype=0',
        f'rtsp://{ip}/live=2.2&username={usr}&password={pwd}',
        f'rtsp://{usr}:{pwd}@{ip}',
        f'rtsp://{usr}:{pwd}@{ip}/1',
        f'rtsp://{usr}:{pwd}@{ip}/stream1',
        f'rtsp://{usr}:{pwd}@{ip}/Stream1',
        f'rtsp://{ip}/user={usr}&password={pwd}&channel=1&stream=0.sdp?',
        f'rtsp://{ip}/user={usr}&password={pwd}&channel=1&stream=0.sdp',#
        f'rtsp://{ip}/videostream.asf?user={usr}&pwd={pwd}',
        f'rtsp://{ip}/ucast/11',
        f'rtsp://{ip}/11',#
        f'rtsp://{ip}/12',#
        f'rtsp://{ip}/live0.264',
        f'rtsp://{ip}/mpeg4cif',
        f'rtsp://{ip}/user={usr}&password={pwd}&channel=1&stream=0.sdp?',
        f'rtsp://{ip}/user={usr}&password={pwd}&channel=1&stream=0.sdp',
        f'rtsp://{ip}/live1.264',
        f'rtsp://{ip}/cam1/h264',
        f'rtsp://{ip}/mpeg4cif',
        f'rtsp://{ip}/ucast/11',
        f'rtsp://{ip}/ROH/channel/11',
        f'rtsp://{ip}/user={usr}_password={pwd}_channel=1_stream=0.sdp',
        f'rtsp://{ip}/user={usr}&password={pwd}&channel=1&stream=0.sdp?',
        f'rtsp://{ip}/user={usr}_password={pwd}_channel=1_stream=0.sdp',
        f'rtsp://{ip}/user={usr}_password={pwd}_channel=1_stream=0.sdp?',
        f'rtsp://{ip}/cam1/mpeg4?user={usr}&pwd={pwd}',
        f'rtsp://{ip}/h264_stream',
        f'rtsp://{ip}/live/ch0',
        f'rtsp://{ip}/live/ch1',
        f'rtsp://{ip}/user={usr}&password={pwd}&channel=1&stream=0.sdp?',
        f'rtsp://{ip}/user={usr}&password={pwd}&channel=1&stream=1.sdp?',
        f'rtsp://{ip}/user={usr}&password={pwd}&channel=0&stream=1.sdp?',
        f'rtsp://{ip}/user={usr}&password={pwd}&channel=0&stream=0.sdp?',
        f'rtsp://{ip}/user={usr}&password={pwd}&channel=1&stream=0.sdp',
        f'rtsp://{ip}/user={usr}&password={pwd}&channel=1&stream=1.sdp',
        f'rtsp://{ip}/user={usr}&password={pwd}&channel=0&stream=1.sdp',
        f'rtsp://{ip}/user={usr}&password={pwd}&channel=0&stream=0.sdp',
        f'rtsp://{usr}:{pwd}@{ip}/ucast/11',
        f'rtsp://{usr}:{pwd}@{ip}/11',
        f'rtsp://{usr}:{pwd}@{ip}/12',
        f'rtsp://{usr}:{pwd}@{ip}/live0.264',
        f'rtsp://{usr}:{pwd}@{ip}/mpeg4cif',
        f'rtsp://{usr}:{pwd}@{ip}/live1.264',
        f'rtsp://{usr}:{pwd}@{ip}/cam1/h264',
        f'rtsp://{usr}:{pwd}@{ip}/mpeg4cif',
        f'rtsp://{usr}:{pwd}@{ip}/ucast/11',
        f'rtsp://{usr}:{pwd}@{ip}/ROH/channel/11',
        f'rtsp://{usr}:{pwd}@{ip}/h264_stream',
        f'rtsp://{usr}:{pwd}@{ip}/live/ch0',
        f'rtsp://{usr}:{pwd}@{ip}/live/ch1',
       ]



# I took the url patterns and also included some variations, just to be sure...
# urls = [f'rtsp://{usr}:{pwd}@{ip}:554/cam/realmonitor?channel=1&subtype=0',
#         f'rtsp://{ip}:554/live=2.2&username={usr}&password={pwd}',
#         f'rtsp://{usr}:{pwd}@{ip}:554/1',
#         f'rtsp://{usr}:{pwd}@{ip}:554/stream1',
#         f'rtsp://{usr}:{pwd}@{ip}:554/Stream1',
#         f'rtsp://{ip}:554/user={usr}&password={pwd}&channel=1&stream=0.sdp?',
#         f'rtsp://{ip}:554/user={usr}&password={pwd}&channel=1&stream=0.sdp',#
#         f'rtsp://{ip}:554/videostream.asf?user={usr}&pwd={pwd}',
#         f'rtsp://{ip}:554/ucast/11',
#         f'rtsp://{ip}:554/11',#
#         f'rtsp://{ip}:554/12',#
#         f'rtsp://{ip}:554/live0.264',
#         f'rtsp://{ip}:554/mpeg4cif',
#         f'rtsp://{ip}:554/user={usr}&password={pwd}&channel=1&stream=0.sdp?',
#         f'rtsp://{ip}:554/user={usr}&password={pwd}&channel=1&stream=0.sdp',
#         f'rtsp://{ip}:554/live1.264',
#         f'rtsp://{ip}:554/cam1/h264',
#         f'rtsp://{ip}:554/mpeg4cif',
#         f'rtsp://{ip}:554/ucast/11',
#         f'rtsp://{ip}:554/ROH/channel/11',
#         f'rtsp://{ip}:554/user={usr}_password={pwd}_channel=1_stream=0.sdp',
#         f'rtsp://{ip}:554/user={usr}&password={pwd}&channel=1&stream=0.sdp?',
#         f'rtsp://{ip}:554/user={usr}_password={pwd}_channel=1_stream=0.sdp',
#         f'rtsp://{ip}:554/user={usr}_password={pwd}_channel=1_stream=0.sdp?',
#         f'rtsp://{ip}:554/cam1/mpeg4?user={usr}&pwd={pwd}',
#         f'rtsp://{ip}:554/h264_stream',
#         f'rtsp://{ip}:554/live/ch0',
#         f'rtsp://{ip}:554/live/ch1',
#         f'rtsp://{ip}:554/user={usr}&password={pwd}&channel=1&stream=0.sdp?',
#         f'rtsp://{ip}:554/user={usr}&password={pwd}&channel=1&stream=1.sdp?',
#         f'rtsp://{ip}:554/user={usr}&password={pwd}&channel=0&stream=1.sdp?',
#         f'rtsp://{ip}:554/user={usr}&password={pwd}&channel=0&stream=0.sdp?',
#         f'rtsp://{ip}:554/user={usr}&password={pwd}&channel=1&stream=0.sdp',
#         f'rtsp://{ip}:554/user={usr}&password={pwd}&channel=1&stream=1.sdp',
#         f'rtsp://{ip}:554/user={usr}&password={pwd}&channel=0&stream=1.sdp',
#         f'rtsp://{ip}:554/user={usr}&password={pwd}&channel=0&stream=0.sdp',
#         f'rtsp://{usr}:{pwd}@{ip}:554/ucast/11',
#         f'rtsp://{usr}:{pwd}@{ip}:554/11',
#         f'rtsp://{usr}:{pwd}@{ip}:554/12',
#         f'rtsp://{usr}:{pwd}@{ip}:554/live0.264',
#         f'rtsp://{usr}:{pwd}@{ip}:554/mpeg4cif',
#         f'rtsp://{usr}:{pwd}@{ip}:554/live1.264',
#         f'rtsp://{usr}:{pwd}@{ip}:554/cam1/h264',
#         f'rtsp://{usr}:{pwd}@{ip}:554/mpeg4cif',
#         f'rtsp://{usr}:{pwd}@{ip}:554/ucast/11',
#         f'rtsp://{usr}:{pwd}@{ip}:554/ROH/channel/11',
#         f'rtsp://{usr}:{pwd}@{ip}:554/h264_stream',
#         f'rtsp://{usr}:{pwd}@{ip}:554/live/ch0',
#         f'rtsp://{usr}:{pwd}@{ip}:554/live/ch1',
#        ]


def test_url(url):
    # try to open the stream
    cap = cv2.VideoCapture(url)
    ret = cap.isOpened()  # if it was succesfully opened, that's the URL you need
    cap.release()
    return ret

# then you just need to check those URLs
workingUrls = []
for url in urls:
    if test_url(url):
        workingUrls.append(url)


print("working urls ----------- ")
print(workingUrls)