import socket

HOST = "192.168.50.222"
PORT = 80
with socket.socket() as s:
    s.bind((HOST, PORT))
    s.listen(1)

    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data)
            conn.sendall(
                b"""HTTP/1.1 404 Not Found
Date: Sun, 18 Oct 2012 10:36:20 GMT
Server: Apache/2.2.14 (Win32)
Content-Length: 230
Connection: Closed
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html>
<head>
   <title>HELLO GANDALF</title>
</head>
<body>
   <h1>HELLO GANDALF</h1>
   <p>The requested URL /t.html was not found on this server.</p>
</body>
</html>"""
            )
            break
