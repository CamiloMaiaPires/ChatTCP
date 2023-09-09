import socket
import threading

def receiveMessage(client):

    while True:
        data = client.recv(5000).decode('utf-8')
        print(data)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 5000)
client.connect(server_address) 

thread = threading.Thread(target=receiveMessage, args=(client, ))

thread.start()

while True:
    message = input()
    client.sendall(message.encode('utf-8'))
    