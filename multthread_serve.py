import socket, threading

HOST = "127.0.0.1"
PORT = 8080



class Access(threading.Thread):

    def __init__(self,clientAddress,clientSocket):
        threading.Thread.__init__(self)
        self.client_socket = clientSocket
        self.client_address = clientAddress
        print("Novo Client de: {}".format(clientAddress))


    def run(self):

        print("Conexao Enderenco: {}".format(self.client_address))
        messagem = None
        while True:
            data = self.client_socket.recv(2048)
            messagem = data.decode()
            
            if messagem == 'quit':
                print("GoodBye {}".format(self.client_address))
                self.client_socket.send(bytes("GoodBye",'UTF-8'))
                break
            else:
                print("Messagem to {} : {}".format(self.client_address,messagem))
                msg = "[Recebido]: {}".format(messagem)
                self.client_socket.send(bytes(msg,'UTF-8'))

        print("Client {} desconectou...".format(self.client_address))



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))

print("Servidor Iniciado")
print("Esperando request...")

while True:
    server.listen(1)
    clientSocket, clientAdd = server.accept()
    nthread = Access(clientAdd,clientSocket)
    nthread.start()

