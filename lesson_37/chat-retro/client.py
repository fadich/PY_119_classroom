import socket


HOST = "127.0.0.1"
PORT = 8080

with socket.socket() as s:
    s.connect((HOST, PORT))
    input_msg = input("your message: ") + "END!"
    s.sendall(input_msg.encode())
    resp = b""
    i = 0
    while True:
        resp += s.recv(1)
        i += 1
        if resp.endswith(b"END!"):
            print(resp)
            resp = b""
        # if resp is None:
        #     break
        # print(resp.decode())
