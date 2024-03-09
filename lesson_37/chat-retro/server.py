import socket
import threading
from queue import Queue
from typing import List
import time


HOST = "127.0.0.1"
PORT = 8080
msg_queue = Queue()
connections: List[socket.socket] = []


def save_msg_to_queue(conn):
    while True:
        try:
            msg = conn.recv(1024)
        except ConnectionError as e:
            print("ConnectionError:", e)
            conn.close()
            connections.remove(conn)
            break

        except Exception as e:
            print("NO!: ", e)
        msg_queue.put(msg)


def read_and_send_message():
    while True:
        if msg_queue.empty():
            time.sleep(0.001)
            continue

        msg = msg_queue.get()
        for conn in connections:
            try:
                conn.sendall(msg)
            except ConnectionError as e:
                print("ConnectionError:", e)
                conn.close()
                connections.remove(conn)
            except Exception as e:
                print("Can not send a message:", e)


with socket.socket() as s:
    s.bind((HOST, PORT))
    s.listen(20)

    thr2 = threading.Thread(target=read_and_send_message, daemon=True)
    thr2.start()

    while True:
        conn, addr = s.accept()
        connections.append(conn)
        thr1 = threading.Thread(target=save_msg_to_queue, args=(conn, ), daemon=True)
        thr1.start()
