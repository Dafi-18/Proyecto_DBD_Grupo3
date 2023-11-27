from flask import Blueprint, request, jsonify

from models.EstadisticasModel import EstadisticasModel

main = Blueprint('estadisticas_blueprint', __name__)


@main.route('/total_transacciones_mes', methods=['GET'])
def get_total_transacciones_mes():
    try:
        estadisticas = EstadisticasModel.get_total_transacciones_mes()
        return jsonify(estadisticas), 200

    except Exception as ex:
        return jsonify({'error': str(ex)}), 500
