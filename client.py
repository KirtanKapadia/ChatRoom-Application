import zmq

host = '127.0.0.1'
port = 6789
context = zmq.Context()
client = context.socket(zmq.REQ)
client.connect("tcp://{}:{}".format(host, port))
for num in range(1,6):
	request_str = "message #{}".format(num)
	request_bytes = request_str.encode('utf-8')
	client.send(request_bytes)
	reply_bytes = client.recv()
	reply_str = reply_bytes.decode('utf-8')
	print("Sent {}, received {}".format(request_str, reply_str))