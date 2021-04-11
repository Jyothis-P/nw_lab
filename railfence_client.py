"""
Aim: Write a client-server program using UDP where the client sends a string to the server. The
server encrypts the string using rail fence algorithm and returns the result to the client. Client
displays the result

Client Program.
"""
import socket

"""
Creating a socket object.
@:param AF_INET -> Specifies that we'll be using the IPv4 address family.
@:param SOCK_STREAM -> Specifies that we'll be suing a UDP socket.
"""
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket successfully created")

# Specify the server's port number, host ip and Buffer size.
PORT = 8000
HOST = '127.0.0.1'
SERVER_ADDRESS = (HOST, PORT)
BUFFER_SIZE = 1024

"""
Sends data to the socket. The destination socket is specified by address. 
@:param data -> Data to be sent.
@:param address -> Address to which the data is to be sent.
"""
plaintext = input('Enter plaintext: ')
print("Sending to server...", end=" ")
s.sendto(plaintext.encode(), SERVER_ADDRESS)
print("Done.")

"""
Reads any incoming message. We don't require the address returned as we expect 
a response only from the server.
@:return message -> The message.
@:return add -> A tuple holding the address of the client.
"""
response, _ = s.recvfrom(BUFFER_SIZE)

print("Server says:", response)
