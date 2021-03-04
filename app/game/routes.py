from http import HTTPStatus as status
from flask import Blueprint, make_response, jsonify
from app import db
import concurrent.futures

from app.models import Table, Player
from .services.game_service import GameService

game = Blueprint('game', __name__)


@game.route('/basic-game/simulate', methods=['GET'])
def simulate():
    table = db.session.query(Table).all()[0]
    properties = table.properties.all()
    players = db.session.query(Player).all()

    results = []
    for i in range(0,300):
        service = GameService(properties, players)
        results.append(service.run())

    return make_response(
        jsonify({
            'message': 'OK',
            'data': treat_result(results)
        }),
        status.OK
    )


def treat_result(results):
    turns = list(map(lambda x: x.get('turns'), results))
    winners = list(map(lambda x: x.get('winner'), results))

    timeouts = len(list(filter(lambda x: x == 1000, turns)))
    average = sum(turns)/len(turns)

    impulsives = list(filter(lambda x: x.play_pattern == 'impulsive', winners))
    cautious = list(filter(lambda x: x.play_pattern == 'cautious', winners))
    rigorous = list(filter(lambda x: x.play_pattern == 'rigorous', winners))
    randoms = list(filter(lambda x: x.play_pattern == 'random', winners))

    percentages = {
        'impulsive': len(impulsives) / len(results),
        'cautious': len(cautious) / len(results),
        'rigorous': len(rigorous) / len(results),
        'random': len(randoms) / len(results)
    }

    most_victories = max(percentages.keys(), key=(lambda key: percentages[key]))

    return {
        'timeouts': timeouts,
        'average_turns': average,
        'percentages': percentages,
        'most_victories': most_victories
    }
