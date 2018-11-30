# Ta strategia bardzo opiera sie na widocznej karcie krupiera. Jezeli ma ona wartosc 2 lub 3, to gracz pasuje,
# gdy posiada co najmniej 13 punktów. Jezeli karta jest z przedziału od 4 do 7, to gracz przestaje dobierac
# karty, gdy ma co najmniej 17 punktów. W pozostałych przypadkach gracz pasuje kiedy ma co najmniej 18
# oczek.
from blackjack.game.table import Table


class Bank:
    def __init__(self, table: Table):
        self.table=table

    def play(self):
        try:
            while True:
                self.table.begin_game()
                if self.table.croupier.hand.value in [2, 3]: # or self.table.croupier.hand.value == 3:
                    while self.table.player.hand1.playing is True and self.table.player.hand1.value < 13:
                        self.table.hit1()
                    if self.table.player.hand1 is True:
                        self.table.resolve_game()
                elif self.table.croupier.hand.value in [4, 5, 6, 7]:
                    while self.table.player.hand1.playing is True and self.table.player.hand1.value < 17:
                        self.table.hit1()
                    if self.table.player.hand1 is True:
                        self.table.resolve_game()
                else:
                    while self.table.player.hand1.playing is True and self.table.player.hand1.value < 18:
                        self.table.hit1()
                    if self.table.player.hand1 is True:
                        self.table.resolve_game()
        except:
            return [self.table.winnings, self.table.draw, self.table.loosings, self.table.player.account_balance, self.table.blackjack]