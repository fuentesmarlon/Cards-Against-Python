import sys
import csv
import socket
import json
import bitarray
from random import randint

# host and port to sent data
# HOST = 'redesgameserver.eastus.cloudapp.azure.com' 
HOST = '127.0.0.1'
PORT = 8888

# CARTAS PARA EL JUEGO
with open('white_cards.csv', newline='') as csvfile:
    cartas_blancas_todas = list(csv.reader(csvfile)) 

with open('black_cards.csv', newline='') as csvfile:
    cartas_negras_todas = list(csv.reader(csvfile)) 

# HANDSHAKE
msm = {"action":"handshake", "user": "Diego", "session_id": int(sys.argv[1])}
msm = json.dumps(msm)

msm_bits = bitarray.bitarray()
msm_bits.frombytes(msm.encode('utf-8'))

# Sent message
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((HOST, PORT))
s.sendall(msm_bits)

# SERVER RESPONSE CONFIRMATION 
data = s.recv(5120)
print(data)

# User info
user_info = json.loads(data)
session_id = user_info['session_id']
user_name = user_info['user']

# SERVER RESPONSE CARDS
data2 = s.recv(5120)
print(data2)

new_cards = json.loads(data2)
cartas = new_cards['cartas_blancas']
carta_negra = new_cards['carta_negra']

while True:
    # select cart to sent
    carata_elegida = cartas[randint(0, len(cartas) - 1)]
    cartas.pop(cartas.index(carata_elegida))

    # CHOOSE AND SENT WHITE CARD
    msm = {"action":"jugar_carta", "session_id": session_id, "carta":carata_elegida}
    msm = json.dumps(msm)

    msm_bits = bitarray.bitarray()
    msm_bits.frombytes(msm.encode('utf-8'))

    # Sent message
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.connect((HOST, PORT))
    s.sendall(msm_bits)

    # RESPONSE VOTING OPTIONS
    data3 = s.recv(5120)
    print(data3)

    cartas_votos = json.loads(data3)
    cartas_votos = cartas_votos['cartas']
    voto = cartas_votos[randint(0,len(cartas_votos) - 1)]

    # CHOOSE AND SENT VOTE
    msm = {"action":"voto", "session_id": session_id, "user_name": user_name, "carta":voto}
    msm = json.dumps(msm)

    msm_bits = bitarray.bitarray()
    msm_bits.frombytes(msm.encode('utf-8'))

    # Sent message
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.connect((HOST, PORT))
    s.sendall(msm_bits)

    # RESPONSE ROUND RESULTS
    data4 = s.recv(5120)
    print(data4)

    # RESPONSE NEW CARDS
    data5 = s.recv(5120)
    print(data5)

    siguiente_ronda = json.loads(data5)
    accion = siguiente_ronda['action']
    
    if accion == "cartas_nueva":
        cartas.append(siguiente_ronda['carta_blanca'])
        carta_negra = siguiente_ronda['carta_negra']
    elif accion == "fin_de_juego":
        break

s.close()


