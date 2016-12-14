import socket
from os import system
import time

system("clear")
print("##########\n##Thelema#\n##########")


host = socket.gethostname()
host_server = '0.0.0.0'
host_server = input("Inserire l'host del server: ")
port = 5000
s_client = socket.socket()
s_client.connect((host_server, port))
print("L'host del client: %s\nHost del server: %s\nPorta: %s" %
      (host, host_server, port))
while True:
    message = input("Messaggio: ")
    s_client.send(message.encode('UTF-8'))
s_client.close()
