# Znajac układ całej talii wyliczana jest idealna rozgrywka, w której gracz wygrywa najwiecej rozgrywek.

#min max
from blackjack.game.table import Table


class Idealna:
    def __init__(self, table: Table):
        self.table = table
        self.card = []

    def play(self):
        for i in self.table.decks.cards:
            self.card.append(i)

        # print(self.card)


if __name__ == '__main__':
    table = Table(1)
    Idealna(table).play()