import Maath

####
# NOT COMPLETE
# NOT COMPLETE
# NOT COMPLETE
# NOT COMPLETE
# NOT COMPLETE
# NOT COMPLETE
# NOT COMPLETE
# NOT COMPLETE
# NOT COMPLETE

####

class AI:
	"""
		state 0  -> idle
		state 1  -> free
		state 2  -> ball with us
		state 3  -> ball with them

	"""
	def __init__(self):
		self.ball = 0
		self.team = []
		self.paths = []
		self.enemy = []
		self.state = 0
		self.needRethink = False

	def think(self):
		if(state == 0):
			pass
		else if(state == 1):
			robot = find_nearst_to_point(ball.position)
			cmd = generate_path_to()
			for i in cmd:
				robot.add_cmd(i)





	def find_nearst_to_point(self , point):
		min_dist = distance(self.team[0].position , point)
		robot = self.team[0]
		for i in team :
			d = distance(i.position , point)
			if(d < min_dist):
				min_dist = d
				index = i

		return index
