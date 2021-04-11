import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 3001
HOST = '127.0.0.1'
BUFFER_SIZE = 1024

s.connect((HOST, PORT))
print('Connected to server')

while True:
    message = input('You: ')
    s.send(message.encode())
    if message == 'q':
        s.close()
        break
    response = s.recv(BUFFER_SIZE)
    print('Server:', response.decode('utf-8'))
