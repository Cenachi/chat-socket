import socket

PORTA = 2222

servidor = socket.socket()
servidor.bind(("", PORTA))
servidor.listen(5)

while True:
	cliente, endereco = servidor.accept()
	
	while True:
		mensagem = cliente.recv(1024)
		print("Cliente: ",mensagem.decode())
		mensagem = input("you:")
		cliente.send(mensagem.encode())
	
		
		# cliente.close()
