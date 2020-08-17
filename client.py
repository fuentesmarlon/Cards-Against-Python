import os
import pathlib
import socket
import bitarray
from player import *
from user_ui import *
import json
# host and port to sent data
HOST = '127.0.0.1'
PORT = 8080
# HOST = 'redesgameserver.eastus.cloudapp.azure.com' 
# PORT = 22

flag=menu()

white_cards,black_cards = load_cards()

# instructions
while flag == "3":
    print('''
    
    INSTRUCTIONS:
    1. Create a new game or join an existing session. When you create a new game
    a session id will be given to you. Pass this number to your friends so they 
    can join you in your session. If you are joining a session ask your friend for
    the session id, you can use this number to join him. (NUMBER OF PLAYERS: 3)

    2. Each round the same new card with a statement or question will be given to all 
    the players. This is the black card. Then each player will we dealt 5 white cards. 
    This cards are use to fill the statement or question given by the black card, and
    they are unique to you.

    3. For each round choose one of your white cards, the one that creates the funniest
    statement when joined with the black card. And dont worry, every time you play a new
    white card will be dealt to you at the end of each round.

    4. After choosing which card to play, you will have to vote for which of the cards 
    played by everyone is the funniest. And I know what you are thinking and NO YOU CANT 
    VOTE YOURSELF. Come on now, dont be selfish.
    
    5. The winner of the round will get 5 points, the second place 3, and the last place 0.
    In the unlikely event that there is a tie, everyone will get 1 point, you know as a
    consolation prize for being equally unfunny.

    6. The game consist of 10 rounds, so have fun and try using the chat to talk to 
    everyone.

    7. Ok now, if you have read this far, congrats! but you probably arent a fun person. You are
    that kind of person that reads the user agrement and follows all the instructions of the
    ikea furniture. But hey at least you now know how play this game, you propably would have 
    figure it out by yourself. So yeah you just waisted 5 minutes of your life reading this,
    sorry.
    ''')

    flag = input("""
    CARDS AGAINST PYTHON VERSION

    CHOOSE ONE OPTION:
        1. New Game
        2. Join Session
        3. Instructions
        4. Exit game
    """)

if flag=="4":
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
        
        if data["action"]=="handshake":
            if data["confirmation"]=="ok":
                
                print("New game created! Your Session ID is:"+str(data["session_id"]))
                new_player.assign_session(data["session_id"])

                chat = pathlib.Path("clientChat.py").absolute()
                chat = os.path.join(chat)

                os.system('start cmd.exe /k python "' + str(chat) + '" ' + str(data["user"]) + ' ' \
                     + str(data["session_id"]))
                
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
            if(data["empate"]==0):
                if(data["primero"]==new_player.username):
                    new_player.add_points(5)
                if(data["segundo"]==new_player.username):
                    new_player.add_points(3)
                else:
                    new_player.add_points(0)
            else:
                new_player.add_points(1)
            print("\nAt the end of that round, your points are:\n"+str(new_player.points))
        if data["action"]=="cartas_nueva":
            
            new_player.add_card(data["carta_blanca"])
            print("\nNew Round! A NEW card was added to your collection")
            display_info(white_cards,black_cards,data,new_player.cards)

            played_card = int(input("\n What card will you play?\n (Please insert a number)\n"))

            
            msg=dic_parser(2,new_player,played_card)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            s.connect((HOST, PORT))
            s.sendall(msg) 
            continue
        if data["action"]=="fin_de_juego":
            print("\nAND TODAY'S GAME RANKING IS:\n")
            print("WINNER\n"+data["primero"]+":"+str(data["puntos_p1"])+" points")
            print("LOSER\n"+data["segundo"]+":"+str(data["puntos_p2"])+" points")
            print("TONIGHTS BIGGEST LOSER\n"+data["tercero"]+":"+str(data["puntos_p3"])+" points")

            print(""" Thanks For Playing! """)
            quit()


