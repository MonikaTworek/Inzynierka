from functools import wraps
from namedlist import namedlist

from blackjack.game.decks import Decks
from blackjack.game.exceptions import InvalidMove
from blackjack.game.players import Player, Croupier

State = namedlist("State", ["phase", "bid", "winnings"])
account_balance = 100
bid = 10


def action(from_phases, to_phase):
    def decorator(foo):
        @wraps(foo)
        def wrapper(self, *args, **kw):
            # Do not allow execution of command if not in proper phase
            if self.state.phase not in from_phases:
                raise InvalidMove("Not in proper phase")

            # Execute action and switch to target phase
            foo(self, *args, **kw)
            self.state.phase = to_phase

            # Switch if other hand is still playing, resolve if none is
            if not self.player.hand.playing:
                if self.player.other_hand.playing:
                    self.player.switch_hand()
                else:
                    self.resolve_game()

        return wrapper

    return decorator


class Table:
    def __init__(self):
        self.state = State(phase="awaiting", winnings=0)
        self.player = Player(account_balance)
        self.croupier = Croupier()
        self.decks = Decks()
        self.winnings = 0
        self.draw = 0
        self.loosings = 0
        self.is_insure = False

    def resolve_game(self):
        self.state.phase = "end_game"

        croupier_hand = self.croupier.hand
        croupier_hand.cards[0].face_up = True
        croupier_hand.cards[1].face_up = True

        valid_hands = (x for x in self.player.hands if 0 < x.value <= 21)
        invalid_hands_none = (x for x in self.player.hands if x.value == 0)
        invalid_hands = (x for x in self.player.hands if x.value > 21)

        for player_hand in invalid_hands_none:
            player_hand.winner = "Croupier"

        for player_hand in invalid_hands:
            player_hand.winner = "Croupier"
            self.loosings += 1

        if croupier_hand.has_blackjack and self.is_insure:
            self.player.account_balance += bid
#za blackjack jest 1.5 stawki
        for player_hand in valid_hands:
            if croupier_hand.has_blackjack and player_hand.has_blackjack:
                self.draw += 1
                multiplier = 1
                player_hand.winner = "Draw"
            elif croupier_hand.has_blackjack:
                multiplier = 0
                self.loosings += 1
                player_hand.winner = "Croupier"
            elif player_hand.has_blackjack:
                multiplier = 2
                self.winnings += 1
                player_hand.winner = "Player"
            else:
                # No blackjack scenario
                # Croupier has defined strategy
                while croupier_hand.value <= 16:
                    croupier_hand.add(self.decks.get())
                if croupier_hand.value > 21 or player_hand.value > croupier_hand.value:
                    multiplier = 2
                    player_hand.winner = "Player"
                elif player_hand.value == croupier_hand.value:
                    multiplier = 1
                    player_hand.winner = "Draw"
                else:
                    multiplier = 0
                    player_hand.winner = "Croupier"

            self.state.winnings += self.state.bid * multiplier
        self.player.account_balance += self.state.winnings
        self.state.phase = "end_game"

    @action(from_phases=("awaiting", "end_game"), to_phase="begin_game")
    def begin_game(self):
        self.croupier.clear()
        self.player.clear()

        self.is_insure = False
        self.player.balance -= bid
        self.state.winnings = 0

        #TODO: a co jak sie kosnczyly karty?

        self.croupier.hand.add(self.decks.get(), face_up=False)
        self.croupier.hand.add(self.decks.get(), face_up=True)
        self.player.hand.add(self.decks.get(), face_up=True)
        self.player.hand.add(self.decks.get(), face_up=True)

        if self.player.hand.value >= 21:
            self.player.hand.playing = False

    @action(from_phases=("begin_game", "in_game"), to_phase="in_game")
    def hit(self):
        self.player.hand.add(self.decks.get(), face_up=True)
        # TODO: a co jak sie kosnczyly karty?
        if self.player.hand.value >= 21:
            self.player.hand.playing = False

    @action(from_phases=("begin_game", "in_game"), to_phase="in_game")
    def stand(self):
        self.player.hand.playing = False

    @action(from_phases=("begin_game",), to_phase="in_game")
    def double_down(self):
        self.player.balance -= self.state.bid
        self.state.bid *= 2
        self.player.hand.add(self.decks.get(), face_up=True)
        self.player.hand.playing = False

    @action(from_phases=("begin_game",), to_phase="in_game")
    def split(self):
        first_hand, second_hand = self.player.hands
        if not (first_hand.is_empty or second_hand.is_empty):
            raise InvalidMove("Already did split")

        if first_hand.cards[0].rank != first_hand.cards[1].rank:
            raise InvalidMove("Cannot split cards")

        self.player.balance -= self.state.bid
        second_hand.add(first_hand.cards.pop())
        first_hand.add(self.decks.get(), face_up=True)
        second_hand.add(self.decks.get(), face_up=True)

    @action(from_phases=("begin_game",), to_phase="in_game")
    def insure(self):
        if self.croupier.hand.can_insure:
            self.player.balance -= 0.5 * bid
            self.is_insure = True
        else:
            raise InvalidMove("You cannot insure!")

    @action(from_phases=("in_game",), to_phase="begin_game")
    def surrender(self):
        self.loosings += 1
