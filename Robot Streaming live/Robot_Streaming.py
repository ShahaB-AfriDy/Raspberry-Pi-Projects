
from RPi.GPIO import setmode,setup,OUT,HIGH,LOW,PWM,setwarnings,output,BOARD
from time import sleep

class Car:
    def __init__(self,N1,N2,N3,N4,EnA,EnB):
        self.N1 = N1
        self.N2 = N2
        self.N3 = N3
        self.N4 = N4
        self.EnA = EnA
        self.EnB = EnB
        setmode(BOARD) # type setmode
        setwarnings(False)
        setup(self.N1,OUT)
        setup(self.N2,OUT)
        setup(self.N3,OUT)
        setup(self.N4,OUT)
        setup(self.EnA,OUT)
        setup(self.EnB,OUT)
    # created object of PWM = pules Width modulation
        self.Enable_A = PWM(self.EnA,100)
        self.Enable_B = PWM(self.EnB,100)
        # Initial valule is 0
        self.Enable_A.start(0)
        self.Enable_B.start(0)
        self.speed = 40

    def Forward(self):
        output(self.N1,HIGH)
        output(self.N2,LOW)
        self.Enable_A.start(self.speed)

        output(self.N3,HIGH)
        output(self.N4,LOW)
        self.Enable_B.start(self.speed)

    def Backward(self):
        output(self.N1,LOW)
        output(self.N2,HIGH)
        self.Enable_A.start(self.speed)

        output(self.N3,LOW)
        output(self.N4,HIGH)
        self.Enable_B.start(self.speed)

    def Left_Side(self):
        output(self.N1,HIGH)
        output(self.N2,LOW)
        self.Enable_A.start(self.speed)

        output(self.N3,LOW)
        output(self.N4,HIGH)
        self.Enable_B.start(self.speed)

    def Right_Side(self):
        output(self.N1,LOW)
        output(self.N2,HIGH)
        self.Enable_A.start(self.speed)

        output(self.N3,HIGH)
        output(self.N4,LOW)
        self.Enable_B.start(self.speed)

    def Stop_Car(self):
        output(self.N1,LOW)
        output(self.N2,LOW)
        self.Enable_A.stop()

        output(self.N3,LOW)
        output(self.N4,LOW)
        self.Enable_B.stop()


# this is for showcase for the code
if __name__ == '__main__':
    # Directions pins
    N1, N2, N3, N4 = 11, 13, 16, 18
    # Enable pins
    EnA, EnB = 32, 33
    startcar = Car(N1, N2, N3, N4, EnA, EnB)
    while True:
        Choose = input("Enter: F B L R and Stop: S").upper()
        if Choose == 'F':
            print("Car Moving Forward")
            startcar.Forward()
        elif Choose == 'B':
            print("Car Moving Backword")
            startcar.Backward()
        elif Choose == 'L':
            print("Car Moving Left")
            startcar.Left_Side()
        elif Choose == 'R':
            print("Car Moving Right")
            startcar.Right_Side()
        elif Choose == 'S':
            print("Car Stopped or Brake")
            startcar.Stop_Car()
        else:
            print("Invalid!!!!!")

