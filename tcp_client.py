"""
Aim: Write a socket program to implement client server programming using TCP

TCP Client Program.
"""
import socket

a = 3
b = 4
print("A:", a, "B:", b)

# Create a socket object
s = socket.socket()

# Specify the server's port number, host ip and Buffer size.
PORT = 8080
HOST = '127.0.0.1'
BUFFER_SIZE = 1024

# Connect to the server.
s.connect((HOST, PORT))

# Print the data received from the server
print(s.recv(BUFFER_SIZE))


s.send(bytes([a]))
print("Message from the server:", s.recv(BUFFER_SIZE))
s.send(bytes([b]))
print("Message from the server:", s.recv(BUFFER_SIZE))
msg = s.recv(BUFFER_SIZE)
res = int.from_bytes(msg, "little")
print("Message from the server:", msg)
print("A + B =", res)

print("Closing the connection to the server.")
# close the connection
s.close()
