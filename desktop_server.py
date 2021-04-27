from vidstream import StreamingServer

server = StreamingServer('0.0.0.0', 4444)
server.start_server()

while input("RUNNING > ") != 'STOP':
	continue

server.stop_server()