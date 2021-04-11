"""
Aim: Write a client-server program using UDP where the client sends a string to the server. The
server encrypts the string using rail fence algorithm and returns the result to the client. Client
displays the result

Server Program.
"""
import socket


def rail_fence_encrypt(plain_text, key=3):
    rail = [['\n' for i in range(len(plain_text))]
            for j in range(key)]

    dir_down = False
    row, col = 0, 0

    for i in range(len(plain_text)):
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down

        rail[row][col] = plain_text[i]
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    result = []
    for i in range(key):
        for j in range(len(plain_text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return "".join(result)


"""
Creating a socket object.
@:param AF_INET -> Specifies that we'll be using the IPv4 address family.
@:param SOCK_STREAM -> Specifies that we'll be suing a UDP socket.
"""
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket successfully created")

# Specify port number.
PORT = 8000
BUFFER_SIZE = 1024

"""
Associate the socket with a specific network interface and port number.
@:param -> (Host, Port) 
    Host -> The hosts from which connections can be accepted.
            '' is catch-all. Accepts all hosts.
    Port -> Port number to which the socket is bound to.
"""
s.bind(('', PORT))
print(f'Socket bound to {PORT}')

while True:
    """
    Reads any incoming message. UDP is connectionless. So the source address 
    returned by this function is used to send data back to the client.
    @:return message -> The message sent by the client.
    @:return add -> A tuple holding the address of the client.
    """
    message, addr = s.recvfrom(BUFFER_SIZE)
    print('Message received from', addr, ":", message)

    print('Encrypting...')
    cipher = rail_fence_encrypt(message.decode(), 4)
    print('Sending encrypted message back to client...')
    s.sendto(cipher.encode(), addr)
