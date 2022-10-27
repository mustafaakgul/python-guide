
import socket
from datetime import datetime

HOST = "192.168.1.37"
PORT = 6789
maxsize=1024

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST,PORT))

print(datetime.now())
print("waitng")

sock.listen(5)
client, addr=sock.accept()

while True:
    data=client.recv(maxsize)
    print(datetime.now(), addr, "said", data.decode("utf-8"))
    messagetoclient=input("enter")
    messagetoclient_encoded=messagetoclient.encode("utf-8")
    client.send(messagetoclient_encoded)
client.close()
sock.close()
