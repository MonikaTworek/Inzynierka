import copy

from namedlist import namedlist

from blackjack.game.table import Table
from blackjack.strategy import ekspansyjna
from blackjack.strategy.ekspansyjna import Ekspans

Score = namedlist("score", ["name", "winning", "draw", "loosing"])

class Generate:
    def game(self, table: Table):
        score = []
        explist = Ekspans(copy.deepcopy(table)).play()
        score.append(Score(name = "Ekspansyjna", winning = explist[0], draw = explist[1], loosing = explist[2]))

        return score

    def generate(self, series: int, number: int):
        winnigsEksp = 0
        drawEksp = 0
        loosEksp = 0

        for _ in range(series):
            table = Table(number)
            ekspansyjna = Ekspans(table)
            explist = ekspansyjna.play()
            winnigsEksp += explist[0]
            drawEksp += explist[1]
            loosEksp += explist[2]

        f = open("C:\\Users\\Public\\eksp.txt", "w+")
        f.write("Winning " + str(winnigsEksp) + "\n")
        f.write("Draw " + str(drawEksp) + "\n")
        f.write("Loosing " + str(loosEksp) + "\n")
        f.close()
