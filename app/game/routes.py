from http import HTTPStatus as status
from flask import Blueprint, make_response, jsonify
from app import db

from app.models import Table, Player
from .services.game_service import GameService

game = Blueprint('game', __name__)


@game.route('/basic-game/simulate', methods=['GET'])
def simulate():
    table = db.session.query(Table).all()[0]
    properties = table.properties.all()
    players = db.session.query(Player).all()

    service = GameService(properties, players)
    service.run()
    return make_response(
        jsonify({
            'message': 'OK'
        }),
        status.OK
    )
