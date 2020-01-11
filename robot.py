import Maath
from Commands import CMD
from position import Position

class Robot:
	robotID = 0
	position = Position(0,0)
	orientation = 0
	kickspeedx=0  
	kickspeedz=0  
	veltangent=0  
	velnormal=0  
	velangular=0  
	spinner=0  
	wheelsspeed=0   
	wheel1 = 0
	wheel2 = 0
	wheel3 = 0
	wheel4 = 0
	commands = []

	def set_parameter(self, robotID, position):
		self.robotID = robotID
		self.position = position



	def __init__(self, robotID, position):
		self.robotID = robotID
		self.position = position
		self.commands = []




	def add_cmd(self , cmd):
		self.commands.append(cmd)
	
	def do_now(self , cmd):
		self.do_commad(cmd)


	def update(self):
		for i in self.commands :
			if(Maath.distance(i.point , self.position) < 1):
				print("id : {0} , des :{1} ({2},{3}) - ({4} ,{5})".format(self.robotID , i.des , i.point.x , i.point.y , self.position.x , self.position.y))
				print(Maath.distance(i.point , self.position))
				self.do_commad(i)

	
	def do_commad(self,cmd):
		self.wheelsspeed = cmd.wheelsspeed
		self.wheel1 = cmd.wheel1
		self.wheel2 = cmd.wheel2
		self.wheel3 = cmd.wheel3 
		self.wheel4 = cmd.wheel4
		self.veltangent = cmd.veltangent	
		self.velnormal = cmd.velnormal		
		self.velangular = cmd.velangular		
	
	def to_string(self):
		return "id:{0} , \n\tkickspeedx:{1} , \n\tkickspeedy:{2} , \n\tveltangent:{3} , \n\tvelnormal:{4} , \n\tvelangular:{5}, \n\tspinner:{6} , \n\twheelsspeed:{7} , \n\twheel1:{8} , \n\twheel2:{9} , \n\twheel3:{10} , \n\twheel4:{11}\n\n".format(self.robotID,self.kickspeedx,self.kickspeedz,self.veltangent,self.velnormal,self.velangular,self.spinner,self.wheelsspeed,self.wheel1,self.wheel2,self.wheel3,self.wheel4)
