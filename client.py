import socket
import bitarray
from player import *
from user_ui import *
import json
# host and port to sent data
#HOST = 'redesgameserver.eastus.cloudapp.azure.com' 
HOST = '127.0.0.1'
PORT = 8080


flag=menu()

white_cards,black_cards = load_cards()

if flag=="3":
    quit()
    
else:
    session_id=0    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.connect((HOST, PORT))
    username,game_id=player_builder(flag)


    new_player = Player(username,[],0,game_id)

    
    msg=dic_parser(1,new_player,game_id)
    s.sendall(msg)
    while True:

        
        #Receive Server response 
        

        data = s.recv(4096)
        data = json.loads(data.decode('utf-8'))
        print(data)
        if data["action"]=="handshake":
            if data["confirmation"]=="ok":
                
                print("New game created! Your Session ID is:"+str(data["session_id"]))
                new_player.assign_session(data["session_id"])
                
                continue
            else:
                print("failed to create game")
                quit()

        if data["action"]=="cartas":
            new_player.get_cards(data["cartas_blancas"])
            display_info(white_cards,black_cards,data,new_player.cards)

            played_card = int(input("\n What card will you play?\n (Please insert a number)\n"))

            
            msg=dic_parser(2,new_player,played_card)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            s.connect((HOST, PORT))
            s.sendall(msg) 
            continue
        if data["action"]=="cartas_jugadas":
            display_chosen(white_cards,data)
            choosen_values=data["cartas"]
            voto = int(input("Choose the card that best completes the sentence:\n"))            
            msg=dic_parser(3,new_player,choosen_values[voto])
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            s.connect((HOST, PORT))
            s.sendall(msg) 
            continue
        if data["action"]=="resultado":
            if(data["primero"]==new_player.username):
                new_player.add_points(5)
            if(data["segundo"]==new_player.username):
                new_player.add_points(3)
            else:
                new_player.add_card(0)
            print("At the end of that round, your points are:\n"+str(new_player.points))
        if data["action"]=="cartas_nueva":
            new_player.add_card(data["carta_blanca"])
            print("New Round! A NEW card was added to your collection")
            display_info(white_cards,black_cards,data,new_player.cards)

            played_card = int(input("\n What card will you play?\n (Please insert a number)\n"))

            
            msg=dic_parser(2,new_player,played_card)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            s.connect((HOST, PORT))
            s.sendall(msg) 
            continue
        if data["action"]=="fin_de_juego":
            print("\nAND TODAY'S GAME RANKING IS:\n")
            print("WINNER\n"+data["primero"]+":"+str(data["puntos_p1"]))
            print("LOSER\n"+data["segundo"]+":"+str(data["puntos_p2"]))
            print("TONIGHTS BIGGEST LOSER\n"+data["tercero"]+str(data["puntos_p3"]))

            finished=input("""
                Play Again?
                    1: F*ck Yeah.
                    2. No B*tch           
            
            """)
            if finished=="1":
                break
            else:
                quit()

# sent message


# receive host response
#data = s.recv(4096)

#print(data)

