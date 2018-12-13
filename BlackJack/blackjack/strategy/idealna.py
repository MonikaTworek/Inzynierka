# Znajac układ całej talii wyliczana jest idealna rozgrywka, w której gracz wygrywa najwiecej rozgrywek.

# min max
import copy
from blackjack.game.table import Table


class Idealna:
    def __init__(self, table: Table):
        self.table = table
        self.maxMoney = 0
        self.stos = []

    def play(self):
        passtable = copy.deepcopy(self.table)
        self.stos.append(Structure(copy.deepcopy(passtable), "None"))
        besttable = passtable

        ##Odkłądać na stos przed ruchem z którym chce się to zrobić

        try:
            while True:
                passtable.begin_game()
                if passtable.player.hand1.playing:
                    struct = Structure(copy.deepcopy(passtable), "Stand")
                    passtable.stand1()
                    self.stos.append(struct)
        except:
            self.maxMoney = passtable.winnings - passtable.loosing + 0.5 * passtable.blackjack

        try:
            nowtable = passtable
            while not ((len(
                    nowtable.decks.cards) < 4 or nowtable.is_finished) and self.onlyHit()):  # dopóki są karty, a ruchy to nie same hit
                if len(nowtable.decks.cards) < 4 or nowtable.is_finished:
                    if nowtable.winnings - nowtable.loosing + 0.5 * nowtable.blackjack > self.maxMoney or (nowtable.winnings - nowtable.loosing + 0.5 * nowtable.blackjack == self.maxMoney and nowtable.blackjack > besttable.blackjack):
                        besttable = nowtable
                        self.maxMoney = nowtable.winnings - nowtable.loosing + 0.5 * nowtable.blackjack
                    nowstruct = self.stos.pop()
                    while nowstruct.lastChoos is "Hit":
                        nowstruct = self.stos.pop()
                    nowtable = nowstruct.tab

                    try:
                        while not nowtable.player.hand1.playing:
                            nowtable.begin_game()
                        struct = Structure(copy.deepcopy(nowtable), "Hit")
                        nowtable.hit1()
                        self.stos.append(struct)

                    except:
                        nowtable.is_finished = True

                else:
                    try:
                        while not nowtable.player.hand1.playing:
                            nowtable.begin_game()
                        struct = Structure(copy.deepcopy(nowtable), "Stand")
                        nowtable.stand1()
                        self.stos.append(struct)
                    except:
                        nowtable.is_finished = True

            return [besttable.winnings, besttable.draw, besttable.loosing, besttable.player.account_balance, besttable.blackjack]
        except:
            return [besttable.winnings, besttable.draw, besttable.loosing, besttable.player.account_balance, besttable.blackjack]

    def onlyHit(self):
        answer = True
        for i in self.stos:
            if i.lastChoos not in ["Hit", "None"]:
                answer = False
        return answer


class Structure:
    def __init__(self, table: Table, lastchoose):
        self.lastChoos = lastchoose  # Hit, Stand, None
        self.tab = table  # kopia tablicy

        self.winn = table.winnings
        self.dra = table.draw
        self.loos = table.loosing
        self.black = table.blackjack
        self.money = table.player.account_balance  # ile pieniążków w danym momencie