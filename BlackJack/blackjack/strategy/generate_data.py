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
from blackjack.strategy.pasujaca import Pasujaca
from blackjack.strategy.podstawowa import Podstawowa
from blackjack.strategy.prawdopodobna import Prawdopodobna
from blackjack.strategy.przelam_passe import PrzelamPasse
from blackjack.strategy.przetrzymaj_passe import PrzetrzymajPasse
from blackjack.strategy.reaguj_na_bank import Bank
from blackjack.strategy.zalezna_od_szczescia import Zalezna

Score = namedlist("score", ["name", "winnings", "draw", "loosing", "money", "blackjack"])


class Generate:
    def game(table: Table, with_perfect: bool):
        score = []

        explist = Ekspans(copy.deepcopy(table)).play()
        score.append(Score(name="Ekspansyjna", winnings=explist[0], draw=explist[1], loosing=explist[2], money=explist[3], blackjack=explist[4]))

        bank = Bank(copy.deepcopy(table)).play()
        score.append(Score(name="ReagujNaBank", winnings=bank[0], draw=bank[1], loosing=bank[2], money=bank[3], blackjack=bank[4]))

        hilow = HiLow(copy.deepcopy(table)).play()
        score.append(Score(name="HILow", winnings=hilow[0], draw=hilow[1], loosing=hilow[2], money=hilow[3], blackjack=hilow[4]))

        intuicja = Intuicyjna(copy.deepcopy(table)).play()
        score.append(Score(name="Intuicyjna", winnings=intuicja[0], draw=intuicja[1], loosing=intuicja[2], money=intuicja[3], blackjack=intuicja[4]))

        neverbust = NeverBust(copy.deepcopy(table)).play()
        score.append(Score(name="NeverBust", winnings=neverbust[0], draw=neverbust[1], loosing=neverbust[2], money=neverbust[3], blackjack=neverbust[4]))

        prawdopodobna = Prawdopodobna(copy.deepcopy(table)).play()
        score.append(Score(name="NeverBust", winnings=prawdopodobna[0], draw=prawdopodobna[1], loosing=prawdopodobna[2], money=prawdopodobna[3], blackjack=prawdopodobna[4]))

        przelam = PrzelamPasse(copy.deepcopy(table)).play()
        score.append(Score(name="PrzelamPasse", winnings=przelam[0], draw=przelam[1], loosing=przelam[2], money=przelam[3], blackjack=przelam[4]))

        przetrzym = PrzetrzymajPasse(copy.deepcopy(table)).play()
        score.append(Score(name="PrzetrzymajPasse", winnings=przetrzym[0], draw=przetrzym[1], loosing=przetrzym[2], money=przetrzym[3],blackjack=przetrzym[4]))

        pod = Podstawowa(copy.deepcopy(table)).play()
        score.append(Score(name="Podstawowa", winnings=pod[0], draw=pod[1], loosing=pod[2], money=pod[3], blackjack=pod[4]))

        zalez = Zalezna(copy.deepcopy(table)).play()
        score.append(Score(name="ZaleznaOdSzczescia", winnings=zalez[0], draw=zalez[1], loosing=zalez[2], money=zalez[3], blackjack=zalez[4]))

        passing = Pasujaca(copy.deepcopy(table)).play()
        score.append(Score(name="Pasujaca", winnings=passing[0], draw=passing[1], loosing=passing[2], money=passing[3], blackjack=passing[4]))

        if with_perfect:
            ideal = Idealna(copy.deepcopy(table)).play()
            score.append(Score(name="Idealna", winnings=ideal[0], draw=ideal[1], loosing=ideal[2], money=ideal[3], blackjack=ideal[4]))
        else:
            score.append(Score(name="Idealna", winnings=0, draw=0, loosing=0, money=0, blackjack=0))

        return score

    @staticmethod
    def generate(series: int, numberTalii: int, wiht_perfect: bool):
        eksp = Score(name="Ekspansyjna", winnings=0, draw=0, loosing=0, money=0, blackjack=0)
        banks = Score(name="ReagujNaBank", winnings=0, draw=0, loosing=0, money=0, blackjack=0)
        hilows = Score(name="HiLow", winnings=0, draw=0, loosing=0, money=0, blackjack=0)
        int = Score(name="Intuicyjna", winnings=0, draw=0, loosing=0, money=0, blackjack=0)
        krupier = Score(name="Krupierska", winnings=0, draw=0, loosing=0, money=0, blackjack=0)
        neverbust = Score(name="NeverBust", winnings=0, draw=0, loosing=0, money=0, blackjack=0)
        prawdopodobna = Score(name="Prawdopodobna", winnings=0, draw=0, loosing=0, money=0, blackjack=0)
        przelampasse = Score(name="PrzelamPasse", winnings=0, draw=0, loosing=0, money=0, blackjack=0)
        przetrzymajpasse = Score(name="PrzetrzymajPasse", winnings=0, draw=0, loosing=0, money=0, blackjack=0)
        zalezna = Score(name="ZaleznaOdSzczescia", winnings=0, draw=0, loosing=0, money=0, blackjack=0)
        podstaw = Score(name="Podstawowa", winnings=0, draw=0, loosing=0, money=0, blackjack=0)
        passing = Score(name="Pasujaca", winnings=0, draw=0, loosing=0, money=0, blackjack=0)
        idealna = Score(name="Idealna", winnings=0, draw=0, loosing=0, money=0, blackjack=0)

        for _ in range(series):
            table = Table(numberTalii)

            explist = Ekspans(copy.deepcopy(table)).play()
            packing(eksp, explist)

            bank = Bank(copy.deepcopy(table)).play()
            packing(banks, bank)

            hilow = HiLow(copy.deepcopy(table)).play()
            packing(hilows, hilow)

            intuicja = Intuicyjna(copy.deepcopy(table)).play()
            packing(int, intuicja)

            krupierska = Krupier(copy.deepcopy(table)).play()
            packing(krupier, krupierska)

            nvbust = NeverBust(copy.deepcopy(table)).play()
            packing(neverbust, nvbust)

            prob = Prawdopodobna(copy.deepcopy(table)).play()
            packing(prawdopodobna, prob)

            przelam = PrzelamPasse(copy.deepcopy(table)).play()
            packing(przelampasse, przelam)

            przetrzym = PrzetrzymajPasse(copy.deepcopy((table))).play()
            packing(przetrzymajpasse, przetrzym)

            zalez = Zalezna(copy.deepcopy((table))).play()
            packing(zalezna, zalez)

            pod = Podstawowa(copy.deepcopy(table)).play()
            packing(podstaw, pod)

            passlol = Pasujaca(copy.deepcopy(table)).play()
            packing(passing, passlol)

            if wiht_perfect:
                id = Idealna(copy.deepcopy(table)).play()
                packing(idealna, id)

        path = "C:\\Users\\Public\\score_series" + str(series) + "_DeckOfCard" + str(numberTalii) + "_" + str(datetime.date.today()) + ".txt"

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
        f.write(str(podstaw) + "\n")
        f.write(str(passing) + "\n")
        f.write(str(idealna) + "\n")
        f.close()


def packing(score: Score, list: []):
    score.winnings += list[0]
    score.draw += list[1]
    score.loosing += list[2]
    score.money += list[3]
    score.blackjack += list[4]


if __name__ == '__main__':
    Generate.generate(1, 3, True)

