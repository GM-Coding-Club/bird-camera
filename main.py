import os.path

import time

from conf import is_pi
from conf import tweeting

import firebasef
db = firebasef.rdb()
fs = firebasef.fs()

from twitter import tweet # Import basic twitter functions

if is_pi:
    from gpiozero import MotionSensor # Import motion sensor
    from picamera import PiCamera # Import pi camera

    try:
        pir = MotionSensor(4) # Instantiate motion sensor
    except gpio.exe.PinFixedPull:
        print('Error getting MotionSensor. Do you have it plugged into GPIO4?')

    camera = PiCamera()

def on_detection():
    if is_pi:
        camera.capture('./img.jpg')
    try:
        if (tweeting):
            tweet('I spotted: ', './img.jpg')
            print('Tweeted ./img.jpg with the caption: \'I spotted: \'')

        fname = (str(time.time()) + '.jpg')
        download_url = fs.add('images/' + fname, fname, './img.jpg')
        print ('Image download URL' + download_url)

        db.push('/spottings', {
            'image': download_url,
            'confirmed': False,
            'time': fname[:-4]
        })
    except IOError:
        print("./img.jpg cannot be parsed/detected; does the file exist & is it a jpg?")

if not is_pi:
    print("conf.py states that this platform isn't a pi... going into testing mode.")

# main run loop
while True:
    if is_pi:
        pir.wait_for_motion()
        # camera.start_preview()
        on_detection()
        pir.wait_for_no_motion()
        # camera.stop_preview()
    else:
        print('')
        p = raw_input("Press Enter to take a fake picture from ./img.png")
        on_detection()