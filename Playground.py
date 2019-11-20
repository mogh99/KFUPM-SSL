
from ball import Ball
from Network import Network
from robot import Robot
class Playground:
	robot1 = Ball(4 ,4)
	net = Network()
	robotYellow = []
	robotBlue = []

	coachYellow = "null"
	coachBlue = "null"

	def __init__(self):
		print("statr")
	def update(self):
		self.net.update()
		p = self.net.getPacket()
		print(p)
