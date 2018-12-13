# Losowana jest liczba z przedziału 0-100. Jezeli zostanie wynik jest nizszy niz 50% to uzytkownik przestaje
# dobierac karty.
from random import Random
from blackjack.game.table import Table


class Intuicyjna:
    def __init__(self, table: Table):
        self.table = table
        self.random = Random()

    def play(self):
        try:
            while True:
                self.table.begin_game()
                while self.table.player.hand1.playing and self.random.randint(0, 100) > 50:
                    self.table.hit1()
                if self.table.player.hand1.playing:
                    self.table.resolve_game()
        except:
            return [self.table.winnings, self.table.draw, self.table.loosing, self.table.player.account_balance, self.table.blackjack]