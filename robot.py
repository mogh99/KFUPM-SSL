import position

class Robot:
	def __init__(self, robotID, position, velx, vely, wheel1, wheel2, wheel3, wheel4 ,commands):
		self.robotID = robotID
		self.position = position
		self.velx = velx
		self.wheel1 = wheel1
		self.wheel2 = wheel2
		self.wheel3 = wheel3
		self.wheel4 = wheel4
		self.newCommand = commands
	def setNewCommands(commands):
		self.newCommand = commands
	#def update(self):
		#do newcommands
