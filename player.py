class Player:
    # Player parameters
    def __init__(self, username,cards):
        self.username=username
        self.cards = cards
    
    # play a card
    def play_card(self,choosed_card):
        self.cards.pop(self.cards.index(choosed_card))

    # add card to collection 
    def add_card(self,added_card):
        self.cards.append(added_card)

    

