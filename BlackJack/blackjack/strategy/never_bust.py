# Jest bardzo podobna do strategii krupierskiej, ale gracz przestaje dobierac karty gdy ma wiecej niz 11
# punktów.
from blackjack.game.table import Table


class NeverBust:
    def __init__(self, table: Table):
        self.table = table

    def play(self):
        try:
            while True:
                self.table.begin_game()
                while self.table.player.hand1.playing is True and self.table.player.hand1.value < 11:
                    self.table.hit1()
                if self.table.player.hand1.playing is True:
                    self.table.resolve_game()
        except:
            return [self.table.winnings, self.table.draw, self.table.loosings, self.table.player.account_balance, self.table.blackjack]