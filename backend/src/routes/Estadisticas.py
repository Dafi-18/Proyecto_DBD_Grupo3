from flask import Blueprint, request, jsonify

from models.EstadisticasModel import EstadisticasModel

main = Blueprint('estadisticas_blueprint', __name__)


@main.route('/total_transacciones_mes', methods=['GET'])
def get_total_transacciones_mes():
    try:
        fecha = request.args.get('fecha')
        estadisticas = EstadisticasModel.get_total_transacciones_mes(fecha)
        return jsonify(estadisticas), 200

    except Exception as ex:
        return jsonify({'error': str(ex)}), 500


@main.route('/total_alquileres_mes', methods=['GET'])
def get_total_alquileres_mes():
    try:
        fecha = request.args.get('fecha')
        total_alquileres = EstadisticasModel.get_total_alquileres_mes(fecha)
        return jsonify(total_alquileres), 200

    except Exception as ex:
        return jsonify({'error': str(ex)}), 500


@main.route('/total_ventas_mes', methods=['GET'])
def total_ventas_mes():
    try:
        fecha = request.args.get('fecha')
        total = EstadisticasModel.get_total_ventas_mes(fecha)
        return jsonify({'total_ventas_mes': total}), 200
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500


@main.route('/total_prestamos_mes', methods=['GET'])
def total_prestamos_mes():
    try:
        fecha = request.args.get('fecha')
        total = EstadisticasModel.get_total_prestamos_mes(fecha)
        return jsonify({'total_prestamos_mes': total}), 200
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500


@main.route('/total_recaudado_alquiler_mes', methods=['GET'])
def total_recaudado_alquiler_mes():
    try:
        fecha = request.args.get('fecha')
        total = EstadisticasModel.get_total_recaudado_alquiler_mes(fecha)
        return jsonify({'total_recaudado_alquiler_mes': total}), 200
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500


@main.route('/total_recaudado_venta_mes', methods=['GET'])
def total_recaudado_ventas_mes():
    try:
        fecha = request.args.get('fecha')
        total = EstadisticasModel.get_total_recaudado_ventas_mes(fecha)
        return jsonify({'total_recaudado_venta_mes': total}), 200
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500
