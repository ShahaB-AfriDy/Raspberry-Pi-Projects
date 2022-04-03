from gpiozero import Servo
s = Servo(17)  # note Pin only work BCM
mi = s.min() # measure the angle
mx = s.max() # measure the angle

# You should now be able to construct an AngularServo instance with
# the  correct bounds:

from gpiozero import AngularServo
s = AngularServo(17, min_angle=-42, max_angle=44)
s.angle = 0.0
print(s.angle)

s.angle = 15
print(s.angle)