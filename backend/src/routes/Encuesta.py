from flask import Blueprint, request, jsonify

# Models
from models.EncuestasModel import EncuestasModel

main = Blueprint('encuesta_blueprint', __name__)


@main.route('/', methods=['GET'])
def get_Encuesta():
    try:
        encuestas = EncuestasModel.get_Encuesta()
        return jsonify(encuestas), 200

    except Exception as ex:
        return jsonify({'error': str(ex)}), 500