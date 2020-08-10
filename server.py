import socket
import json
import bitarray
import game_class

# host and port to sent data
# HOST = socket.gethostname() 
HOST = '127.0.0.1'
PORT = 8888

socket.setdefaulttimeout(20)

# Mount host
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

s.listen()

# Clients
clients_ids = []
ciients_sessions = []

# Sessions array
sessions = []

# Sent message function
def sent_message(to_sent, conn):

    to_sent = json.dumps(to_sent)
    msm_bits = bitarray.bitarray()
    msm_bits.frombytes(to_sent.encode('utf-8'))

    conn.sendall(msm_bits)
    

while True:

    # Conection
    conn, addr = s.accept()
    print("Connection: " + str(conn) + ", Addr: " + str(addr))

    # Received data
    data = conn.recv(4096)
    data = json.loads(data.decode('utf-8'))

    # HANDSHAKE
    if data['action'] == "handshake":

        # Vars
        ses_id = data['session_id']
        confirm = "no"

        # New session
        if ses_id == 0:
            ses_id = len(sessions) + 1

            # Create new session
            new_session = game_class.game(ses_id)
            sessions.append(new_session)

            # Add user
            confirm = new_session.set_player(data['user'], addr, conn)

        # Join session
        else:
            # Add user
            confirm = sessions[ses_id - 1].set_player(data['user'], addr, conn)

        # Sent confirmation
        to_sent = {"action": "handshake", "session_id": ses_id, "confirmation": confirm}
        sent_message(to_sent, conn)

        # START ROUND 1
        if sessions[ses_id - 1].players == 3:
            
            # Round variables
            tmp_session = sessions[ses_id - 1]
            black_card = tmp_session.get_blackcards(1)[0]
            players = [tmp_session.player1, tmp_session.player2, tmp_session.player3]
            players_users = [i[0] for i in players] 

            # Sent cards to each player
            for i in players:
                tmp_w_cards = tmp_session.get_whitecards(5)

                i[4] += tmp_w_cards      # Adds record of what cards each player has

                to_sent = {"action":"cartas", "cartas_blancas": tmp_w_cards, \
                    "carta_negra": black_card, "jugadores":players_users}

                sent_message(to_sent, i[2])

    # JUGAR_CARTA
    elif data['action'] == "jugar_carta":
        
        # Round variables
        tmp_session = sessions[data['session_id'] - 1]
        round_number = tmp_session.rounds

        # Players making the decision
        if len(tmp_session.rounds_cards[round_number]) < 3:
            # Add player
            tmp_session.rounds_cards[round_number].append((data['carta'], conn))

        # Sent cards played back
        if len(tmp_session.rounds_cards[round_number]) == 3:
            # Cards with addrs
            tmp_round_decisions = tmp_session.rounds_cards[round_number]

            # Get users connection and cards to sent
            for i in tmp_round_decisions:
                tmp_conn = i[1]
                tmp_cards = []

                for j in tmp_round_decisions:
                    # Add cards
                    if j != i:
                        tmp_cards.append(j[0])

                # Sent message to user i
                to_sent = {"action":"cartas_jugadas","cartas":tmp_cards}
                sent_message(to_sent, tmp_conn)

    # VOTO
    elif data['action'] == "voto":

        # Round variables
        tmp_session = sessions[data['session_id'] - 1]
        round_number = tmp_session.rounds

        # Players voting
        if len(tmp_session.rounds_votes[round_number]) < 3:
            # Add vote
            tmp_session.rounds_votes[round_number].append((data['carta'], conn, data['user_name']))

        # Sent cards played back
        if len(tmp_session.rounds_votes[round_number]) == 3:

            # Total votes
            tmp_votes = tmp_session.rounds_votes[round_number]
            tmp_votes_cards = [i[0] for i in tmp_votes]
            tmp_votes_conns = [i[1] for i in tmp_votes]
            tmp_votes_nplay = [i[2] for i in tmp_votes]
            tmp_first  = max(tmp_votes_cards)
            tmp_second = min(tmp_votes_cards)

            # Add points and get winners
            players = [tmp_session.player1, tmp_session.player2, tmp_session.player3]
            first_place, second_place, third_place = ('','','')

            for i in players:
                if tmp_first in i[4]:
                    i[3] += 5           # first place +5
                    first_place = i[0]

                elif tmp_second in i[4]:
                    i[3] += 3           # second place +3
                    second_place = i[0]

                else:
                    third_place = i[0]  # third place +0
            
            # Sent results
            to_sent = {"action":"resultado","primero":first_place,"segundo":second_place,"tercero":third_place}
            
            for i in tmp_votes_conns:
                sent_message(to_sent, i)

            # Add +1 to rounds
            tmp_session.rounds += 1

            # NEW ROUND
            if tmp_session.rounds < 10:

                # Sent new cards to each player
                black_card = tmp_session.get_blackcards(1)[0]

                for i in range(len(tmp_votes_conns)):
                    tmp_w_cards = tmp_session.get_whitecards(1)

                    # Adds record of what cards each player has
                    players[tmp_session.get_player(tmp_votes_nplay[i])][4] += tmp_w_cards 

                    to_sent = {"action": "cartas_nueva", "carta_blanca": tmp_w_cards[0], "carta_negra": black_card}

                    sent_message(to_sent, tmp_votes_conns[i])

            # FINAL RESULTS
            else:
                # Get final results
                places = []

                for i in players:
                    places.append([i[0],i[3]])

                places.sort(key = lambda x: x[1])

                # Sent results
                to_sent = {"action": "fin_de_juego", "primero": places[2][0], "puntos_p1": places[2][1], \
                    "segundo": places[1][0], "puntos_p2": places[1][1], "tercero": places[0][0], "puntos_p3": places[0][1]}

                for i in tmp_votes_conns:
                    sent_message(to_sent,conn)


                

                


        








