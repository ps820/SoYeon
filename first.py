import socket
import struct

first = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
first.bind(('127.0.0.1', 7700))
firstdata, addr = first.recvfrom(2000)

#second = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#second.bind(('127.0.0.1', 7800))

firstdata_upacked = struct.unpack('<2sffffffff3s', firstdata)
pos_x = firstdata_upacked[1]
pos_y = firstdata_upacked[2]
pos_z = firstdata_upacked[3]

print("data : ", firstdata)
print("pos_x : ", pos_x)
print("pos_y : ", pos_y)
print("pos_z : ", pos_z)
print("IP : ", addr[0])
print("Port : ", addr[1])
