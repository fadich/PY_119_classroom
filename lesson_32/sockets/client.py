# Echo client program
import socket

HOST = "192.168.50.222"
PORT = 80


with socket.socket() as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', repr(data))
