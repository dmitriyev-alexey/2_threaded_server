import socket, threading

def scanner(ip, port):
	scan = socket.socket()

	try:
		connection = scan.connect((ip, port))
		print(f'Port ${port} is open!')
		connection.close()
	except:
		pass

ip = input('Enter an IP address to scan...')

for i in range(65536):
	thread = threading.Thread(target=scanner, args=(ip, i))
	thread.start()
