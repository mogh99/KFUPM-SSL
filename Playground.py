
from ball import Ball
from Network import Network
from robot import Robot
from position import Position
from Packet import SPacket
from Commands import CMD
class Playground:
	ball = Ball(4 ,4)
	net = Network()
	robotYellow = []
	robotBlue = []

	coachYellow = "null"
	coachBlue = "null"

	def __init__(self):
		for i in range(7):
			self.robotBlue.append(Robot(i , Position(0,0)))

		for i in range(7):
			self.robotYellow.append(Robot(i , Position(0,0)))
		
		
	def update(self):
		# recive new packet
		self.net.update()
		p = self.net.getPacket()

		# update ball position 
		self.ball.x = p.info_ball.x
		self.ball.y = p.info_ball.y
		self.ball.z = p.info_ball.z

		# update Yellow team position and angle
		for i in p.info_robotY :
			self.robotYellow[i.id -1].position.x = i.x
			self.robotYellow[i.id -1].position.y = i.y
			self.robotYellow[i.id -1].orientation = i.orientation
		
		# update Blue team position and angle
		for i in p.info_robotB :
			self.robotBlue[i.id -1].position.x = i.x
			self.robotBlue[i.id -1].position.y = i.y
			self.robotBlue[i.id -1].orientation = i.orientation

		#### 
		#### <RemoveMe>
		# test sending command to robots
		# new command
		cmd = CMD()
		# command description for debugging
		cmd.des = "point1"

		cmd.wheelsspeed = False
		cmd.velocity(1,0,0)
		# if robot in  this position it do the command 
		# in this case the position of the command is the same as robot[0] so the robot will do this command
		cmd.point.x = self.robotYellow[0].position.x
		cmd.point.y = self.robotYellow[0].position.y
		# send this command to robot 0
		self.robotYellow[0].add_cmd(cmd)

		# we can give many commands to the robot and he will do it if he has the same position as the command
		cmd1 = CMD()
		cmd1.des = "point2"
		cmd1.wheelsspeed = False

		cmd1.velocity(0,0,1)
		cmd1.point.y = cmd.gety()
		cmd1.point.x = 0
		self.robotYellow[0].add_cmd(cmd1)
		####
		#### </RemoveMe>


		# the update command in Robot class will compare the robot position with each of the command in the robot command array
		# if they are "equal" then the robot will do the command 
		for i in self.robotYellow:
			i.update()

		for i in self.robotBlue:
			i.update()





		#####
		# DO AI
		#
		####



		# we send each team commands to the simulator so the robots will move after this block 
		# according to the protocol we send each team command packet alone
		next_command_Y = SPacket(0,1,self.robotYellow)
		self.net.sendPacket(next_command_Y)
		#print(next_command_Y.to_string())
		next_command_B = SPacket(0,0,self.robotBlue)
		self.net.sendPacket(next_command_B)
