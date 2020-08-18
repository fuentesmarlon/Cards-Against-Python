# Cards-Against-Python

### Librerias y programs necesarios:
Python 3.7 <

Librerias
- pickle
- bitarray
- python-csv

El juego esta diseñado para Windows. Sin embargo, si se puede correr en otros sistemas operativos solo que se tendra que correr el chat por separado. Para correr el
chat separado se corre "python clientChat.py [USER_NAME] [ID DE LA SESION]".

### Correr el programa
El programa actualmente esta puesto para jugar localmente. Si esto es lo que se quiere, solo es necesario correr el programa server.py y luego en tres 
terminales distintas client.py, ambos sin ningun parametro. De lo contrario, si se quiere usar el servidor que se tiene para el juego (hablar con los administradores
para asegurarse que el servidor este activo) y luego en el programa del cliente habrá que quitar de comentarios la parte de HOST y PORT que se encuentran comentadas
en las lineas 11 y 12, igual con el chat en la parte de IP y PORT en las lineas 11 y 12. Luego solo es necesario correr el programa cliente.py en tres computadoras. De igual
manera el servidor y servidorChat tambien se encuentra en localhost, para cambiarlo solo es necesario quitar de comentarios el HOST e PORT puesto en comentario.

### Protocolo de comunicación cliente servidor 
- Handshake
  - Servidor recibe -> {"action": "handshake", "user": (STRING) USER_NAME, "session_id": (INT) session_id}
    - session_id = 0  -> nuevo juego
    - session_id != 0 -> entrar a juego establecido
  - Servidor envia  -> {"action": "handshake", "session_id": (INT) session_id, "user": (STRING) USER_NAME, "confirmation": (STRING) confirm}
    - confirm puede ser "ok" o "no"

- Init game (despues de  3 handshakes con la misma sesion)
  - Servidor envia  -> {"action": "cartas", "cartas_blancas": (LIST) [card_w_id0 ... card_w_id4], "carta_negra": card_b_id, "jugadores", (LIST) [username1, username2, usernam3]}
    - cartas_w -> cartas para el jugador
    - carta_negra -> carta para la mesa
    
- Decision de carta del jugador
  - Servidor recibe -> {"action": "jugar_carta", "session_id": (INT) session_id, "carta": card_w_id}
  - Servidor envia  -> {"action": "cartas_jugadas", "cartas": (LIST) [card_w_id0 ... card_w_id4]}
    - cartas -> se devuelve unicamente las cartas de otros jugadores

- Decision de ronda
  - Servidor recibe -> {"action":"voto", "session_id": (INT) session_id, "user_name", (STRING) username, "carta": card_w_id}
  - Servidor envia  -> {"action":"resultado", "primero": (STRING) username, "segundo": (STRING) username, "tercero": (STRING) username}
    - se devuelve luego de tener los tres votos

- Nueva ronda (justo despues de mandar los resultados anteriores)
  - Servidor envia  -> {"action": "cartas_nueva", "carta_blanca": card_w_id, "carta_negra": card_b_id}
    
- Finalizacion (justo despues de mandar los resultados de la ronda 10)
  - Servidor envia  -> {"action": "fin_de_juego", "primero": (STRING) username, "puntos_p1": (INT) puntos, "segundo": (STRING) username, "puntos_p2": (INT) puntos, "tercero": (STRING) username, "puntos_p3": (INT) puntos}
  
  
### Instrucciones para el juego
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
 
  
   
 
 
  
  
