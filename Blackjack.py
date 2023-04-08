

# BLACKJACK GAME

'''

Rules for this non-fully version of a blackjack game:

1) Ace has only the value of 1
2) Whoever has more than 21, loses
3) If dealer has less than 17, he must hit automatically until he has at least 17. If he has 17 or more in his hand, he must stand
4) You can modify your wallet at line 101 if you want more or less money
5) The game has only a deck to play(52 different cards)
5) Good luck!

'''

# LIBRARIES

import random

# GLOBAL VARIABLES

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two' : 2, 'Three' : 3, 'Four' : 4, 'Five' : 5, 'Six' : 6, 'Seven' : 7, 'Eight' : 8, 'Nine' : 9, 'Ten' : 10, 'Jack' : 10, 'Queen' : 10, 'King' : 10, 'Ace' : 1}


# CARD CLASS

class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


# DECK CLASS

class Deck():

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


# PLAYER CLASS

class Player():
    def __init__(self, name, wallet):
        self.name = name
        self.game_cards = []
        self.wallet = wallet

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.game_cards.extend(new_cards)
        else:
            self.game_cards.append(new_cards)

    def remove_one(self):
        return self.game_cards.pop(0)

    def __str__(self):
        return f'Player {self.name} has {self.wallet} $ and {self.game_cards} cards'


# DEALER CLASS

class Dealer():
    def __init__(self):
        self.game_cards = []

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.game_cards.extend(new_cards)
        else:
            self.game_cards.append(new_cards)

    def remove_one(self):
        return self.game_cards.pop(0)

    def __str__(self):
        return f'Dealer has {len(self.game_cards)} cards'


# GAME SETUP

# CREATE THE PLAYER AND THE DEALER

player = Player('Player_name', 100)
dealer = Dealer()

# CREATE THE DECK

new_deck = Deck()
new_deck.shuffle()

# GAME LOGIC

used_game_cards = []

game_on = True

while game_on:
    print("Welcome to my blackjack game!")

    # bet in play
    bet = 0

    print(f'You have {player.wallet} $')

    if player.wallet <= 0:
        print("Player has no more money to play! \nGame over! \nDealer wins!")
        game_on = False
        break


    has_money = True

    while has_money:
        bet = int(input('Choose your bet: '))
        print('\n')
        if bet <= player.wallet:
            has_money = False
            player.wallet -= bet
        else:
            print('Your balance is lower than your bet! \nPlease choose a lower bet!')
            continue

    for x in range(2):
        player.add_cards(new_deck.deal_one())
        dealer.add_cards(new_deck.deal_one())


    print("Player has these cards: ")
    for x in range(2):
        print(player.game_cards[x])
    print('\n')

    print("Dealer has these cards: ")
    print(dealer.game_cards[0])
    print('X')
    print('\n')


    start_game = True

    sum_of_player_cards = 0
    sum_of_dealer_cards = 0

    while start_game:

        # Player's turn

        sum_of_player_cards = player.game_cards[0].value + player.game_cards[1].value
        print(f"Sum of player's cards is: {sum_of_player_cards}")
        print('\n')

        if sum_of_player_cards == 21:
            print("Player's sum is 21! Player wins!")
            start_game = False

        wanna_hit = True
        while wanna_hit:
            if input('Do you want to hit or stand? Press h for hit and s for stand! ') == 'h':
                print('\n')
                player.add_cards(new_deck.deal_one())
                print(f"Added card is: {player.game_cards[-1]}")
                sum_of_player_cards += player.game_cards[-1].value
                print(f"Sum of player's cards is: {sum_of_player_cards}")
                print('\n')

                if sum_of_player_cards > 21:
                    print("Player's sum of cards value is higher than 21! \nPlayer loses! Dealer wins!")
                    print('\n')
                    wanna_hit = False
                    start_game = False
                    break

                elif sum_of_player_cards == 21:
                    print("Player's sum is 21! Player wins!")
                    player.wallet += bet * 2
                    wanna_hit = False
                    start_game = False
                    break

            else:
                break

        if wanna_hit == False:
            break

        # Dealer's turn

        # Dealer can now show his second card

        sum_of_dealer_cards = dealer.game_cards[0].value + dealer.game_cards[1].value

        print("Second dealer's card is: \n")
        print(dealer.game_cards[-1])
        print('\n')
        print(f"Sum of dealer's cards is: {sum_of_dealer_cards}")
        print('\n')

        while sum_of_dealer_cards < 17:
            dealer.add_cards(new_deck.deal_one())
            print(f"Added dealer's card is: {dealer.game_cards[-1]}")
            sum_of_dealer_cards += dealer.game_cards[-1].value
            print(f"New sum of dealer's cards is: {sum_of_dealer_cards}")
            print('\n')


        if sum_of_dealer_cards > 21:
            print("Dealer's sum of cards value is higher than 21! \nDealer loses! Player wins!")
            print('\n')
            player.wallet += bet * 2
            break

        if sum_of_dealer_cards == 21:
            print("Dealer's sum is 21! Dealer wins!")
            print('\n')
            break

        # Compare

        if sum_of_player_cards == sum_of_dealer_cards:
            print("Draw! Nobody wins!")
            print('\n')
            player.wallet += bet
            break
        elif sum_of_player_cards > sum_of_dealer_cards:
            print("Player wins!")
            print('\n')
            player.wallet += bet * 2
            break
        elif sum_of_player_cards < sum_of_dealer_cards:
            print("Dealer wins!")
            print('\n')
            break

    # UPDATE CARDS AND DECK

    for x in range(len(player.game_cards)):
        used_game_cards.append(player.remove_one())
    for x in range(len(dealer.game_cards)):
        used_game_cards.append(dealer.remove_one())



    if player.wallet == 0:
        print("Player has no more money to play!\nGame over\nDealer wins!")
        print('\n')
        break

    if len(new_deck.all_cards) < 10:
        print("Not enough cards to play!\nGame over!")
        print('\n')
        break

    if input("Do you want to play again? y or n") == 'y':
        continue
    else:
        print('See you next time!')
        break












