from blackjack.game.decks import Card
from blackjack.game.players import Hand
from blackjack.game.table import Player, Croupier, State, Table
from blackjack.strategy.generate_data import Score


def card_to_dict(card: Card):
    return {
        "color": card.color if card.face_up else "face_down",
        "rank": card.rank if card.face_up else "face_down"
    }


def hand_to_dict(hand: Hand):
    return {
        "cards": [card_to_dict(card) for card in hand.cards],
        "value": hand.value,
        "playing": hand.playing,
        "winner": hand.winner
    }


def player_to_dict(player: Player):
    return {
        "hands1": hand_to_dict(player.hands1),
        "hands2": hand_to_dict(player.hands2),
        "account_balance": player.account_balance
    }


def croupier_to_dict(croupier: Croupier):
    return {
        "hand": hand_to_dict(croupier.hand)
    }


def state_to_dict(state: State):
    return {
        "phase": state.phase,
        "bid": state.bid,
        "winnings": state.winnings
    }


def player_score_to_dict(table: Table):
    return {
        "winning": table.winnings,
        "draw": table.draw,
        "loosing": table.loosings
    }


def bot_result(score: Score):
    return {
        "winning": score.winnings,
        "draw": score.draw,
        "loosing": score.loosings
    }


def bot_score_to_dict(score: Score):
    return {
        "name": score.name,
        "score": bot_result(score)
    }


def table_to_dict(table: Table):
    return {
        "state": state_to_dict(table.state),
        "player": player_to_dict(table.player),
        "croupier": croupier_to_dict(table.croupier)
    }


def score_to_dict(table: Table, scoreslist):
    return {
        "player_score": player_score_to_dict(table),
        "bots_score": [bot_score_to_dict(bot) for bot in scoreslist]
    }
