# Na podstawie kart, które zostały juz od poczatku gry uzyte wyliczane jest prawdopodobienstwo przekroczenia
# przez uzytkownika 21. Jezeli jest ono niskie gracz dobiera karte, w przeciwnym razie pasuje.
from blackjack.game.table import Table


class Prawdopodobna:
    def __init__(self, table: Table):
        self.table = table

    def play(self):
        try:
            czyGram = True

            while True:
                number = len(self.table.decks.cards) / 52
                probably = {
                     1: (4 * number) / len(self.table.decks.cards),
                     2: (4 * number) / len(self.table.decks.cards),
                     3: (4 * number) / len(self.table.decks.cards),
                     4: (4 * number) / len(self.table.decks.cards),
                     5: (4 * number) / len(self.table.decks.cards),
                     6: (4 * number) / len(self.table.decks.cards),
                     7: (4 * number) / len(self.table.decks.cards),
                     8: (4 * number) / len(self.table.decks.cards),
                     9: (4 * number) / len(self.table.decks.cards),
                    10: (4 * number) / len(self.table.decks.cards),
                    11: (4 * number) / len(self.table.decks.cards),
                    12: (4 * number) / len(self.table.decks.cards),
                    13: (4 * number) / len(self.table.decks.cards)
                }

                self.table.begin_game()
                czyGram = True

                oldvalue = probably[self.table.croupier.hand.value]
                probably[self.table.croupier.hand.value] = oldvalue - 1 / len(self.table.decks.cards)

                oldvalue = probably[self.table.player.hand1.cards[0].rank]
                probably[self.table.player.hand1.cards[0].rank] = oldvalue - 1 / len(self.table.decks.cards)

                oldvalue = probably[self.table.player.hand1.cards[1].rank]
                probably[self.table.player.hand1.cards[1].rank] = oldvalue - 1 / len(self.table.decks.cards)

                playerValue = self.table.player.hand1.value
                newcard = 0

                while self.table.player.hand1.playing and czyGram:
                    roznica = 21 - self.table.player.hand1.value
                    prawdopodobienstwo = 0
                    for i in probably.keys():
                        if i < roznica:
                            prawdopodobienstwo += probably[i]
                    if prawdopodobienstwo > 0.5:
                        self.table.hit1()

                        newcard = self.table.player.hand1.value - playerValue
                        playerValue = self.table.player.hand1.value

                        oldvalue = probably[newcard]
                        probably[newcard] = oldvalue - 1 / len(self.table.decks.cards)

                    else:
                        czyGram = False
                if self.table.player.hand1.playing:
                    self.table.resolve_game()

        except:
            return [self.table.winnings, self.table.draw, self.table.loosing, self.table.player.account_balance, self.table.blackjack]