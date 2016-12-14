# Server
from socket import *
from threading import Thread
from os import system

clients = []


def clientHandler(conn, addr):
    global clients
    sender = addr[0]
    print(sender, "si è connesso")
    try:
        while True:
            data = c.recv(1024)
            data = data.decode('UTF-8')
            print(str(sender) + ":", data)
            if not data:
                break
            for client in clients:
                if addr != client:
                    c.sendto(data, client)
    except Exception as err:
        print(err)
        exit()

system("clear")
host = "192.168.1.232"
port = 5000
print ("Hostando server:\nIP:", host, " Porta:", port, "\n\n")
mysocket = socket(AF_INET, SOCK_STREAM)
mysocket.bind((host, port))
mysocket.listen(5)

trds = []
try:
    for i in range(5):
        c, addr = mysocket.accept()
        clients.append(addr)
        t = Thread(target=clientHandler, args=(c, addr))
        trds.append(t)
        t.start()
except Exception as err:
    print(err)

for t in trds:
    t.join()

system("clear")

print("Server aperto a: " + str(addr[0]))
while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    data = str(data)
    conn.send(data.encode())
conn.close()
