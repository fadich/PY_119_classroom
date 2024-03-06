import socket


HOST = "127.0.0.1"
PORT = 8080


with socket.socket() as s:
    s.connect((HOST, PORT))
    msg_bytes = input(">>> ").encode()
    s.sendall(msg_bytes)
    data = s.recv(1024)

print('Received', repr(data))
