import socket
import bitarray
import pickle 
import csv

def menu():
    choosen= input("""
    CARDS AGAINST PYTHON

    CHOOSE ONE OPTION:
        1. New Game
        2. Join Session
        3. Exit game
    """)

    return choosen 




def dic_parser(value_type,Player,action_val):
    
    dic_server = {}
    #handshake
    if value_type==1:
        dic_server["action"]="handshake"
        dic_server["user"]=Player.username
        dic_server["session_id"]=Player.session
    #play card
    if value_type==2:
        dic_server["action"]="jugar_carta"
        dic_server["session_id"]=Player.session
        dic_server["carta"]=Player.play_card(action_val)
    #round vote
    if value_type==3:
        dic_server["action"]="voto"
        dic_server["session_id"]=Player.session
        dic_server["user_name"]=Player.username
        dic_server["carta"]=action_val

    print(dic_server)
    #dic_server[value_send[0]]=value_send[1]
    msg=pickle.dumps(dic_server)
    
    return msg



def player_builder(type_game):
    username=str(input("""
    Welcome to Cards Against Python!!

    Please choose a Username: \n      
    
    """))
    
    if type_game=="2":
        session_id =int(input("What's yours session ID?\n"))
    else:
        session_id=0

    return username,session_id

def load_cards():
    white_cards=[]
    black_cards=[]
    with open("white_cards.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            white_cards.extend(map(str,row))
    with open("black_cards.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            black_cards.extend(map(str,row))
    return white_cards,black_cards

def display_info(white_cards,black_cards,dictionary_server,cards):

    white_choices=[]


    chosen_black = dictionary_server["carta_negra"]

    print("\nThis Round's Card:\n"+black_cards[chosen_black])


    for i in cards:
        white_choices.append(white_cards[i])
        

    print("\n YOUR CARDS ARE:\n")
    for i in range(0,len(white_choices)): 
        print("\n"+str(i)+" "+str(white_choices[i]))

def display_chosen(white_cards,dictionary_server):
    chosen_cards = dictionary_server["cartas"]
    print("TIME TO VOTE: The options are: \n")

    count=0
    for i in chosen_cards:

        print(str(count)+" "+str(white_cards[i]))
        count= count+1
        
    