from RC_Robot_Module import Car
from Key_Press_Module import init,getKey

# ---------------------------------------------------------
N1, N2, N3, N4 = 11, 13, 16, 18
EnA, EnB = 32, 36
Servo_PIN = 13 # on BCM
RC_Car = Car(EnA,N1, N2, N3, N4, EnB,Servo_PIN,Speed=30)
# ----------------------------------------------------------

try:
    init() # for pygame window and click on than window
    while True:
        # COMPLEX ORDER
        if getKey('UP') and getKey('LEFT'):
            Car.Forward(Angle=20)
            print("Slight Left")
        elif getKey('UP') and getKey('RIGHT'):
            Car.Forward(Angle=-20)
            print("Slight Right")

        # Simple order
        elif getKey('UP'):
            Car.Forward(Angle=0)
            print("Forward")
        elif getKey('DOWN'):
            Car.Backward(Angle=0)
            print("Backward")

        elif getKey('DOWN') and getKey('LEFT'):
            Car.Backward(Angle=-20)
            print("Left Backward")
        elif getKey('DOWN') and getKey('RIGHT'):
            Car.Backward(Angle=20)
            print("Right Backward")

        elif getKey('LEFT'):
            Car.Left_Side(Angle=-50)
            print("Left")
        elif getKey('RIGHT'):
            Car.Left_Side(Angle=45)
            print("Right")
        else:
            Car.Stop_Car(Angle=0)
            print("Stop")

        if getKey('s') and getKey('c'):
            print("Program Stopped")
            break
except KeyboardInterrupt:
    print("Canceled!!!")