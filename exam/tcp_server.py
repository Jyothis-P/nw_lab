import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 3001
BUFFER = 1024

s.bind(('', PORT))
s.listen(5)

print('Server up. Port:', PORT)

while True:
    connection, client_address = s.accept()
    print('Connected to ', client_address)
    while True:
        message = connection.recv(BUFFER)
        if message.decode('utf-8') == 'q':
            connection.close()
            break
        print(f'Client {client_address}: {message.decode("utf-8")}')
        connection.send(b'ACK')
    print('Connection terminated.')
