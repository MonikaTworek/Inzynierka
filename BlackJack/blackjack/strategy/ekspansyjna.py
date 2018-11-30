# Strategia ta dazy do jak najblizszej wartosci 21. Gracz dobiera karte dopóki nie ma co najmniej 20 oczek.
from blackjack.game.table import Table


class Ekspans:
    def __init__(self, table: Table):
        self.table = table

    def play(self):
        try:
            while True:
                self.table.begin_game()
                while self.table.player.hand1.playing is True and self.table.player.hand1.value < 20:
                    self.table.hit1()
                if self.table.player.hand1 is True:
                    self.table.resolve_game()
        except:
            return [self.table.winnings, self.table.draw, self.table.loosings, self.table.player.account_balance, self.table.blackjack]
