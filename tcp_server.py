"""
Aim: Write a socket program to implement client server programming using TCP

TCP Server Program.
"""
import socket

"""
Creating a socket object.
@:param AF_INET -> Specifies that we'll be using the IPv4 address family.
@:param SOCK_STREAM -> Specifies that we'll be suing a TCP socket.
"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket successfully created")

# Specify port number.
PORT = 8080
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

"""
Set the socket to Listening Mode.
@:param Backlog -> Max number of pending connections.
"""
s.listen(5)
print("socket is listening")

while True:
    """
    Waits for an incoming connection.
    @:return c -> A socket object representing the connection.
    @:return add -> A tuple holding the address of the client.
    """
    c, addr = s.accept()
    print('Got connection from', addr)

    # send a thank you message to the client.
    c.send(b'Connection Established')

    d = c.recv(BUFFER_SIZE)
    print(d)
    a = int.from_bytes(d, "big")
    print("Incoming message: " + str(a))
    c.send(b'Received A')
    b = int.from_bytes(c.recv(BUFFER_SIZE), "big")
    print("Incoming message: " + str(b))
    c.send(b'Received B')
    message = bytes([a + b])
    print("Sending message: " + str(message))
    # print(f'Sending message: {message} | {a+b}')
    c.send(message)
    print(f'Connection with {addr} closed.')

    # Close the connection with the client
    c.close()
