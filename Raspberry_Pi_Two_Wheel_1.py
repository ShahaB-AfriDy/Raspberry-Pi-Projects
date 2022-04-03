
from RPi.GPIO import setmode,setup,OUT,HIGH,LOW,PWM,setwarnings,output,BOARD
from time import sleep

setmode(BOARD)
setwarnings(False)

# Directions pins
N1, N2, N3, N4 = 11, 13, 16, 18
# Enable pins
EnA, EnB  = 32, 33

setup(N1,OUT)
setup(N2,OUT)
setup(N3,OUT)
setup(N4,OUT)
setup(EnA,OUT)
setup(EnB,OUT)

# created object of PWM = pules Width modulation

Enable_A = PWM(EnA,100)
Enable_B = PWM(EnB,100)

# Initial valule is 0

Enable_A.start(0)
Enable_B.start(0)
speed = 15

def Forward():
	output(N1,HIGH)
	output(N2,LOW)
	Enable_A.start(speed)

	output(N3,HIGH)
	output(N4,LOW)
	Enable_B.start(speed)

def Backword():
	output(N1,LOW)
	output(N2,HIGH)
	Enable_A.start(speed)

	output(N3,LOW)
	output(N4,HIGH)
	Enable_B.start(speed)

def Left_Side():
	output(N1,HIGH)
	output(N2,LOW)
	Enable_A.start(speed)

	output(N3,LOW)
	output(N4,HIGH)
	Enable_B.start(speed)

def Right_Side():
	output(N1,LOW)
	output(N2,HIGH)
	Enable_A.start(speed)

	output(N3,HIGH)
	output(N4,LOW)
	Enable_B.start(speed)

def Stop_Car():
	output(N1,LOW)
	output(N2,LOW)
	Enable_A.stop()

	output(N3,LOW)
	output(N4,LOW)
	Enable_B.stop()

if __name__ == '__main__':
	while True:
		Choose = input("Enter: F B L R and Stop: S").upper()

		if Choose == 'F':
			print("Car Moving Forward")
			Forward()
		elif Choose == 'B':
			print("Car Moving Backword")
			Backword()
		elif Choose == 'L':
			print("Car Moving Left")
			Left_Side()
		elif Choose == 'R':
			print("Car Moving Right")
			Right_Side()
		elif Choose == 'S':
			print("Car Stopped or Brake")
			Stop_Car()
		else:
			print("Invalid!!!!!")