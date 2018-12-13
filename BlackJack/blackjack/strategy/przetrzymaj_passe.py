# Kiedy gracz ma miedzy 17, a 21 przestaje dobierac karty. W przypadku co najmniej 3 porazek pod rzad
# przestaje dobierac jak ma wiecej niz 13. W przypadku co najmniej 5 porazek gracz pasuje jak ma co najmniej
# 11 punktów.
from blackjack.game.table import Table


class PrzetrzymajPasse:
    def __init__(self, table: Table):
        self.table = table

    def play(self):
        seriaPorazek = 0
        try:
            while True:
                self.table.begin_game()
                while self.table.player.hand1.playing:
                    if seriaPorazek < 3:
                        if self.table.player.hand1.value < 17:
                            self.table.hit1()
                        else:
                            self.table.resolve_game()
                    elif 2 < seriaPorazek < 5:
                        if self.table.player.hand1.value < 14:
                            self.table.hit1()
                        else:
                            self.table.resolve_game()
                    else:
                        if self.table.player.hand1.value < 11:
                            self.table.hit1()
                        else:
                            self.table.resolve_game()
                if self.table.player.hand1.winner is "Croupier":
                    seriaPorazek += 1
                else:
                    seriaPorazek = 0
        except:
            return [self.table.winnings, self.table.draw, self.table.loosing, self.table.player.account_balance, self.table.blackjack]