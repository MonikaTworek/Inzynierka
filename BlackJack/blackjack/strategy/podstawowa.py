from blackjack.game.table import Table


class Podstawowa:
    def __init__(self, table: Table):
        self.table = table

    def split(self):
        if self.table.player.hand1.value >= 17:
            self.table.stand1()
        elif self.table.player.hand1.value in [13, 14, 15, 16] and self.table.croupier.hand.value in [2, 3, 4, 5, 6]:
            self.table.stand1()
        elif self.table.player.hand1.value in [13, 14, 15, 16] and self.table.croupier.hand.value not in [2, 3, 4, 5, 6]:
            self.table.hit1()
        elif self.table.player.hand1.value == 12 and self.table.croupier.hand.value in [4, 5, 6]:
            self.table.stand1()
        elif self.table.player.hand1.value == 12 and self.table.croupier.hand.value not in [4, 5, 6]:
            self.table.hit1()
        else:
            self.table.hit1()

        if self.table.player.hand2.value >= 17:
            self.table.stand1()
        elif self.table.player.hand2.value in [13, 14, 15, 16] and self.table.croupier.hand.value in [2, 3, 4, 5, 6]:
            self.table.stand1()
        elif self.table.player.hand2.value in [13, 14, 15, 16] and self.table.croupier.hand.value not in [2, 3, 4, 5, 6]:
            self.table.hit1()
        elif self.table.player.hand2.value == 12 and self.table.croupier.hand.value in [4, 5, 6]:
            self.table.stand1()
        elif self.table.player.hand2.value == 12 and self.table.croupier.hand.value not in [4, 5, 6]:
            self.table.hit1()
        else:
            self.table.hit1()

    def play(self):
        try:
            while True:
                self.table.begin_game()

                #Kiedy mamy te same karty
                if self.table.player.hand1.cards[0].rank == self.table.player.hand1.cards[1].rank:
                    if self.table.player.hand1.cards[0].rank >= 10:
                        self.table.stand1()
                    elif self.table.player.hand1.cards[0].rank == 9 and self.table.croupier.hand.value in [7, 10, 1]:
                        self.table.stand1()
                    elif self.table.player.hand1.cards[0].rank == 9 and self.table.croupier.hand.value not in [7, 10, 1]:
                        self.table.split()
                        self.split()
                    elif self.table.player.hand1.cards[0].rank == 8:
                        self.table.split()
                        self.split()
                    elif self.table.player.hand1.cards[0].rank == 7 and self.table.croupier.hand.value in [8, 9, 10, 1]:
                        self.table.hit1()
                    elif self.table.player.hand1.cards[0].rank == 9 and self.table.croupier.hand.value not in [8, 9, 10, 1]:
                        self.table.split()
                        self.split()
                    elif self.table.player.hand1.cards[0].rank == 6 and self.table.croupier.hand.value in [7, 8, 9, 10, 1]:
                        self.table.hit1()
                    elif self.table.player.hand1.cards[0].rank == 6 and self.table.croupier.hand.value not in [7, 8, 9, 10, 1]:
                        self.table.split()
                        self.split()
                    elif self.table.player.hand1.cards[0].rank == 5 and self.table.croupier.hand.value in [10, 1]:
                        self.table.hit1()
                    elif self.table.player.hand1.cards[0].rank == 5 and self.table.croupier.hand.value not in [10, 1]:
                        self.table.double_down()
                    elif self.table.player.hand1.cards[0].rank == 4 and self.table.croupier.hand.value in [5, 6]:
                        self.table.split()
                        self.split()
                    elif self.table.player.hand1.cards[0].rank == 4 and self.table.croupier.hand.value not in [5, 6]:
                        self.table.hit1()
                    elif self.table.player.hand1.cards[0].rank in [2,3] and self.table.croupier.hand.value in [8, 9, 10, 1]:
                        self.table.hit1()
                    else:
                        self.table.split()
                        self.split()

                #Kiedy mamy na jednej z rąk asa:
                elif self.table.player.hand1.cards[0].rank == 1 or self.table.player.hand1.cards[1].rank == 1:
                    if self.table.player.hand1.cards[0].rank == 1:
                        otherhand = self.table.player.hand1.cards[1].rank
                    else:
                        otherhand = self.table.player.hand1.cards[0].rank
                    if otherhand in [8, 9]:
                        self.table.stand1()
                    elif otherhand == 7 and self.table.croupier.hand.value in [3, 4, 5, 6]:
                        self.table.double_down()
                    elif otherhand == 7 and self.table.croupier.hand.value in [2, 7]:
                        self.table.stand1()
                    elif otherhand == 7 and self.table.croupier.hand.value in [8, 9, 10, 1]:
                        self.table.hit1()
                    elif otherhand == 6 and self.table.croupier.hand.value in [3, 4, 5, 6]:
                        self.table.double_down()
                    elif otherhand == 6 and self.table.croupier.hand.value not in [3, 4, 5, 6]:
                        self.table.hit1()
                    elif otherhand in [4, 5] and self.table.croupier.hand.value in [4, 5, 6]:
                        self.table.double_down()
                    elif otherhand in [4, 5] and self.table.croupier.hand.value not in [4, 5, 6]:
                        self.table.hit1()
                    elif otherhand in [2, 3] and self.table.croupier.hand.value in [5, 6]:
                        self.table.double_down()
                    elif otherhand in [2, 3] and self.table.croupier.hand.value not in [5, 6]:
                        self.table.hit1()
                #pozostałe wypadki oparte na wartości ręki
                else:
                    if self.table.player.hand1.value >= 17:
                        self.table.stand1()
                    elif self.table.player.hand1.value in [13, 14, 15, 16] and self.table.croupier.hand.value in [2, 3, 4, 5, 6]:
                        self.table.stand1()
                    elif self.table.player.hand1.value in [13, 14, 15, 16] and self.table.croupier.hand.value not in [2, 3, 4, 5, 6]:
                        self.table.hit1()
                    elif self.table.player.hand1.value == 12 and self.table.croupier.hand.value in [4, 5, 6]:
                        self.table.stand1()
                    elif self.table.player.hand1.value == 12 and self.table.croupier.hand.value not in [4, 5, 6]:
                        self.table.hit1()
                    elif self.table.player.hand1.value == 11 and self.table.croupier.hand.value == 1:
                        self.table.hit1()
                    elif self.table.player.hand1.value == 11 and self.table.croupier.hand.value != 1:
                        self.table.double_down()
                    elif self.table.player.hand1.value == 10 and self.table.croupier.hand.value in [1, 10]:
                        self.table.hit1()
                    elif self.table.player.hand1.value == 10 and self.table.croupier.hand.value not in [1, 10]:
                        self.table.double_down()
                    elif self.table.player.hand1.value == 9 and self.table.croupier.hand.value in [3, 4, 5, 6]:
                        self.table.hit1()
                    elif self.table.player.hand1.value == 9 and self.table.croupier.hand.value not in [3, 4, 5, 6]:
                        self.table.double_down()
                    else:
                        self.table.hit1()
                if self.table.player.hand1.playing:
                    self.table.stand1()
                if self.table.player.hands2.playing:
                    self.table.stand2()

        except:
            return [self.table.winnings, self.table.draw, self.table.loosing, self.table.player.account_balance, self.table.blackjack]