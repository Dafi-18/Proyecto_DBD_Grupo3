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


@main.route('/fecha/<fe>', methods=['GET'])
def get_Encuesta_fecha(fe):
    try:
        # Lógica para obtener la encuesta por fecha
        encuesta = EncuestasModel.get_Encuesta_fecha(fe)
        if encuesta != None:
            return jsonify(encuesta), 200
        else:
            return jsonify({}), 404

    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

@main.route('/id/<id>', methods=['GET'])
def get_Encuesta_ID(id):
    try:
        # Lógica para obtener la encuesta por ID
        encuesta = EncuestasModel.get_Encuesta_ID(id)
        if encuesta != None:
            return jsonify(encuesta), 200
        else:
            return jsonify({}), 404

    except Exception as ex:
        return jsonify({'error': str(ex)}), 500