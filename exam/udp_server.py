import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
PORT = 3000
s.bind(('', PORT))
print(f'Server running. Port: {PORT}')

while True:
    message, client_address = s.recvfrom(1024)
    print(f'Message from {client_address}: {message.decode("utf-8") }')
    s.sendto(b'ACK', client_address)