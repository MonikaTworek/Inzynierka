# Kiedy gracz ma miedzy 15, a 21 przestaje dobierac karty. Z kazdym zwyciestwem dolna granica kiedy
# gracz przestaje dobierac karty jest zwiekszana co 1 az do 20. Z kazda porazka dolna granica jest obnizana o
# 1 az do 11.
from blackjack.game.table import Table


class Zalezna:
    def __init__(self, table: Table):
        self.table = table

    def play(self):
        seriaPorazek = 0
        zaleznosc = {
            -4 : 11,
            -3 : 12,
            -2 : 13,
            -1 : 14,
             0 : 15,
             1 : 16,
             2 : 17,
             3 : 18,
             4 : 19,
             5 : 20,
             6 : 21
        }
        try:
            while True:
                self.table.begin_game()
                while self.table.player.hand1.playing:
                    if self.table.player.hand1.value < zaleznosc[seriaPorazek]:
                        self.table.hit1()
                    else:
                        self.table.resolve_game()

                if self.table.player.hand1.winner is "Croupier":
                    if seriaPorazek < -4 :
                        seriaPorazek = -4
                    else:
                        seriaPorazek -= 1
                else:
                    if seriaPorazek > 6 :
                        seriaPorazek = 6
                    else:
                        seriaPorazek += 1
        except:
            return [self.table.winnings, self.table.draw, self.table.loosing, self.table.player.account_balance, self.table.blackjack]