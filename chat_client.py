"""
Aim: Write a socket program to implement client server programming using TCP

Chat Client Program.
"""
import socket

# Specify the server's port number, host ip and Buffer size.
PORT = 3000
HOST = '127.0.0.1'
BUFFER_SIZE = 1024
NAME = input("Enter your name. ")

s = socket.socket()
s.connect((HOST, PORT))


s_name = s.recv(BUFFER_SIZE).decode("utf-8")
s.send(str.encode(NAME))

print("Chatting with", s_name)
print("Type 'okey bei' to exit chat.")
s_name += ':'

while True:
    try:
        res = s.recv(BUFFER_SIZE).decode("utf-8")
        print(s_name, res)
        if res == 'okey bei':
            s.send(str.encode('okey bei'))
            break
        msg_raw = input("You: ")
        msg = str.encode(msg_raw)
        s.send(msg)
        if msg == 'okey bei':
            break
    except:
        print("Closing connection.")
        break

print("Closing the connection to the server.")
# close the connection
s.close()
