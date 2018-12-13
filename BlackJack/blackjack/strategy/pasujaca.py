#Zawsze pasujemy - liczymy na przebicie krupiera
from blackjack.game.table import Table


class Pasujaca:
    def __init__(self, table: Table):
        self.table = table

    def play(self):
        try:
            while True:
                self.table.begin_game()
                if self.table.player.hand1.playing:
                    self.table.stand1()
        except:
            return [self.table.winnings, self.table.draw, self.table.loosing, self.table.player.account_balance, self.table.blackjack]