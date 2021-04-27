from vidstream import CameraClient

client = CameraClient('127.0.0.1', 9999)
client.start_stream()

while True:
	continue

client.stop_stream()