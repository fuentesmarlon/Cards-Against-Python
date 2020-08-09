import socket
import bitarray
import pickle 

def menu():
    choosen= input("""
    CARDS AGAINST PYTHON

    CHOOSE ONE OPTION:
        1. Play game
        2. Exit game
    """)

    return choosen 

def dic_parser(value_send):
    dic_server = {}
    dic_server[value_send[0]]=value_send[1]
    msg=pickle.dumps(dic_server)
    return msg

def action(action_type):
    play_step=[]
    if action_type==1:
        play_step.append("handshake")
        return play_step
    if action_type==2:
        play_step.append("vote")
        return play_step


