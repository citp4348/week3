import socket
import sys
import os

HOST, PORT = "192.168.1.101", 8000
data = " ".join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to server and send data
sock.connect((HOST, PORT))
sock.sendall(bytes(data + "\n", "utf-8"))

# Receive data from the server and shut down
received = str(sock.recv(1024), "utf-8")
#exec(received)
#os.system(received)
print("Sent:     {}".format(data))
print("Received: {}".format(received))
