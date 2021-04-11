"""
Aim: Write a socket program to implement LZW compression

Server Program.
"""
import socket
from lzw_utils import decompress

print('\n************ Connection setup - Begin **************')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket successfully created")
PORT = 8080
BUFFER_SIZE = 1024
s.bind(('', PORT))
print(f'Socket bound to {PORT}')
s.listen(5)
print("socket is listening")

while True:
    c, addr = s.accept()
    print('Got connection from', addr)

    # send a thank you message to the client.
    c.send(b'Connection Established')
    print('************ Connection setup - End **************\n\n')

    """ Receive the bytestream of the compressed message from the client. """
    d = c.recv(BUFFER_SIZE)
    """ Decoding the bytes to integers. """
    decoded_message = [x for x in d]
    """ Decompress the message using the lzw algorithm. """
    decompressed_message = decompress(decoded_message)
    print('Message:')
    print(decompressed_message)

    # Close the connection with the client
    c.close()
    print(f'\nConnection with {addr} closed.')
