import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('127.0.0.1', 3000)

while True:
    message = input('You: ').encode()
    s.sendto(message, server_address)
    response, _ = s.recvfrom(1024)
    print(f'Server: {response}')