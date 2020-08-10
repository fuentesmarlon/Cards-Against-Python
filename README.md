# Cards-Against-Python

### Protocolo de comunicación
- Handshake
  - Servidor recibe -> {"action": "handshake", "user": (STRING) USER_NAME, "session_id": (INT) session_id}
    - session_id = 0  -> nuevo juego
    - session_id != 0 -> entrar a juego establecido
  - Servidor envia  -> {"action": "handshake", "session_id": (INT) session_id, "confirmation": (STRING) confirm}
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
  - Servidor recibe -> {"action":"voto", "session_id": (INT) session_id, "carta": card_w_id}
  - Servidor envia  -> {"action":"resultado", "ganador_p1": (STRING) username, "ganador_p2": (STRING) username, "puntos": (INT) puntos}
    - se devuelve luego de tener los tres votos

- Nueva ronda (justo despues de mandar los resultados anteriores)
  - Servidor envia  -> {"action": "cartas_nueva", "carta_blanca": card_w_id, "carta_negra": card_b_id}
    
- Finalizacion (justo despues de mandar los resultados de la ronda 10)
  - Servidor envia  -> {"action": "fin_de_juego", "primero": (STRING) username, "segundo": (STRING) username, "tercero": (STRING) username}
  
   
 
 
  
  
