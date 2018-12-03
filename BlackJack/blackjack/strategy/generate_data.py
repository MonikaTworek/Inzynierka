import copy
import datetime

from namedlist import namedlist

from blackjack.game.table import Table

from blackjack.strategy.Hi_Low import HiLow
from blackjack.strategy.Intuicyjna import Intuicyjna
from blackjack.strategy.ekspansyjna import Ekspans
from blackjack.strategy.idealna import Idealna
from blackjack.strategy.krupierska import Krupier
from blackjack.strategy.never_bust import NeverBust
from blackjack.strategy.prawdopodobna import Prawdopodobna
from blackjack.strategy.przelam_passe import PrzelamPasse
from blackjack.strategy.przetrzymaj_passe import PrzetrzymajPasse
from blackjack.strategy.reaguj_na_bank import Bank
from blackjack.strategy.zalezna_od_szczescia import Zalezna

Score = namedlist("score", ["name", "winning", "draw", "loosing", "money", "blackjack"])


class Generate:
    def game(self, table: Table):
        score = []
        explist = Ekspans(copy.deepcopy(table)).play()
        score.append(Score(name="Ekspansyjna", winning=explist[0], draw=explist[1], loosing=explist[2], money=explist[3], blackjack=explist[4]))

        bank = Bank(copy.deepcopy(table)).play()
        score.append(Score(name="ReagujNaBank", winning=bank[0], draw=bank[1], loosing=bank[2], money=bank[3], blackjack=bank[4]))

        hilow = HiLow(copy.deepcopy(table)).play()
        score.append(Score(name="HILow", winning=hilow[0], draw=hilow[1], loosing=hilow[2], money=hilow[3], blackjack=hilow[4]))

        intuicja = Intuicyjna(copy.deepcopy(table)).play()
        score.append(Score(name="Intuicyjna", winning=intuicja[0], draw=intuicja[1], loosing=intuicja[2], money=intuicja[3], blackjack=intuicja[4]))

        neverbust = NeverBust(copy.deepcopy(table)).play()
        score.append(Score(name="NeverBust", winning=neverbust[0], draw=neverbust[1], loosing=neverbust[2], money=neverbust[3], blackjack=neverbust[4]))

        prawdopodobna = Prawdopodobna(copy.deepcopy(table)).play()
        score.append(Score(name="NeverBust", winning=prawdopodobna[0], draw=prawdopodobna[1], loosing=prawdopodobna[2], money=prawdopodobna[3], blackjack=prawdopodobna[4]))

        przelam = PrzelamPasse(copy.deepcopy(table)).play()
        score.append(Score(name="PrzelamPasse", winning=przelam[0], draw=przelam[1], loosing=przelam[2], money=przelam[3], blackjack=przelam[4]))

        przetrzym = PrzetrzymajPasse(copy.deepcopy(table)).play()
        score.append(Score(name="PrzetrzymajPasse", winning=przetrzym[0], draw=przetrzym[1], loosing=przetrzym[2], money=przetrzym[3],blackjack=przetrzym[4]))

        zalez = Zalezna(copy.deepcopy(table)).play()
        score.append(Score(name="ZaleznaOdSzczescia", winning=zalez[0], draw=zalez[1], loosing=zalez[2], money=zalez[3], blackjack=zalez[4]))

        return score

    @staticmethod
    def generate(series: int, number: int):
        eksp = Score(name="Ekspansyjna", winning=0, draw=0, loosing=0, money=0, blackjack=0)
        banks = Score(name="ReagujNaBank", winning=0, draw=0, loosing=0, money=0, blackjack=0)
        hilows = Score(name="HiLow", winning=0, draw=0, loosing=0, money=0, blackjack=0)
        int = Score(name="Intuicyjna", winning=0, draw=0, loosing=0, money=0, blackjack=0)
        krupier = Score(name="Krupierska", winning=0, draw=0, loosing=0, money=0, blackjack=0)
        neverbust = Score(name="NeverBust", winning=0, draw=0, loosing=0, money=0, blackjack=0)
        prawdopodobna = Score(name="Prawdopodobna", winning=0, draw=0, loosing=0, money=0, blackjack=0)
        przelampasse = Score(name="PrzelamPasse", winning=0, draw=0, loosing=0, money=0, blackjack=0)
        przetrzymajpasse = Score(name="PrzetrzymajPasse", winning=0, draw=0, loosing=0, money=0, blackjack=0)
        zalezna = Score(name="ZaleznaOdSzczescia", winning=0, draw=0, loosing=0, money=0, blackjack=0)
        idealna = Score(name="Idealna", winning=0, draw=0, loosing=0, money=0, blackjack=0)

        for _ in range(series):
            table = Table(number)

            explist = Ekspans(copy.deepcopy(table)).play()
            eksp.winning += explist[0]
            eksp.draw += explist[1]
            eksp.loosing += explist[2]
            eksp.money += explist[3]
            eksp.blackjack += explist[4]

            bank = Bank(copy.deepcopy(table)).play()
            banks.winning += bank[0]
            banks.draw += bank[1]
            banks.loosing += bank[2]
            banks.money += bank[3]
            banks.blackjack += bank[4]

            hilow = HiLow(copy.deepcopy(table)).play()
            hilows.winning += hilow[0]
            hilows.draw += hilow[1]
            hilows.loosing += hilow[2]
            hilows.money += hilow[3]
            hilows.blackjack += hilow[4]

            intuicja = Intuicyjna(copy.deepcopy(table)).play()
            int.winning += intuicja[0]
            int.draw += intuicja[1]
            int.loosing += intuicja[2]
            int.money += intuicja[3]
            int.blackjack += intuicja[4]

            krupierska = Krupier(copy.deepcopy(table)).play()
            krupier.winning += krupierska[0]
            krupier.draw += krupierska[1]
            krupier.loosing += krupierska[2]
            krupier.money += krupierska[3]
            krupier.blackjack += krupierska[4]

            nvbust = NeverBust(copy.deepcopy(table)).play()
            neverbust.winning += nvbust[0]
            neverbust.draw += nvbust[1]
            neverbust.loosing += nvbust[2]
            neverbust.money += nvbust[3]
            neverbust.blackjack += nvbust[4]

            prob = Prawdopodobna(copy.deepcopy(table)).play()
            prawdopodobna.winning += prob[0]
            prawdopodobna.draw += prob[1]
            prawdopodobna.loosing += prob[2]
            prawdopodobna.money += prob[3]
            prawdopodobna.blackjack += prob[4]

            przelam = PrzelamPasse(copy.deepcopy(table)).play()
            przelampasse.winning += przelam[0]
            przelampasse.draw += przelam[1]
            przelampasse.loosing += przelam[2]
            przelampasse.money += przelam[3]
            przelampasse.blackjack += przelam[4]

            przetrzym = PrzetrzymajPasse(copy.deepcopy((table))).play()
            przetrzymajpasse.winning += przetrzym[0]
            przetrzymajpasse.draw += przetrzym[1]
            przetrzymajpasse.loosing += przetrzym[2]
            przetrzymajpasse.money += przetrzym[3]
            przetrzymajpasse.blackjack += przetrzym[4]

            zalez = Zalezna(copy.deepcopy((table))).play()
            zalezna.winning += zalez[0]
            zalezna.draw += zalez[1]
            zalezna.loosing += zalez[2]
            zalezna.money += zalez[3]
            zalezna.blackjack += zalez[4]

            # id = Idealna(copy.deepcopy(table)).play()
            # idealna.winning += id[0]
            # idealna.draw += id[1]
            # idealna.loosing += id[2]
            # idealna.money += id[3]
            # idealna.blackjack += id[4]

        path = "C:\\Users\\Public\\score_series" + str(series) + "_" + str(datetime.date.today()) + ".txt"

        f = open(path, "w+")
        f.write(str(eksp) + "\n")
        f.write(str(banks) + "\n")
        f.write(str(hilows) + "\n")
        f.write(str(int) + "\n")
        f.write(str(krupier) + "\n")
        f.write(str(neverbust) + "\n")
        f.write(str(prawdopodobna) + "\n")
        f.write(str(przelampasse) + "\n")
        f.write(str(przetrzymajpasse) + "\n")
        f.write(str(zalezna) + "\n")
        f.write(str(idealna) + "\n")
        f.close()


if __name__ == '__main__':
    Generate.generate(10, 1)

# dziwne wyniki - malo gier ma
# Intuicyjna

