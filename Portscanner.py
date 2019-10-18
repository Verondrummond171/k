import socket



s = socket.socket(Socket.AF_INET,SOCKET.SOCK_STREAM)

host = "input(" enter the IP":)
port = int("input(enter port:")

def port scanner():
if s.connect_exc host,port()):
print("the port is open")
else:
print("the port is closed")
port scanner(port)
