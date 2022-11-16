import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("192.168.2.113", 2222))

while True:

    msg = input("you:")

    cliente.send(msg.encode())

    mensagem = cliente.recv(1024)
    print("Servidor: ", mensagem.decode())

    # cliente.close()
