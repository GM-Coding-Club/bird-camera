from firebasef import rdb
db = rdb()

db.update('spottings/', ({
    'test': 'yay'
}))

from twitter import tweet # Import basic twitter functions
from gpiozero import MotionSensor # Import motion sensor
from picamera import PiCamera # Import pi camera

try:
    pir = MotionSensor(4) # Instantiate motion sensor
except gpio.exe.PinFixedPull:
    print('Error getting MotionSensor. Do you have it plugged into GPIO4?')

camera = PiCamera()

def on_detection():
    camera.capture('./img.jpg')
    tweet('I spotted: ', './img.jpg')

# main run loop
while True:
    pir.wait_for_motion()
    camera.start_preview()
    on_detection()
    pir.wait_for_no_motion()
    camera.stop_preview()