import sys
import socket
import json
import bitarray
from random import randint

# host and port to sent data
# HOST = 'redesgameserver.eastus.cloudapp.azure.com' 
HOST = '127.0.0.1'
PORT = 8888

# HANDSHAKE
user_name = "Diego" + str(randint(0,10000))
msm = {"action":"handshake", "user": user_name, "session_id": int(sys.argv[1])}
msm = json.dumps(msm)

msm_bits = bitarray.bitarray()
msm_bits.frombytes(msm.encode('utf-8'))

# Sent message
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((HOST, PORT))
s.sendall(msm_bits)

# RESPONSE CONFIRMATION 
data = s.recv(4096)
print(data)

# RESPONSE CARDS
data2 = s.recv(4096)
print(data2)

cartas = json.loads(data2)
cartas = cartas['cartas_blancas']
carata_elegida = cartas[randint(0, len(cartas) - 1)]

# CHOOSE AND SENT WHITE CARD
msm = {"action":"jugar_carta", "session_id": 1, "carta":carata_elegida}
msm = json.dumps(msm)

msm_bits = bitarray.bitarray()
msm_bits.frombytes(msm.encode('utf-8'))

# Sent message
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((HOST, PORT))
s.sendall(msm_bits)

# RESPONSE VOTING OPTIONS
data3 = s.recv(4096)
print(data3)

cartas = json.loads(data3)
cartas = cartas['cartas']
voto = cartas[randint(0,len(cartas) - 1)]

# CHOOSE AND SENT VOTE
msm = {"action":"voto", "session_id": 1, "user_name": user_name, "carta":voto}
msm = json.dumps(msm)

msm_bits = bitarray.bitarray()
msm_bits.frombytes(msm.encode('utf-8'))

# Sent message
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((HOST, PORT))
s.sendall(msm_bits)

# RESPONSE ROUND RESULTS
data4 = s.recv(4096)
print(data4)

# RESPONSE NEW CARDS
data4 = s.recv(4096)
print(data4)

cartas = json.loads(data2)
cartas = cartas['cartas_blancas']
carata_elegida = cartas[randint(0, len(cartas) - 1)]

# CHOOSE AND SENT WHITE CARD
msm = {"action":"jugar_carta", "session_id": 1, "carta":carata_elegida}
msm = json.dumps(msm)

msm_bits = bitarray.bitarray()
msm_bits.frombytes(msm.encode('utf-8'))

# Sent message
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((HOST, PORT))
s.sendall(msm_bits)

# RESPONSE VOTING OPTIONS
data3 = s.recv(4096)
print(data3)

cartas = json.loads(data3)
cartas = cartas['cartas']
voto = cartas[randint(0,len(cartas) - 1)]

# CHOOSE AND SENT VOTE
msm = {"action":"voto", "session_id": 1, "user_name": user_name, "carta":voto}
msm = json.dumps(msm)

msm_bits = bitarray.bitarray()
msm_bits.frombytes(msm.encode('utf-8'))

# Sent message
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((HOST, PORT))
s.sendall(msm_bits)

# RESPONSE ROUND RESULTS
data4 = s.recv(4096)
print(data4)

# RESPONSE NEW CARDS
data4 = s.recv(4096)
print(data4)

s.close()


