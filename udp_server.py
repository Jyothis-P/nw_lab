"""
Aim: Write a socket program to implement client server programming using UDP

UDP Server Program.
"""
import socket

"""
Creating a socket object.
@:param AF_INET -> Specifies that we'll be using the IPv4 address family.
@:param SOCK_DGRAM -> Specifies that we'll be suing a UDP socket.
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

    """
    Sends message to the client using the address.
    """
    s.sendto(b'Received.', addr)
