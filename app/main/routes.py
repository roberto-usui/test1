from http import HTTPStatus as status
from flask import Blueprint, make_response, jsonify

main = Blueprint('main', __name__)


@main.route('/health-check')
def health_check():
    return make_response(
        jsonify({
            'message': 'OK'
        }),
        status.OK
    )
