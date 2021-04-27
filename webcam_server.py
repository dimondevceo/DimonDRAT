from vidstream import StreamingServer

server = StreamingServer('0.0.0.0', 9999)
server.start_server()

while input("RUNNING > ") != 'STOP':
	continue

server.stop_server()