import copy
from functools import wraps

from jsonschema import validate, ValidationError
from flask import Flask, request, jsonify

from blackjack.game.table import Table, InvalidMove
from blackjack.schemas import schemas
from blackjack.describe import table_to_dict, score_to_dict
from blackjack.strategy.generate_data import Generate

app = Flask(__name__)

tables = {}
scores = {}


def validate_schema(schema_name):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kw):
            validate(request.json, schema=schemas[schema_name])
            return f(*args, **kw)

        return wrapper

    return decorator


@app.errorhandler(ValidationError)
@app.errorhandler(InvalidMove)
def handle_exception(exception):
    response = jsonify({"header": "error", "message": exception.message})
    response.status_code = 400
    return response


@app.route('/register', methods=['POST'])
@validate_schema('register')
def register():
    number = request.json["numberof"]
    uid = max(tables) + 1 if tables else 0
    tables[uid] = Table(number)
    if number > 1:
        with_perfect = False
    else:
        with_perfect = True
    scores[uid] = Generate.game(copy.deepcopy(tables[uid]), with_perfect) ###zrobić to na wątku
    return jsonify({"header": "confirm_register", "uid": uid})


@app.route('/generate', methods=['POST'])
@validate_schema('generate')
def generate():
    number = request.json["numberof"]
    if number > 2 :
        with_perfect = False
    else:
        with_perfect = True
    Generate.generate(1, number, with_perfect)

    return jsonify({"header": "success", "tekst": "data was generate in C: Users Public"})


@app.route('/player/<int:uid>/begin', methods=['POST'])
@validate_schema('begin_game')
def begin_game(uid: int):
    tables[uid].begin_game()

    table_dict = table_to_dict(tables[uid])
    table_dict["header"] = "success"
    return jsonify(table_dict)


@app.route('/player/<int:uid>/action', methods=['POST'])
@validate_schema('action_in_game')
def make_action(uid: int):
    actions = {
        "split": Table.split,
        "double_down": Table.double_down,
        "stand1": Table.stand1,
        "stand2": Table.stand2,
        "hit1": Table.hit1,
        "hit2": Table.hit2,
        "end_game": Table.finish_game,
        "insure": Table.insure,
        "surrender": Table.surrender
    }
    actions[request.json["action"]](tables[uid])

    table_dict = table_to_dict(tables[uid])
    table_dict["header"] = "success"
    return jsonify(table_dict)


@app.route('/player/<int:uid>/finish', methods=['POST'])
@validate_schema('finish_game')
def finish_game(uid: int):
    try:
        tables[uid].finish_game()
    except:
        print("FIINISH")
    score_dict = score_to_dict(tables[uid], scores[uid])
    score_dict["header"] = "success"
    return jsonify(score_dict)
