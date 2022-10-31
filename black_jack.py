'''
Blackjack is a game where the player needs to have the sum of cards value of 21. And if no one has the sum of 21, the winner is the closest one to the 21. And if more than 21, that player will bust and lose.

NEEDED CLASS:
1. class Card, for changing the card format.
2. class Deck, for generate all the 52 card.
3. class Hand, for the card in players hand.
4. class Chips, for calculating the chips.
'''
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
class Card:
    def __init__(self, suit, rank) -> None:
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self) -> None:
        self.allcards = []
        for i in suits:
            for j in ranks:
                self.allcards.append(Card(i,j))

    # 0 : top && -1 : bottom
    # For removing the top of the deck and return the card from the top of the deck
    def hit(self):
        return self.allcards.pop(0)

    # For shuffling the deck
    def shuffle(self):
        random.shuffle(self.allcards)
    
    # Return lenght of the self.allcards list
    def __len__(self):
        return len(self.allcards)

class Hand():
    def __init__(self) -> None:
        self.cards = []
        self.value = 0
    
    def add_card(self,new_card):
        self.cards.append(new_card)
        
        # Aces can have two value, 1 and 11. 
        if new_card.rank == 'Ace':
            # If the sum value is more than 10, the ace value will become 1
            if self.value >= 10:
                new_card.value = 1
            # If the sum value is less than 10, the ace value will become 11
            elif self.value <= 10:
                new_card.value = 11
        
        self.value += new_card.value
    
class Chip:
    def __init__(self, bet=0) -> None:
        # Total chip 
        self.total_chip = 100 
        self.bet = bet

    def lose_bet(self):
        self.total_chip -= self.bet

    def win_bet(self):
        self.total_chip += self.bet


def menu():
    print("Welcome to Black Jack")
    print("> Get as close to 21 as you can without going over!")
    print("> Dealer hits until she reaches 17. Aces count as 1 or 11.")
    print("1. Play")
    print("2. Exit")

def starter_deck(player):
    player.add_card(deck.hit())
    player.add_card(deck.hit())

def hit(player, card):
    player.add_card(card)
    print("Player cards : ", end='')
    for i in range(0, len(player.cards)):
        if i == len(player.cards)-1:
            print(player.cards[i], end='\n')
        else:
            print(player.cards[i], end=' & ')
    print(f'Player cards value : {player.value}')

def check_bust(value):
    if value > 21:
        return True
    return False

def dealer_hit(dealer, new_card):
    while dealer.value < 17 :
        dealer.add_card(new_card)

def show_some(dealer):
    print(f'Dealer cards : {dealer.cards[0]} and [[Hidden]]')

def show_all(dealer):
    print("Dealer cards : ", end='')
    for i in dealer.cards:
        if i == dealer.cards[-1]:
            print(i, end='\n')
        else :
            print(f'{i}', end=' & ')

def play_again():
    choose2 = input("Play again? [Y/N] : ").upper()
    if choose2 == 'N':
        return 2
    elif choose2 == 'Y':
        return 1

if __name__ == "__main__":
    # Show the menu options
    menu()
    choose = int(input("What you wanna do : "))
    # Storing player chips
    player_chips = Chip()

    while choose != 2:
        # Place a bet
        print(f'Player chips : {player_chips.total_chip}')
        player_chips.bet = int(input("Place a bet : "))
        # If bet value is more than player total chips
        while player_chips.bet >= player_chips.total_chip :
            print("You cannot do that")
            player_chips.bet = int(input("Place a bet : "))

        # Generate 52 cards
        deck = Deck()
        deck.shuffle()

        # Generate card on player hand
        player = Hand()
        starter_deck(player)
        print(f'Player cards : {player.cards[0]} & {player.cards[1]}')
        print(f'Player value : {player.value}')

        # Generate card on dealer hand
        dealer = Hand()
        dealer_new_card = deck.hit()
        starter_deck(dealer)

        # Hit function on player 
        flag = 1
        hit_choose = input("Hit? [Y/N]: ").upper()
        
        while hit_choose == 'Y':    
            # Show some dealer card
            choose_show = input("Show some dealer card? [Y/N] : ").upper()
            if flag == 1 :
                if choose_show == 'Y':
                    show_some(dealer)
                    flag = 2

            # Player hit function
            new_card = deck.hit()
            hit(player, new_card)
            hit_choose = input("Hit? [Y/N]: ").upper()

            # Check if bust
            if check_bust(player.value):
                print("You bust and lose")
                # Player chips will be minus by the bet
                player_chips.lose_bet()

                # Show chips 
                print(f'Player chips : {player_chips.total_chip}')

                # Player will be ask to play again or no
                choose = play_again()
                break
        
        # Dealer hit
        dealer_hit(dealer, dealer_new_card)
        print(f'Dealer value : {dealer.value}')
        show_all(dealer)
        # If dealer card busted
        dealer_busted = False
        if dealer.value > 21 :
            dealer_busted = True
            print("You win, dealer card busted")
            player_chips.win_bet()
            # Show chips 
            print(f'Player chips : {player_chips.total_chip}')



        # If player choose to not hit, so we will compare it to the dealer value
        if hit_choose == 'N':
            if player.value > dealer.value:
                print("You won!")
                player_chips.win_bet()

                # Show chips 
                print(f'Player chips : {player_chips.total_chip}')
            elif player.value < dealer.value and dealer_busted == False:
                print("You lose")
                player_chips.lose_bet()

                # Show chips 
                print(f'Player chips : {player_chips.total_chip}')
            elif player.value == dealer.value:
                print("No one wins, it is a draw")
            
            choose = play_again()

        # If player chips is 0
        if player_chips.total_chip <= 0:
            print("Your chips is 0, you cannot play anymore!")
            choose = 2
            break

    if choose == 2 :
        print("Bye bye!")