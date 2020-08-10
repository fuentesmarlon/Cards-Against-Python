from random import shuffle

class game():

    def __init__(self, session_id):
        self.session_id = session_id
        self.players = 0
        self.player1 = None
        self.player2 = None
        self.player3 = None
        self.rounds = 0
        self.rounds_cards = [[],[],[],[],[],[],[],[],[],[]]
        self.rounds_votes = [[],[],[],[],[],[],[],[],[],[]]
        self.whitecards = [i for i in range(50)]
        self.blackcards = [i for i in range(50)]
        self.turns = 0

        shuffle(self.whitecards)
        shuffle(self.blackcards)

    def set_player(self, name, user_id, conn):
        
        if self.player1 == None:
            self.player1 = [name, user_id, conn, 0, []]
            self.players += 1
            return 'ok'

        elif self.player2 == None:
            self.player2 = [name, user_id, conn, 0, []]
            self.players += 1
            return 'ok'

        elif self.player3 == None:
            self.player3 = [name, user_id, conn, 0, []]
            self.players += 1
            return 'ok'

        return 'no'

    def get_player(self, user_name):

        if self.player1[0] == user_name:
            return 0

        elif self.player2[0] == user_name:
            return 1

        elif self.player3[0] == user_name:
            return 2
    
    
    def reset_whitecards(self):
        self.whitecards = [i for i in range(50)]
        shuffle(self.whitecards)

    def reset_blackcards(self):
        self.whitecards = [i for i in range(50)]
        shuffle(self.whitecards)

    def get_whitecards(self, number_of_cards):
        cards = []

        for i in range(number_of_cards):
            card = self.whitecards.pop()
            cards.append(card)

        return cards

    def get_blackcards(self, number_of_cards):
        cards = []

        for i in range(number_of_cards):
            card = self.blackcards.pop()
            cards.append(card)

        return cards

        
    



