

from RPi.GPIO import setmode,setup,OUT,HIGH,LOW,PWM,setwarnings,output
from time import sleep


class Robot(object):
	def __init__(self):

		setmode(self.BORAD)
		setwarnings(False)

		# Directions pins
		self.N1, self.N2, self.N3, self.N4 = 11, 13, 16, 18
		# Enable pins
		self.EnA, self.EnB  = 32, 33

		setup(self.N1,self.OUT)
		setup(self.N2,self.OUT)
		setup(self.N3,self.OUT)
		setup(self.N4,self.OUT)
		setup(self.EnA,self.OUT)
		setup(self.EnB,self.OUT)

		# created object of PWM = pules Width modulation

		self.Enable_A = PWM(self.EnA,100)
		self.Enable_B = PWM(self.EnB,100)

		# Initial valule is 0

		self.Enable_A.start(0)
		self.Enable_B.start(0)

		self.speed = 15

	def Forward(self):
		self.output(self.N1,self.HIGH)
		self.output(self.N2,self.LOW)
		self.Enable_A.start(self.speed)

		self.output(self.N3,self.HIGH)
		self.output(self.N4,self.LOW)
		self.Enable_B.start(self.speed)

	def Backword(self):
		self.output(self.N1,self.LOW)
		self.output(self.N2,self.HIGH)
		self.Enable_A.start(self.speed)

		self.output(self.N3,self.LOW)
		self.output(self.N4,self.HIGH)
		self.Enable_B.start(self.speed)

	def Left_Moving(self):
		self.output(self.N1,self.HIGH)
		self.output(self.N2,self.LOW)
		self.Enable_A.start(self.speed)

		self.output(self.N3,self.LOW)
		self.output(self.N4,self.HIGH)
		self.Enable_B.start(self.speed)

	def Right_Moving(self):
		self.output(self.N1,self.LOW)
		self.output(self.N2,self.HIGH)
		self.Enable_A.start(self.speed)

		self.output(self.N3,self.HIGH)
		self.output(self.N4,self.LOW)
		self.Enable_B.start(self.speed)


Car = Robot()

while True:
	Choose = input("Enter: F B L R and Stop: S").upper()

	if Choose == 'F':
		print("Car Moving Forward")
		Car.Forward()
	elif Choose == 'B':
		print("Car Moving Backword")
		Car.Backword()
	elif Choose == 'L':
		print("Car Moving Left")
		Car.Left_Side()
	elif Choose == 'R':
		print("Car Moving Right")
		Car.Right_Side()
	elif Choose == 'S':
		print("Car Stopped or Brake")
		Car.Stop_Car()
	else:
		print("Invalid!!!!!")