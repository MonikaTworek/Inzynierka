from blackjack.game.decks import Decks
from blackjack.game.exceptions import InvalidMove
from blackjack.game.players import Player, Croupier


class Table:
    def __init__(self, number: int = 1):
        self.phase = "awaiting"
        self.statewin = 0
        self.statebid = 0
        self.decks = Decks(number)
        self.winnings = 0
        self.draw = 0
        self.loosing = 0
        self.is_insure = False
        self.bid = 10
        self.player = Player()
        self.croupier = Croupier()
        self.is_finished = False
        self.blackjack = 0
        self.is_perfect = False

    def finish_game(self):
        self.is_finished = True
        self.player.account_balance += self.bid

        raise InvalidMove("You finish")

    def resolve_game(self):
        self.phase = "end_game"

        self.player.hand1.playing = False
        self.player.hand2.playing = False

        croupier_hand = self.croupier.hand
        croupier_hand.cards[0].face_up = True
        croupier_hand.cards[1].face_up = True

        valid_hands = (x for x in self.player.hands if 0 < x.value <= 21)
        invalid_hands_none = (x for x in self.player.hands if x.value == 0)
        invalid_hands = (x for x in self.player.hands if x.value > 21)

        for player_hand in invalid_hands_none:
            player_hand.winner = "None"

        for player_hand in invalid_hands:
            player_hand.winner = "Croupier"
            self.loosing += 1

        if croupier_hand.has_blackjack and self.is_insure:
            self.player.account_balance += self.bid

        for player_hand in valid_hands:
            if croupier_hand.has_blackjack and player_hand.has_blackjack:
                self.winnings += 1
                multiplier = 2.5
                player_hand.winner = "Player"
                self.blackjack += 1
            elif croupier_hand.has_blackjack:
                multiplier = 0
                self.loosing += 1
                player_hand.winner = "Croupier"
            elif player_hand.has_blackjack:
                multiplier = 2.5
                self.winnings += 1
                player_hand.winner = "Player"
                self.blackjack += 1
            else:
                # No blackjack scenario
                # Croupier has defined strategy
                while croupier_hand.value <= 16:
                    if len(self.decks.cards) < 1:
                        self.draw += 1
                        self.finish_game()
                    else:
                        croupier_hand.add(self.decks.get())
                self.decks.up()
                if croupier_hand.value > 21 or player_hand.value > croupier_hand.value:
                    multiplier = 2
                    player_hand.winner = "Player"
                    self.winnings += 1
                elif player_hand.value == croupier_hand.value:
                    multiplier = 1
                    player_hand.winner = "Draw"
                    self.draw += 1
                else:
                    multiplier = 0
                    player_hand.winner = "Croupier"
                    self.loosing += 1

            self.statewin += self.statebid * multiplier
        self.player.account_balance += self.statewin
        self.phase = "end_game"

    def begin_game(self):
        if self.phase not in ["awaiting", "end_game"]:
            print("Not in proper phase. You cannot begin!")
            raise InvalidMove("Not in proper phase. You cannot begin game!")
        self.croupier.clear()
        self.player.clear()
        self.phase = "begin_game"

        self.is_insure = False
        self.player.account_balance -= self.bid
        self.statewin = 0
        self.statebid = self.bid

        if len(self.decks.cards) < 4:
            self.phase = "end_game"
            self.finish_game()

        else:
            self.croupier.hand.add(self.decks.get(), face_up=False)
            self.croupier.hand.add(self.decks.get(), face_up=True)
            self.player.hands1.add(self.decks.get(), face_up=True)
            self.player.hands1.add(self.decks.get(), face_up=True)
            self.decks.up()

            if self.player.hands1.value >= 21:
                self.player.hands1.playing = False
                self.resolve_game()

    def hit1(self):
        if self.phase not in ["in_game", "begin_game"]:
            print("Not in proper phase. You cannot hit1!")
            raise InvalidMove("Not in proper phase. You cannot hit!")
        if self.player.hands1.playing is False:
            print("Not have card. You cannot hit1!")
            raise InvalidMove("Not in proper phase")

        if len(self.decks.cards) < 1:
            self.phase = "end_game"
            self.finish_game()

        else:
            self.player.hands1.add(self.decks.get(), face_up=True)
            self.decks.up()
            if self.player.hands1.value >= 21:
                self.player.hands1.playing = False
                if self.player.hands2.playing is False:
                    self.resolve_game()
                else:
                    self.phase = "in_game"
            else:
                self.phase = "in_game"

    def hit2(self):
        if self.phase not in ["in_game", "begin_game"]:
            print("Not in proper phase. You cannot hit2!")
            raise InvalidMove("Not in proper phase. You cannot hit!")
        if self.player.hands1.playing is False:
            print("Not have caard. You cannot hit2!")
            raise InvalidMove("Hand is empty")

        if len(self.decks.cards) < 1:
            self.phase = "end_game"
            self.finish_game()

        else:
            self.player.hands2.add(self.decks.get(), face_up=True)
            self.decks.up()
            if self.player.hands2.value >= 21:
                self.player.hands2.playing = False
                if self.player.hands1.playing is False:
                    self.resolve_game()
                else:
                    self.phase = "in_game"
            else:
                self.phase = "in_game"

    def stand1(self):
        if self.phase not in ["in_game", "begin_game"]:
            print("Not in proper phase. You cannot stand2!")
            raise InvalidMove("Not in proper phase. You cannot stand!")

        self.player.hands1.playing = False
        if self.player.hands2.playing is False:
            self.resolve_game()
        else:
            self.phase = "in_game"

    def stand2(self):
        if self.phase not in ["in_game", "begin_game"]:
            print("Not in proper phase. You cannot stand2!")
            raise InvalidMove("Not in proper phase. You cannot stand!")

        self.player.hands2.playing = False
        if self.player.hands1.playing is False:
            self.resolve_game()
        else:
            self.phase = "in_game"

    def double_down(self):
        if self.phase is not "begin_game":
            print("Not in proper phase. You cannot double down!")
            raise InvalidMove("Not in proper phase. You cannot double down!")
        if len(self.decks.cards) < 1:
            self.phase = "end_game"
            self.finish_game()

        else:
            self.player.account_balance -= self.bid
            self.statebid *= 2
            self.player.hands1.add(self.decks.get(), face_up=True)
            self.decks.up()
            self.player.hands1.playing = False
            self.resolve_game()

    def split(self):
        if self.phase is not "begin_game":
            print("Not in proper phase. You cannot split!")
            raise InvalidMove("Not in proper phase. You cannot split!")

        first_hand, second_hand = self.player.hands
        if not (first_hand.is_empty or second_hand.is_empty):
            print("Already did split")
            raise InvalidMove("Already did split")

        if first_hand.cards[0].rank != first_hand.cards[1].rank:
            print("Cannot split cards")
            raise InvalidMove("Cannot split cards")

        if len(self.decks.cards) < 3:
            self.phase = "end_game"
            self.finish_game()

        else:
            self.player.account_balance -= self.bid
            second_hand.add(first_hand.cards.pop())
            first_hand.add(self.decks.get(), face_up=True)
            second_hand.add(self.decks.get(), face_up=True)
            self.decks.up()

            self.phase = "in_game"

    def insure(self):
        if self.phase is not "begin_game":
            raise InvalidMove("Not in proper phase. You cannot insure!")

        if self.croupier.hand.can_insure:
            self.player._balance -= 0.5 * self.bid
            self.is_insure = True
        else:
            raise InvalidMove("You cannot insure!")

    def surrender(self):
        self.loosing += 1
        self.phase = "end_game"
