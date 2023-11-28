from flask import Blueprint, request, jsonify

from models.FinanzasModel import FinanzasModel

main = Blueprint('finanzas_blueprint', __name__)


@main.route('/total_transacciones_mes', methods=['GET'])
def get_total_transacciones_mes():
    try:
        fecha = request.args.get('fecha')
        estadisticas = FinanzasModel.get_total_transacciones_mes(fecha)
        return jsonify(estadisticas), 200

    except Exception as ex:
        return jsonify({'error': str(ex)}), 500


@main.route('/total_recaudado_alquier_mes', methods=['GET'])
def get_total_recaudado_alquier_mes():
    try:
        fecha = request.args.get('fecha')
        estadisticas = FinanzasModel.get_total_recaudado_alquier_mes(fecha)
        return jsonify(estadisticas), 200

    except Exception as ex:
        return jsonify({'error': str(ex)}), 500


@main.route('/total_recaudado_ventas_mes', methods=['GET'])
def get_total_recaudado_ventas_mes():
    try:
        fecha = request.args.get('fecha')
        estadisticas = FinanzasModel.get_total_recaudado_ventas_mes(fecha)
        return jsonify(estadisticas), 200

    except Exception as ex:
        return jsonify({'error': str(ex)}), 500


@main.route('/total_recaudado_mes', methods=['GET'])
def get_total_recaudado_mes():
    try:
        fecha = request.args.get('fecha')
        estadisticas = FinanzasModel.get_total_recaudado_mes(fecha)
        return jsonify(estadisticas), 200

    except Exception as ex:
        return jsonify({'error': str(ex)}), 500


@main.route('/historial_transacciones', methods=['GET'])
def get_historial():
    try:
        estadisticas = FinanzasModel.get_historial()
        return jsonify(estadisticas), 200

    except Exception as ex:
        return jsonify({'error': str(ex)}), 500
