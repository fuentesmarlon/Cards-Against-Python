import socket
import bitarray
from player import *
from user_ui import *
# host and port to sent data
#HOST = 'redesgameserver.eastus.cloudapp.azure.com' 
HOST = '127.0.0.1'
PORT = 8080


flag=menu()


if flag=="1":
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.connect((HOST, PORT))
        new_message=input("test_message")
        play_step=action(1)
        play_step.append(new_message)
        msg=dic_parser(play_step)
        s.sendall(msg)

if flag=="2":
    quit()
else:
    menu()

# sent message


# receive host response
data = s.recv(4096)

print(data)

