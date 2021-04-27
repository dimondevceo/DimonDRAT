from vidstream import ScreenShareClient

client = ScreenShareClient('127.0.0.1', 4444)
client.start_stream()

while True:
	continue

client.stop_stream()