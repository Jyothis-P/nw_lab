"""
Aim: Write a socket program to implement LZW compression.

Client Program.
"""
import socket
from lzw_utils import compress

print('\n************ Connection setup - Begin **************')
s = socket.socket()
print("Socket successfully created")
PORT = 8080
HOST = '127.0.0.1'
BUFFER_SIZE = 1024
s.connect((HOST, PORT))
print("Connecting to server.")

# Print the data received from the server
print(s.recv(BUFFER_SIZE))
print('************ Connection setup - End **************\n\n')

message = '''Nory was a Catholic because her mother was a Catholic, and Norys mother was a Catholic because her father 
was a Catholic, and her father was a Catholic because his mother was a Catholic, or had been.'''

compressed_message = compress(message)
encoded_message = bytes(compressed_message)

print('Length of uncompressed message:', len(message.encode()))
print('Length of encoded compressed message:', len(encoded_message))
print(f'Compression percentage: {len(encoded_message) * 100 / len(message.encode())}%')

s.send(encoded_message)
print('Message sent to server.')

print("\nClosing the connection to the server.")
# close the connection
s.close()
