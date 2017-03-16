from gpiozero import MotionSensor
from picamera import PiCamera

camera = PiCamera()
pir = MotionSensor(4)
while True:
    pir.wait_for_motion()
    camera.start_preview()
    pir.wait_for_no_motion()
    camera.stop_preview()
