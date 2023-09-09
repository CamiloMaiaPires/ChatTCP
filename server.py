import socket
import threading

def broadcast(sender, data):

    for clt in clients:
        if(clt != sender):
            clt.send(data)

def handleClient(client):

    #recebendo dados do cliente
    data = client.recv(5000)
    broadcast(client, data)


familia = socket.AF_INET #endereço da família ipv4 
tipo = socket.SOCK_STREAM #Protocolo TCP/IP

#criando o socket para o servidor
server = socket.socket(family=familia, type=tipo)
host = 'localhost'
porta = 5000
endereco = (host, porta)
#atribuindo o endereço ao socket
server.bind(endereco)

#numero maximo de clientes será dois
server.listen(2)
print('Esperando por conexão dos clientes')
clients = []
while True:
    
    #aceitando conexão
    client, addr = server.accept()
    for c in clients:
        msg = 'Cliente' + ' [' + addr[0] + ',' + str(addr[1]) + '] ' + 'entrou no chat'
        c.send(msg.encode('utf-8'))
    clients.append(client)
    print('Cliente' + ' [' + addr[0] + ',' + str(addr[1]) + '] ' + 'se conectou')

    thread = threading.Thread(target=handleClient, args=(clients[len(clients)-1],))
    thread.start()


