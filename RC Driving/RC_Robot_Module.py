from RPi.GPIO import setmode, setup, OUT, HIGH, LOW, PWM, setwarnings, output, BOARD
from time import sleep
from gpiozero import AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory


class Car:
    def __init__(self, EnA, N1, N2, N3, N4, EnB, Servo_Pin, Speed=30, ):
        self.N1 = N1
        self.N2 = N2
        self.N3 = N3
        self.N4 = N4
        self.EnA = EnA
        self.EnB = EnB
        setmode(BOARD)  # type setmode
        setwarnings(False)
        setup(self.N1, OUT)
        setup(self.N2, OUT)
        setup(self.N3, OUT)
        setup(self.N4, OUT)
        setup(self.EnA, OUT)
        setup(self.EnB, OUT)
        # created object of PWM = pules Width modulation
        self.Enable_A = PWM(self.EnA, 100)
        self.Enable_B = PWM(self.EnB, 100)
        # Initial value is 0
        self.Enable_A.start(0)
        self.Enable_B.start(0)
        self.speed = Speed
        self.Pins_Factory = PiGPIOFactory()  # must run the "sudo pigpiod" commond before run the script
        self.Steering = AngularServo(Servo_Pin, initial_angle=0, min_pulse_width=0.5 / 1000, max_pulse_width=2.5 / 1000,
                                     pin_factory=self.Pins_Factory)
    def Forward(self, Angle):
        output(self.N1, HIGH)
        output(self.N2, LOW)
        self.Enable_A.start(self.speed)

        output(self.N3, HIGH)
        output(self.N4, LOW)
        self.Enable_B.start(self.speed)

        self.Steering.angle = Angle
        sleep(0.2)  # if not working as desire or create another module for that

    def Backward(self, Angle):
        output(self.N1, LOW)
        output(self.N2, HIGH)
        self.Enable_A.start(self.speed)

        output(self.N3, LOW)
        output(self.N4, HIGH)
        self.Enable_B.start(self.speed)

        self.Steering.angle = Angle
        sleep(0.2)  # if not working as desire or create another module for that

    def Left_Side(self, Angle):
        output(self.N1, HIGH)
        output(self.N2, LOW)
        self.Enable_A.start(self.speed)

        output(self.N3, LOW)
        output(self.N4, HIGH)
        self.Enable_B.start(self.speed)

        self.Steering.angle = Angle
        sleep(0.2)  # if not working as desire or create another module for that

    def Right_Side(self, Angle):
        output(self.N1, LOW)
        output(self.N2, HIGH)
        self.Enable_A.start(self.speed)

        output(self.N3, HIGH)
        output(self.N4, LOW)
        self.Enable_B.start(self.speed)

        self.Steering.angle = Angle
        sleep(0.2)  # if not working as desire or create another module for that

    def Stop_Car(self, Angle):
        output(self.N1, LOW)
        output(self.N2, LOW)
        self.Enable_A.stop()

        output(self.N3, LOW)
        output(self.N4, LOW)
        self.Enable_B.stop()

        self.Steering.angle = Angle
        sleep(0.2)  # if not working as desire or create another module for that
