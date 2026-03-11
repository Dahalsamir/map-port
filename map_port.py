#!/usr/bin/pyython3
import sys
import socket

if len(sys.argv) == 1:
	print(f"{sys.argv[0]} IP START(optional)  END(optional)",file=sys.stderr)
	exit(1)

ip = sys.argv[1]
start=1
end=65535

if len(sys.argv) >= 3:
	start=int(sys.argv[2])
	if len(sys.argv) >= 4:
		end = int(sys.argv[3])

def Check_Port_Status(port:int) -> bool:
	try:
		s = socket.socket()
		s.settimeout(1)
		s.connect((ip,port))
		return True
	except (ConnectionRefusedError,socket.timeout):
		return False

for port in range(start,end):
	response = Check_Port_Status(port)
	if response:
		print(f"Open port is Found {port}")