import random

colors = ['red', 'yellow', 'blue', 'green']
class Cards:

    def __init__(self, standard=[], cards=[], user_deck=[], auto_deck=[], in_play=''):
        self.standard = standard
        self.cards = cards
        self.user_deck = user_deck
        self.auto_deck = auto_deck
        self.in_play = in_play

    def standard_cards(self):
        for color in colors:
            for numbers in range(10):
                self.cards.append(color + " " + str(numbers))
                self.standard.append(color + " " + str(numbers))
        return self.cards

    def shuffle(self):
        self.cards.reverse()
        for i in range(len(self.cards)-1):
            temp = self.cards[i]
            self.cards[i] = self.cards[random.randint(0, len(self.cards)-1)]
            self.cards[random.randint(0, len(self.cards)-1)] = temp
        return self.cards

class Make_deck(Cards):

    def __init__(self):
        super().__init__()

    def player1_Deck(self):
        while len(self.user_deck) < 7:
            self.user_deck.append(self.cards[random.randint(0, len(self.cards)-1)])
        return self.user_deck

    def player2_Deck(self):
        while len(self.auto_deck) < 7:
            self.auto_deck.append(self.cards[random.randint(0, len(self.cards)-1)])
        return self.auto_deck

class Start(Cards):

    def __init__(self):
        super().__init__()

    def starting_card(self):
        self.in_play = self.standard[random.randint(0, len(self.standard)-1)]
        return self.in_play


class Player1_user(Make_deck, Start):

    def __init__(self):
        super().__init__()

    def display_cards(self):
        return self.user_deck

    def move(self, in_play):
        #player should input the card they want to play in the form "red 5"
        user_choose_card = input('\nChoose a card that matches either the color or number. Type \'draw\' to draw card.')
        if user_choose_card.lower() == "draw":
            self.user_deck.append(self.cards[random.randint(0, len(self.cards)-1)])
            print("Card Drawn")
            return in_play
        else:
            c1, n1 = in_play.split()
            c2, n2 = user_choose_card.split()
            if (user_choose_card in self.user_deck) and (c1 == c2 or n1 == n2):
                del self.user_deck[self.user_deck.index(user_choose_card)]
                #c1, n1 = c2, n2
                temp = in_play
                in_play = user_choose_card
                temp = in_play
                return in_play

            elif user_choose_card not in self.user_deck:
                return 'You do not own this card.'

            elif c1 != c2 and n1 != n2:
                return 'You cannot play this card.'


class Player2_auto(Make_deck, Start):
    def __init__(self):
        super().__init__()

    def move(self, in_play):
        c1, n1 = in_play.split()
        match = []
        for card in self.auto_deck[:]:
            c3, n3 = card.split()
            if c1 == c3 or n1 == n3:
                match.append(card)
        #if no card matches, draw from the main deck and append the auto deck.
        if match == []:
            self.auto_deck.append(self.cards[random.randint(0, len(self.cards)-1)])
            return in_play
        else:
            for card in range(1):
                play_card = match[random.randint(0, len(match)-1)]
                del self.auto_deck[self.auto_deck.index(play_card)]
                temp = in_play
                in_play = play_card
            return in_play

    def display_cards(self):
        return self.auto_deck
