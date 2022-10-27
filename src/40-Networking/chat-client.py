
import socket
from datetime import datetime

HOST = "192.168.1.37"
PORT = 6789
maxsize=1024

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

while True:
    messageserver=input("enter")
    messageserver_encode=messageserver.encode("utf-8")
    s.send(messageserver_encode)
    data=s.recv(maxsize)
    print(data.decode("utf-8"))
s.close()