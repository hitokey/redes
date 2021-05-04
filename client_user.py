import socket

SERVER = "127.0.0.1"
PORT = 8080

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((SERVER,PORT))
client.sendall(bytes("Hello", 'UTF-8'))

while True:
    input_data = client.recv(1024)
    print("Connect Server Messagem : {}".format(input_data.decode()))
    output_data = input() #read keyboard
    client.sendall(bytes(output_data,'UTF-8'))
    if output_data == 'quit':
        break

client.close()
