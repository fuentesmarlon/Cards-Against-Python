import socket
import pickle
# host and port to sent data
HOST = '127.0.0.1'
PORT = 8080

socket.setdefaulttimeout(30)

# Mount host
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

s.listen()


while True:

    # Conection
    conn, addr = s.accept()
    print("Connection: " + str(conn) + ", Addr: " + str(addr))

    # Received data
    data = conn.recv(4096)
    data=pickle.loads(data)
    print(data)

    