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
                number = self.table.numberOfCards / 52
                probably = {
                    1: (4 * number) / self.table.numberOfCards,
                    2: (4 * number) / self.table.numberOfCards,
                    3: (4 * number) / self.table.numberOfCards,
                    4: (4 * number) / self.table.numberOfCards,
                    5: (4 * number) / self.table.numberOfCards,
                    6: (4 * number) / self.table.numberOfCards,
                    7: (4 * number) / self.table.numberOfCards,
                    8: (4 * number) / self.table.numberOfCards,
                    9: (4 * number) / self.table.numberOfCards,
                    10: (4 * number) / self.table.numberOfCards,
                    11: (4 * number) / self.table.numberOfCards,
                    12: (4 * number) / self.table.numberOfCards,
                    13: (4 * number) / self.table.numberOfCards
                }

                self.table.begin_game()
                czyGram = True

                oldvalue = probably[self.table.croupier.hand.value]
                probably[self.table.croupier.hand.value] = oldvalue - 1 / self.table.numberOfCards

                oldvalue = probably[self.table.player.hand1.cards[0].rank]
                probably[self.table.player.hand1.cards[0].rank] = oldvalue - 1 / self.table.numberOfCards

                oldvalue = probably[self.table.player.hand1.cards[1].rank]
                probably[self.table.player.hand1.cards[1].rank] = oldvalue - 1 / self.table.numberOfCards

                playerValue = self.table.player.hand1.value
                newcard = 0

                while self.table.player.hand1.playing is True and czyGram:
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
                        probably[newcard] = oldvalue - 1 / self.table.numberOfCards

                    else:
                        czyGram = False
                if self.table.player.hand1.playing is True:
                    self.table.resolve_game()

        except:
            return [self.table.winnings, self.table.draw, self.table.loosings, self.table.player.account_balance, self.table.blackjack]