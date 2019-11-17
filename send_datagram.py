#	packet{
#		commands :{
#		timestamp : 0,
#		isteamyellow : False,
#		robot_commands: [{id:
#				
#				   id: 1
#   				 kickspeedx: 0.0
#   				 kickspeedz: 0.0
#   				 veltangent: 1.0
#   				 velnormal: 0.0
#   				 velangular: 0.0
#   				 spinner: false
#  				 wheelsspeed: false
#   				 wheel1: 0.0
# 			         wheel2: 0.0
#    				 wheel3: 0.0
#  				 wheel4: 0.0	
#
#				} , {...}]
#		}
#		replacment : {}
#
#	}
#
#	1- Create packet : p = grSim_Packet_pb2.grSim_Packet()
#	2- packet.commands.timestamp = 0
#	3- packet.commands.isteamyellow = 0
#	4- Create robot Commands : c = grSim_Commands_pb2.grSim_Robot_Command()
#	5- fill c.id ... c.wheel4
#	6- p.commands.robot_commands.append(c)
#	7- sock.sendto(p.SerializeToString(), (UDP_IP, UDP_PORT))
#packet.commands  = grSim_Commands_pb2.grSim_Commands()
import socket
#I have problem with importing from other file
import grSim_Packet_pb2
import grSim_Commands_pb2

UDP_IP = "127.0.0.1"
UDP_PORT = 20011

packet = grSim_Packet_pb2.grSim_Packet()

packet.commands.timestamp = 0
packet.commands.isteamyellow = 0

robots_commands = [];

robotcommand1 = grSim_Commands_pb2.grSim_Robot_Command()
robotcommand1.id = 1
robotcommand1.kickspeedx= 0.0
robotcommand1.kickspeedz= 0.0
robotcommand1.veltangent= 1.0 #x
robotcommand1.velnormal= 0.0 #y
robotcommand1.velangular= 0.0
robotcommand1.spinner= False
robotcommand1.wheelsspeed= False
robotcommand1.wheel1= 0.0
robotcommand1.wheel2= 0.0
robotcommand1.wheel3= 0.0
robotcommand1.wheel4= 0.0

robotcommand2 = grSim_Commands_pb2.grSim_Robot_Command()
robotcommand2.id = 4
robotcommand2.kickspeedx= 0.0
robotcommand2.kickspeedz= 0.0
robotcommand2.veltangent= 1.0
robotcommand2.velnormal= 0.0
robotcommand2.velangular= 0.0
robotcommand2.spinner= False
robotcommand2.wheelsspeed= False
robotcommand2.wheel1= 0.0
robotcommand2.wheel2= 0.0
robotcommand2.wheel3= 0.0
robotcommand2.wheel4= 0.0

packet.commands.robot_commands.append(robotcommand1)
packet.commands.robot_commands.append(robotcommand2)


# Internet
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.sendto(packet.SerializeToString(), (UDP_IP, UDP_PORT))
sock.close()
