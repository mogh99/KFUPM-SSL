import socket
import struct

from Packet import packet
class Network:

	p = 0
	MCAST_GRP = '224.5.23.2'
	MCAST_PORT = 10020
	sock = 0
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
		p = packet(sock.recv(65536))

	def update(self):
		self.p = packet(self.sock.recv(65536))
	def getPacket(self):
		return self.p