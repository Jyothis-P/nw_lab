"""
Aim: Write a socket program to implement single chat.

Chat Server Program.
"""
import socket
import sys

# Constants
PORT = 3000
BUFFER_SIZE = 1024
NAME = input("Enter your name. ")

# Setup Socket.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', PORT))
s.listen(5)

print("Server setup complete.")
print("Type 'okey bei' to exit chat.")

while True:
    c, addr = s.accept()
    print('New connection.', addr)

    # sending username to client.
    c.send(str.encode(NAME))

    c_name = c.recv(BUFFER_SIZE).decode("utf-8")
    print("Chatting with", c_name)
    c_name += ':'
    while True:
        try:
            msg_raw = input("You: ")
            msg = str.encode(msg_raw)
            c.send(msg)
            if msg == 'okey bei':
                break
            res = c.recv(BUFFER_SIZE).decode("utf-8")
            print(c_name, res)
            if res == 'okey bei':
                c.send(str.encode('okey bei'))
                break
        except:
            print("Closing connection.")
            break
    # Close the connection with the client
    print("End chat.")
    c.close()
