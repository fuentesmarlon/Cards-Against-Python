import socket
import sys
import _thread as thread
import threading

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234
TIMEOUT = 10
mi_usuario = sys.argv[1]
mi_id = sys.argv[2]

# IP = 'redesgameserver.eastus.cloudapp.azure.com' 
# PORT = 21

def recibir_mensajes(mensaje):
    if mensaje:
        mensaje = mensaje.encode('utf-8')
        mensaje_header = f"{len(mensaje):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(mensaje_header + mensaje)

    try: 
        while True:
            usuario_header = client_socket.recv(HEADER_LENGTH)
            if not len(usuario_header):
                print("Conexion cerrada por el servidor")
                sys.exit()

            usuario_length = int(usuario_header.decode('utf-8').strip())
            usuario = client_socket.recv(usuario_length).decode('utf-8')

            mensaje_header = client_socket.recv(HEADER_LENGTH)
            mensaje_length = int(mensaje_header.decode('utf-8').strip())
            mensaje = client_socket.recv(mensaje_length).decode('utf-8')

            usr_len = len(usuario)
            ab2 = "-" * (usr_len + 4)

            print("")
            print(f"    {ab2}")
            print(f"    | {usuario} | ")
            print(f"    {ab2}")
            print(f"    {mensaje}")
            print("\n" + mi_usuario + ":")

    except:
        pass

def time_up():
    recibir_mensajes('update')
    timer = threading.Timer(TIMEOUT, time_up)
    timer.start()
    return 0


def timed_input(prompt , timeout=TIMEOUT):
    print(prompt, end=' ')    
    
    timer = threading.Timer(timeout, time_up)
    astring = None

    try:
        timer.start()
        astring = input()
    except:
        pass

    timer.cancel()
    return astring

print("""
 #####                                    #                                                                 
#     #   ##   #####  #####   ####       # #    ####    ##   # #    #  ####  #####     
#        #  #  #    # #    # #          #   #  #    #  #  #  # ##   # #        #         
#       #    # #    # #    #  ####     #     # #      #    # # # #  #  ####    #         
#       ###### #####  #    #      #    ####### #  ### ###### # #  # #      #   #      
#     # #    # #   #  #    # #    #    #     # #    # #    # # #   ## #    #   #      
 #####  #    # #    # #####   ####     #     #  ####  #    # # #    #  ####    #      
                                      
                                                                                                                                                                                     
#     # #    # #    #   ##   #    # # ##### #   #     #####  #    #   ##   #####
#     # #    # ##  ##  #  #  ##   # #   #    # #     #     # #    #  #  #    #
####### #    # # ## # #    # # #  # #   #     #      #       ###### #    #   #
#     # #    # #    # ###### #  # # #   #     #      #       #    # ######   #   
#     # #    # #    # #    # #   ## #   #     #      #     # #    # #    #   #   
#     #  ####  #    # #    # #    # #   #     #       #####  #    # #    #   #   
""")

print("User: " + mi_usuario + "\n")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)

usuario = mi_usuario.encode("utf-8")
usuario_header = f"{len(usuario):<{HEADER_LENGTH}}".encode("UTF-8")

id_usuario = mi_id.encode("utf-8")
id_header = f"{len(id_usuario):<{HEADER_LENGTH}}".encode("UTF-8")

client_socket.send(usuario_header + usuario) 

while True: 

    mensaje = timed_input(f"{mi_usuario}: \n")

    if mensaje == "exit":
        break

    recibir_mensajes(mensaje)

