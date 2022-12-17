# The Sueca Game
# A tricks-based card game, Sueca is played by 4 players
# who form two pairs competing against each other. Sueca is
# usually played at a squared table; the players that form a
# pair sit opposite from each other (Fig. 1). The aim is to win
# tricks containing valuable cards which are worth points; the
# pair that makes most points wins.

import random
import time

class Card():
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        
    def show_card(self):
        print(f"{self.value} of {self.suit}")

class Deck(Card):
    def __init__(self):
        self.cards = []
        self.build()
        
    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(v, s))
                
    def show_deck(self):
        for c in self.cards:
            c.show_card()
            
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
            
    def draw_card(self):
        return self.cards.pop()
    
class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []
        
    def draw(self, deck):
        self.hand.append(deck.draw_card())
        return self

    def show_hand(self):
        for card in self.hand:
            card.show_card()
            
    def play_card(self, card):
        self.hand.remove(card)
        return card
    
    def get_card(self, card):
        self.hand.append(card)
        return self
    
    def get_hand(self):
        return self.hand
    
    def get_name(self):
        return self.name
        
class Game():
    def __init__(self, player1, player2, player3, player4):
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.player4 = player4
        self.players = [self.player1, self.player2, self.player3, self.player4]
        self.deck = Deck()
        self.trump = None
        self.round = 0
        
    def deal_cards(self):
        self.deck.shuffle()
        for i in range(10):
            for player in self.players:
                player.draw(self.deck)
                
    def show_cards(self):
        for player in self.players:
            print(player.get_name())
            player.show_hand()
            print("showing cards")
            
    def get_trump(self):
        self.trump = self.deck.cards[39].suit
        print(f"The trump is {self.trump}")
        
    def play_round(self):
        self.round += 1
        print(f"Round {self.round}")
        self.play_trick()
        
    def play_trick(self):
        trick = []
        for player in self.players:
            print(player.get_name())
            player.show_hand()
            card = player.play_card(player.get_hand()[0])
            trick.append(card)
            print(f"Played {card.value} of {card.suit}")
        self.get_trick_winner(trick)
        
    def get_trick_winner(self, trick):
        print("Getting trick winner")
        for card in trick:
            if card.suit == self.trump:
                print(f"{card.value} of {card.suit} is the winner")
                break
            else:
                print(f"{card.value} of {card.suit} is not the winner")
                
    def play_game(self):
        self.deal_cards()
        self.show_cards()
        self.get_trump()
        self.play_round()
        
player1 = Player("Player 1")
            