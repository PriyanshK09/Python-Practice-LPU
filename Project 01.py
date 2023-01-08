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
        self.trump = self.deck.cards[0].suit
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
player2 = Player("Player 2")
player3 = Player("Player 3")
player4 = Player("Player 4")
game = Game(player1, player2, player3, player4)
game.play_game()

# Output
# Player 1
# 1 of Spades
# 2 of Spades
# 3 of Spades
# 4 of Spades
# 5 of Spades
# 6 of Spades
# 7 of Spades
# 8 of Spades
# 9 of Spades
# 10 of Spades
# showing cards
# Player 2
# 1 of Clubs
# 2 of Clubs
# 3 of Clubs
# 4 of Clubs
# 5 of Clubs
# 6 of Clubs
# 7 of Clubs
# 8 of Clubs
# 9 of Clubs
# 10 of Clubs
# showing cards
# Player 3
# 1 of Diamonds
# 2 of Diamonds
# 3 of Diamonds
# 4 of Diamonds
# 5 of Diamonds
# 6 of Diamonds
# 7 of Diamonds
# 8 of Diamonds
# 9 of Diamonds
# 10 of Diamonds
# showing cards
# Player 4
# 1 of Hearts
# 2 of Hearts
# 3 of Hearts
# 4 of Hearts
# 5 of Hearts
# 6 of Hearts
# 7 of Hearts
# 8 of Hearts
# 9 of Hearts
# 10 of Hearts
# showing cards
# The trump is Spades
# Round 1
# Player 1
# 1 of Spades
# 2 of Spades
# 3 of Spades
# 4 of Spades
# 5 of Spades
# 6 of Spades
# 7 of Spades
# 8 of Spades
# 9 of Spades
# 10 of Spades
# Played 1 of Spades
# Player 2
# 1 of Clubs
# 2 of Clubs
# 3 of Clubs
# 4 of Clubs
# 5 of Clubs
# 6 of Clubs
# 7 of Clubs
# 8 of Clubs
# 9 of Clubs
# 10 of Clubs
# Played 1 of Clubs
# Player 3
# 1 of Diamonds
# 2 of Diamonds
# 3 of Diamonds
# 4 of Diamonds
# 5 of Diamonds
# 6 of Diamonds
#