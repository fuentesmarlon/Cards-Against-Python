import socket
import sys

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234

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

            print(f"{ab2}")
            print(f"| {usuario} | ")
            print(f"{ab2}")
            print(f"{mensaje}\n")

    except:
        pass

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

mi_usuario = input("Usuario: ")
mi_id = input("Usuario id: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)

usuario = mi_usuario.encode("utf-8")
usuario_header = f"{len(usuario):<{HEADER_LENGTH}}".encode("UTF-8")

id_usuario = mi_id.encode("utf-8")
id_header = f"{len(id_usuario):<{HEADER_LENGTH}}".encode("UTF-8")

client_socket.send(usuario_header + usuario) 

while True: 
    mensaje = input(f"{mi_usuario}: \n")
    print("")
    # time.sleep(3)

    recibir_mensajes(mensaje)

