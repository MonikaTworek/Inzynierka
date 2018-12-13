# Najbardziej medialna i filmowa strategia, która polega na liczeniu oczek. Niskie karty (od 2 do 6) maja
# wartosc +1. Srednie karty (od 7 do 0) sa neutralne i maja wartosc 0. Pozostałe, wysokie karty maja wartosc
# -1. Przed rozpoczeciem rozdania stół ma wartosc 0. Wraz ze wzrostem wyniku rosnie prawdopodobienstwo,
# ze w talii pozostaje wiecej wysokich kart i odwrotnie - jezeli potrzebna jest niska karta, a wynik jest ujemny,
# to oznacza, ze jest wysokie prawdopodobienstwo karty z przedziału 2-6.
from blackjack.game.table import Table


class HiLow:
    def __init__(self, table: Table):
        self.table = table
        self.low = [2, 3, 4, 5, 6] #4
        self.non = [7, 8, 9] #8
        self.high = [10, 11, 12, 13, 1] #10
        self.score = 0
        self.croupierfirst = 0

    def play(self):
        try:
            while True:
                self.table.begin_game()
                if self.table.croupier.hand.value in self.low :
                    self.score += 1
                    self.croupierfirst = 1
                elif self.table.croupier.hand.value in self.high:
                    self.score -= 1
                    self.croupierfirst = -1
                else:
                    self.croupierfirst = 0

                if self.table.player.hand1.cards[0].rank in self.low :
                    self.score += 1
                elif self.table.player.hand1.cards[0].rank in self.high:
                    self.score -= 1

                if self.table.player.hand1.cards[1].rank in self.low :
                    self.score += 1
                elif self.table.player.hand1.cards[1].rank in self.high:
                    self.score -= 1

                while self.table.player.hand1.playing:
                    if 21 - self.table.player.hand1.value > 10:
                        if self.score > 0:
                            self.table.hit1()
                            if self.table.player.hand1.lastcard in self.low:
                                self.score += 1
                            elif self.table.player.hand1.lastcard in self.high:
                                self.score -= 1
                        else:
                            self.table.resolve_game()
                            for lol in self.table.croupier.hand.cards:
                                if lol.rank in self.low:
                                    self.score += 1
                                elif lol.rank in self.high:
                                    self.score -= 1
                            self.score -= self.croupierfirst
                    elif 21 - self.table.player.hand1.value > 8:
                        if self.score in [-1, 0, 1]:
                            self.table.hit1()
                            if self.table.player.hand1.lastcard in self.low:
                                self.score += 1
                            elif self.table.player.hand1.lastcard in self.high:
                                self.score -= 1
                        else:
                            self.table.resolve_game()
                            for lol in self.table.croupier.hand.cards:
                                if lol.rank in self.low:
                                    self.score += 1
                                elif lol.rank in self.high:
                                    self.score -= 1
                            self.score -= self.croupierfirst
                    else:
                        if self.score < 0:
                            self.table.hit1()
                            if self.table.player.hand1.lastcard in self.low:
                                self.score += 1
                            elif self.table.player.hand1.lastcard in self.high:
                                self.score -= 1
                        else:
                            self.table.resolve_game()
                            for lol in self.table.croupier.hand.cards:
                                if lol.rank in self.low:
                                    self.score += 1
                                elif lol.rank in self.high:
                                    self.score -= 1
                            self.score -= self.croupierfirst


        except:
            return [self.table.winnings, self.table.draw, self.table.loosing, self.table.player.account_balance, self.table.blackjack]