import socket
import os
# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and port
host = os.getenv('CLIENT_HOST')
port = int(os.getenv('CLIENT_PORT'))

# connect to the server
client_socket.connect((host, port))

# send a message to the server
message = "Hello, Server!"
client_socket.send(message.encode('utf-8'))

# receive the message from the server
data = client_socket.recv(1024).decode('utf-8')
print(f"Received data: {data}")

client_socket.close()
