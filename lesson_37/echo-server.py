import socket


HOST = "127.0.0.1"
PORT = 8000


with socket.socket() as s:
    s.bind((HOST, PORT))
    s.listen(1)

    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)
        conn.sendall("Hello".encode())
        while True:
            while True:

                data = conn.recv(1024)
                if not data:
                    break
                print(data)
                conn.sendall(data)
                break
