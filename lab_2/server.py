import socket
import threading

from config import ADDRESS, FORMAT


clients = []


def handle(conn):
    while True:
        data = conn.recv(1024).decode(FORMAT)
        print(data)
        if not data:
            break
        for client in clients:
            client.send(data.encode(FORMAT))

    # close the connection
    conn.close()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(ADDRESS)
    s.listen()
    while True:
        conn, addr = s.accept()
        clients.append(conn)
        print('Connected by', addr)
        t = threading.Thread(target=handle, args=(conn,))
        t.start()
