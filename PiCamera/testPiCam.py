from picamera2 import Picamera2, Preview
import time
import subprocess
picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)
#picam2.start_preview(Preview.QTGL)
picam2.start()
time.sleep(2)
c = 100

while c:
    picam2.capture_file("test.jpg")
    subprocess.Popen("sh SendBack.sh", shell=True)
    time.sleep(0.5)
    c=c-1
