"""
Aim: Implement multi chat program using TCP or UDP in python.

Protocol used: TCP.

Group Chat Server Program.
"""
import socket
from _thread import *

# Constants
PORT = 3000
BUFFER_SIZE = 1024

# Setting up the server socket.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', PORT))

"""
Set the socket to Listening Mode. Since we are trying for a group chat, we should
keep a sufficiently high enough value for backlog.
@:param Backlog -> Max number of pending connections.
"""
s.listen(100)

print("Server running on port", PORT)

"""
Dictionary to store the details of the connected clients.
Expected format ->
{
    (HOST, PORT) : {
                        name: "Jyothis P",
                        socket: <socket object>
                    }
}
"""
connected_clients = {}


def client_connection_thread(client_socket, address):
    """
    Function to receive messages and send them off to be broad-casted to the rest.
    :param client_socket: socket object for the client.
    :param address: (Host, port) of the client.
    """
    client_socket.send(str.encode("Namaskaram."))

    while True:
        try:
            message = client_socket.recv(BUFFER_SIZE).decode("utf-8")
            if (not message) or message == '/q':
                message = f'{connected_clients[address]["name"]} has left the conversation.'
                print(message)
                broadcast(address, message)
                if address in connected_clients:
                    connected_clients.pop(address)
                return
            else:
                print(connected_clients[address]['name'], ':', message)
                broadcast(address, message)
        except Exception as e:
            return


def broadcast(sender_address, message, server_message=False):
    """
    Function to broadcast messages to all the clients in the client list, except
    for the sender. Also associates username with the messages.
    :param sender_address: (Host, Port) of the sender.
    :param message: Message to be broad-casted.
    :param server_message: Boolean value. Skips the username association part for the server messages.
    :return:
    """
    if not server_message:
        sender_name = connected_clients[sender_address]['name']
        message = sender_name + ': ' + message

    message = str.encode(message)
    for address in connected_clients:
        if address != sender_address:
            client = connected_clients[address]
            try:
                client['socket'].send(message)
            except:
                client['socket'].close()
                connected_clients.pop(address)


"""
Loop to keep listening for new connections.
"""
while True:
    conn, addr = s.accept()

    c_name = conn.recv(BUFFER_SIZE).decode("utf-8").title()

    client_data = {
        'socket': conn,
        'name': c_name
    }

    connected_clients[addr] = client_data

    print(c_name, 'connected.')
    broadcast(addr, f'{c_name} has entered the conversation.', server_message=True)

    """
    After receiving a new connections, starts a new thread to handle the connection
    using the client_connection_thread() function.
    """
    start_new_thread(client_connection_thread, (conn, addr))
