import socket
import threading
from datetime import datetime

def broadcast(sender, data):
    hora = datetime.now()
    msg = hora.strftime('%d/%m/%Y %H:%M:%S ') + str(sender.getpeername()[1]) + ": " + data
    for clt in clients:
        if(clt != sender):
            try:
                clt.send(msg.encode('utf-8'))
            except:
                client.close()
                clients.remove(client)

def handleClient(client):
    #recebendo dados do cliente
    while True:
        try:
            data = client.recv(1024)
            if data.decode('utf-8') == 'quit()':
                desconexao = "Voce se desconectou da sala"
                client.send(desconexao.encode('utf-8'))
                print(str(client.getpeername()[1]) + " saiu da sala.")
                broadcast(client, str(client.getpeername()[1]) + " saiu da sala.")
                client.close()
                break
            else:
                data = data.decode('utf-8')
                broadcast(client, data)
        except:
            clients.remove(client)
            broadcast(client, f"{str(client.getpeername()[1])} saiu da sala.")
            client.close()
            break

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