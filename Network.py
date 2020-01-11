import socket
import struct

from Packet import Packet , SPacket
import pythonProto.grSim_Packet_pb2 as grSim_Packet_pb2
import pythonProto.grSim_Commands_pb2 as grSim_Commands_pb2

class Network:

	p = 0
	MCAST_GRP = '224.5.23.2'
	MCAST_PORT = 10020
	sock = 0
	UDP_IP = "127.0.0.1"
	UDP_PORT = 20011
	def __init__(self):
		

		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		sock.bind(('', self.MCAST_PORT))  # use MCAST_GRP instead of '' to listen only
		                     # to MCAST_GRP, not all groups on MCAST_PORT
		mreq = struct.pack("4sl", socket.inet_aton(self.MCAST_GRP), socket.INADDR_ANY)

		sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
		self.sock =sock
#def sendData():
	
	
	def recieveData(self):
		self.p = Packet(self.sock.recv(65536))
		self.p.add(self.sock.recv(65536))

	def update(self):
		self.p = Packet(self.sock.recv(65536))
		self.p.add(self.sock.recv(65536))

	def getPacket(self):
		return self.p

	def sendPacket(self ,data):
		packet = grSim_Packet_pb2.grSim_Packet()
		#print(data.to_string())
		packet.commands.timestamp = data.timestamp
		packet.commands.isteamyellow = data.isteamyellow

		for i in data.robots_commands :
			command = grSim_Commands_pb2.grSim_Robot_Command()
			command.id = i.robotID
			command.kickspeedx= i.kickspeedx
			command.kickspeedz= i.kickspeedz
			command.veltangent= i.veltangent
			command.velnormal= i.velnormal #y
			command.velangular= i.velangular
			command.spinner= i.spinner
			command.wheelsspeed= i.wheelsspeed
			command.wheel1= i.wheel1
			command.wheel2= i.wheel2
			command.wheel3= i.wheel3
			command.wheel4= i.wheel4
			packet.commands.robot_commands.append(command)


		self.sock.sendto(packet.SerializeToString(), (self.UDP_IP, self.UDP_PORT))



