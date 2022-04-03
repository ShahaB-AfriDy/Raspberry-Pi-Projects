import RPi.GPIO as GPIO
import time
# GPIO Pinstup
GPIO.setwarnings(False)
channel = 17
GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel,GPIO.IN)

def Call_Back(channel):
    if GPIO.input(channel):
        print("Sound Detected")
    else:
        print("Not Sound Detected")

GPIO.add_event_detect(channel,GPIO.BOTH,bouncetime=300) # let us know when the pen is high or low
GPIO.add_event_callback(channel,Call_Back)  # assign the gpio pen ,run the function on the change

while True:
    time.sleep(1)
