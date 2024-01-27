
#MACHINE 1
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind('192.168.1.4', 50005)
s.listen(5)
clientsocket,clientaddress = s.accept()
print(clientsocket)
msg=input("enter")
msg_encoded=msg.encode("utf-8")
clientsocket.send(msg_encoded)

#MACHINE 2
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 50005
sock.connect(('192.168.1.4', port))
msg=socket.recv(1024)
msg
msg_decoded = msg.decode("utf-8")
