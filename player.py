class Player:
    # Player parameters
    def __init__(self, username,cards,points,session):
        self.username=username
        self.cards = cards
        self.points = points
        self.session=session
    
    # play a card
    def play_card(self,choosed_card):
        return self.cards.pop(choosed_card)

    # add card to collection 
    def add_card(self,added_card):
        self.cards.append(added_card)

    def add_points(self,points_won):
        self.points = self.points + points_won

    def get_cards(self,new_cards):
        for i in range(0,len(new_cards)):
            self.cards.append(new_cards[i])
    def assign_session(self,session_id):
        self.session=session_id


