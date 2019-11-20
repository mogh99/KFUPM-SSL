
class InfoRobot:
	"""docstring for InfoRobot"""
	def __init__(self, Robot_id , confidence , x , y , orientation):
		self.id = Robot_id
		self.confidence = confidence
		self.x = x
		self.y = y
		self.orientation = orientation 


class InfoBall:
	"""docstring for InfoBall"""
	def __init__(self, confidence,x , y ,z):
		self.x = x
		self.y = y
		self.z = z
		self.confidence = confidence
