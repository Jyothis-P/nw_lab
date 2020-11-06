"""
Aim: Implement multi chat program using TCP or UDP in python.

Protocol used: TCP.

Group Chat Client Program.
"""
import socket
from _thread import *

# Constants
PORT = 3000
HOST = '127.0.0.1'
BUFFER_SIZE = 1024

# Setting up the server.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((HOST, PORT))

"""
Sending the username of the client through to the server. Notice that we've called str.encode()
because the socket.send() function accepts a byte string.
"""
server.send(str.encode(input('Enter your name: ')))


def send_message():
    """
    Function that takes in input from STDIN and sends it through the socket to the server.
    """
    while True:
        try:
            msg_raw = input()
            message = str.encode(msg_raw)
            server.send(message)
            if msg_raw == '/q':
                raise Exception('aa')
        except Exception as e:
            print("Leaving Chat")
            server.close()
            return


"""
Calling the earlier function that handles the input on a separate thread. So essentially, 
we have messages to the server on one thread and messages from the server on a separate one.
This is important as both the input() and socket.recv() blocks and wait before going to the next line.
"""
start_new_thread(send_message, ())

"""
Receive and display messages as long as both the server and client are working.
"""
while True:
    try:
        incoming_message = server.recv(BUFFER_SIZE).decode("utf-8")
        print(incoming_message)
    except:
        break

server.close()
