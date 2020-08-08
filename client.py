import socket
import bitarray

# host and port to sent data
HOST = 'redesgameserver.eastus.cloudapp.azure.com' 
PORT = 22

# Message
msm = "Hello"

# Message in bits
msm_bits = bitarray.bitarray()
msm_bits.frombytes(msm.encode('utf-8'))

# sent message
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((HOST, PORT))
s.sendall(msm_bits)

# receive host response
data = s.recv(4096)

print(data)

