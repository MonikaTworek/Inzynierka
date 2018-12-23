# Na podstawie kart, które zostały juz od poczatku gry uzyte wyliczane jest prawdopodobienstwo przekroczenia
# przez uzytkownika 21. Jezeli jest ono niskie gracz dobiera karte, w przeciwnym razie pasuje.
from blackjack.game.table import Table


class Prawdopodobna:
    def __init__(self, table: Table):
        self.table = table

    def play(self):
        try:
            czyGram = True
            number = len(self.table.decks.cards) / 52
            probably = {
                1: (4 * number),
                2: (4 * number),
                3: (4 * number),
                4: (4 * number),
                5: (4 * number),
                6: (4 * number),
                7: (4 * number),
                8: (4 * number),
                9: (4 * number),
                10: (4 * number),
                11: (4 * number),
                12: (4 * number),
                13: (4 * number)
            }

            while True:
                self.table.begin_game()
                czyGram = True

                oldvalue = probably[self.table.croupier.hand.value]
                probably[self.table.croupier.hand.value] = oldvalue - 1

                oldvalue = probably[self.table.player.hand1.cards[0].rank]
                probably[self.table.player.hand1.cards[0].rank] = oldvalue - 1

                oldvalue = probably[self.table.player.hand1.cards[1].rank]
                probably[self.table.player.hand1.cards[1].rank] = oldvalue - 1

                if not self.table.player.hand1.playing:
                    czyGram = False

                while self.table.player.hand1.playing and czyGram:
                    roznica = 21 - self.table.player.hand1.value
                    prawdopodobienstwo = 0
                    for i in probably.keys():
                        if i < roznica:
                            prawdopodobienstwo += probably[i]

                    prawdopodobienstwo /= len(self.table.decks.cards)

                    if prawdopodobienstwo > 0.5:
                        self.table.hit1()

                        oldvalue = probably[self.table.player.hand1.lastcard]
                        probably[self.table.player.hand1.lastcard] = oldvalue - 1

                    else:
                        czyGram = False

                if self.table.player.hand1.playing:
                    self.table.resolve_game()

        except:
            return [self.table.winnings, self.table.draw, self.table.loosing, self.table.player.account_balance, self.table.blackjack]