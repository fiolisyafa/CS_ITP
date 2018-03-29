from UNO import *

print('LET\'S PLAY UNO\n')
print('Basically this is a game of uno without any of the wildcards. HAVE FUN!\n')
#Start by creating and shuffling all the cards
main_deck = Cards()
main_deck.standard_cards()
#main_deck.wild()
main_deck.shuffle()


#distribute 7 cards to each player
first_card = Start()
make_deck = Make_deck()
make_deck.player1_Deck()
user_deck = make_deck.player1_Deck()
auto_deck = make_deck.player2_Deck()


player_1 = Player1_user()
player_2 = Player2_auto()

turn_count = 1

start_exit = input('Start/Exit? ')
if start_exit.lower() == 'exit':
    print('See you next time!')
if start_exit.lower() == 'start':
    card_in_play = first_card.starting_card()
    print(card_in_play)
    while True:
        if turn_count % 2 == 1:
            print(player_1.display_cards())
            card_in_play = player_1.move(card_in_play)
            print(card_in_play)
            turn_count += 1
            if len(player_1.display_cards()) == 1:
                print(input('You have one card left! Say: '))
            elif len(player_1.display_cards()) == 0:
                print('You Win!')
                break
        else:
            card_in_play = player_2.move(card_in_play)
            print(card_in_play)
            turn_count += 1
            #print(player_2.display_cards())
            print('Your opponent has ' + str(len(player_2.display_cards())) + ' card(s) left.')
            if len(player_2.display_cards()) == 1:
                print('UNO!')
            elif len(player_2.display_cards()) == 0:
                print("Your opponent won... fucking loser")
                break
