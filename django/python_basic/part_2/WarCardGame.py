from random import shuffle

SUIT = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    def __init__(self):
        print("Created deck of card with ")
        self.allCards = [(s,r) for s in SUIT for r in RANKS]        
    def shuffle(self):
        shuffle(self.allCards)
    def split_in_half(self):
        return (self.allCards[:26],self.allCards[26:])

class Hand:
    def __init__(self,cards):
        self.cards = cards
    def __str__(self):
        return 'Contains {} cards'.format(len(self.cards))
    def add_card(self,added_card):
        self.cards.extend(added_card)
    def remove_card(self):
        return self.cards.pop()

class Player:
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed : {} ".format(self.name,drawn_card))
        return drawn_card
        print()

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.remove_card())
            return war_cards
    
    def still_has_cards(self):
        return len(self.hand.cards) != 0  


print("WelCome to the War Game.......\n")

#create a new deck and split in half
d = Deck()
d.shuffle()
half1,half2 = d.split_in_half()

#create both player

comp = Player('Computer',Hand(half1))

name = input("Enter your name : ")

user = Player(name,Hand(half2))

total_rounds = 0
war_count = 0

while user.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print()
    print()
    print("Time for new round\n")
    print("here are current standing\n")
    print(user.name +" has count: "+str(len(user.hand.cards)))
    print(comp.name +" has count: "+str(len(comp.hand.cards)))
    print()
    print("play a card")
    print()

    table_card = []

    c_card = comp.play_card()
    p_card = user.play_card()

    table_card.append(c_card)
    table_card.append(p_card)

    if c_card[1] == p_card[1]:
        war_count += 1
        print("war!")
        

        table_card.extend(user.remove_war_cards())
        table_card.extend(comp.remove_war_cards())

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add_card(table_card)
        else:
            comp.hand.add_card(table_card)
    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add_card(table_card)
        else:
            comp.hand.add_card(table_card)
    
print("Game over,number of rounds:"+str(total_rounds))
print("a war happned  "+str(war_count)+" times")