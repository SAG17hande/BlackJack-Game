import random 
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card:

    def __init__(self,suit,rank):
        self.suit= suit
        self.rank= rank
        

    def __str__(self):
        return self.rank + " of " + self.suit



class Deck:

    def __init__(self):
        self.allcards=[]

        for suit in suits:
            for rank in ranks:
                created_card=Card(suit,rank)
                self.allcards.append(created_card)

    def __str__(self):

        deck_comp = ''  # start with an empty string
        for card in self.Deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp


    def shuffle(self):
        random.shuffle(self.allcards)

    def deal(self):
        single_card=self.allcards.pop()
        return single_card

class Hand:

    def __init__(self):
        self.allcards = []  # start with an empty list as we did in the Deck class
        self.value =0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    

    def add_card(self,Card):
        self.allcards.append(Card)
        self.value +=values[Card.rank]
        if Card.rank =='Ace':
            self.aces += 1

    def adjust_for_ace(self):
        if self.value>21 and self.aces:
            self.value -=10
            self.aces -=1
        



class Chips:


    def __init__(self):
        self.money=0
        self.bet=0

    def win_bet(self):
        self.money += self.bet

    def Losing_bet(self):
        self.money -= self.bet


def take_bet(Chips):
    while True:
        try:
            Chips.money= int(input("how much u have:"))
            break
        except ValueError:
            print("dont enter non numeric values")
        
    while True:

        try:
            Chips.bet=int(input("how much u wanna bet:"))
        except ValueError:
            print("Sorry! a bet must be an integer")
        else:
            if Chips.bet > Chips.money:
                print ("you cant bet as u dont have money to bet")
            else:
                print(f"you have bet {Chips.bet} and now u have {Chips.money- Chips.bet} remaining")
                break

def hit(Deck,Hand):

    Hand.add_card (Deck.deal())
    Hand.adjust_for_ace()

def hit_stand(Deck,Hand):
    playing= True


    while True:
        x= input("do you want to hit or stand? type 'h'for hit or 's' for stand:")
        if x[0].lower() == 's':
            print("player choosed to stay, Dealer's turn now")
            playing = False

        elif x[0].lower()== 'h':
            hit(Deck,Hand)

        else:
            ("Sorry please try again!")
            continue

        break

def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.allcards[1])  
    print("\nPlayer's Hand:", *player.allcards, sep='\n ')

def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.allcards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.allcards, sep='\n ')
    print("Player's Hand =",player.value)

def player_busts(player,dealer,Chips):
    print("Player busts!")
    Chips.Losing_bet()

def player_wins(player,dealer,Chips):
    print("Player wins!")
    Chips.win_bet()

def dealer_busts(player,dealer,Chips):
    print("Dealer busts!")
    Chips.win_bet()

def dealer_wins(player,dealer,Chips):
    print("Dealer wins!")
    Chips.Losing_bet()

def push(player,dealer):
    print("Dealer and Player tie! It's a push.")


# GAMEPLAY!
playon= True
while playon:
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    # Set up the Player's chips
    player_money = Chips()  # remember the default value is 0
    
    # Prompt the Player for their bet:
    take_bet(player_money)
    
    # Show the cards:
    show_some(player_hand,dealer_hand)
   
    
    gameon = True
    while gameon:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)
        
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_money)
            
    
        # If Player hasn't busted, play Dealer's hand        
        if player_hand.value <= 21:

            while dealer_hand.value < 17:
                hit(deck,dealer_hand)

            # Show all cards
            show_all(player_hand,dealer_hand)

            # Test different winning scenarios
            if dealer_hand.value > 21:
                dealer_busts(player_hand,dealer_hand,player_money)

            elif dealer_hand.value > player_hand.value:
                     dealer_wins(player_hand,dealer_hand,player_money)

            elif dealer_hand.value < player_hand.value:
                Chips.player_wins(player_hand,dealer_hand,player_chips)

            else:
                Chips.push(player_hand,dealer_hand)

        # Inform Player of their chips total    
        print("\nPlayer's winnings stand at",player_money.money)

        # Ask to play again
        new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
        if new_game[0].lower()=='y':
            gameon=True
            continue
        else:
            print("Thanks for playing!")
            gameon=False
            playon=False
