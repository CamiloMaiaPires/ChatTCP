import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 5000)
client.connect(server_address) 

def receiveMessage(client):

    while True:
        data = client.recv(1024).decode('utf-8')
        print(data)

thread = threading.Thread(target=receiveMessage, args=(client, ))
thread.start()

while client:
    message = input()
    if message == 'quit()':
        client.sendall(message.encode('utf-8'))
        print("Voce se desconectou da sala {}".format(server_address))
        client.close()
    client.sendall(message.encode('utf-8'))