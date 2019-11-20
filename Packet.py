import pythonProto.messages_robocup_ssl_wrapper_pb2 as wrapper


from info import InfoBall , InfoRobot

class packet:
	"""docstring for packet"""
	info_ball  = InfoBall(0,0,0,0)
	info_robotY = []
	info_robotB = []
	def __init__(self, binary ):
		parser =  wrapper.SSL_WrapperPacket()
		parser.ParseFromString(binary)

		if parser.detection.IsInitialized():
			self.frame_number =  parser.detection.frame_number
			self.frame_number = parser.detection.t_capture
			self.frame_number = parser.detection.t_sent
			self.frame_number = parser.detection.camera_id
			for i in parser.detection.balls:
				self.info_ball = InfoBall(i.confidence , i.x , i.y , i.z)
			for i in parser.detection.robots_yellow:
				self.info_robotY.append(InfoRobot(i.robot_id , i.confidence , i.x , i.y , i.orientation) )
			for i in parser.detection.robots_blue:
				self.info_robotB.append(InfoRobot(i.robot_id , i.confidence , i.x , i.y , i.orientation) )

		#print (parser.detection)
			pass
		if parser.geometry.IsInitialized():
			print (parser.geometry)
		pass
		print ("************")

		
		def to_string(self):
			robot_y_str = ""
			for i in info_robotY :
				
			str = "ball_info {}"
		