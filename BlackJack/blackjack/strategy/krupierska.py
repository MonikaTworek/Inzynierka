# Jest to ta sama strategia według której gra krupier. Jezeli ma 16 punktów lub mniej w kartach musi
# dociagnac karte. W przypadku gdy ma 17 i wiecej nie dobiera kart bez wzgledu na to ile punktów ma gracz.
from blackjack.game.table import Table


class Krupier:
    def __init__(self, table: Table):
        self.table = table

    def play(self):
        try:
            while True:
                self.table.begin_game()
                while self.table.player.hand1.playing is True and self.table.player.hand1.value < 17:
                    self.table.hit1()
                if self.table.player.hand1 is True:
                    self.table.resolve_game()
        except:
            return [self.table.winnings, self.table.draw, self.table.loosings, self.table.player.account_balance, self.table.blackjack]