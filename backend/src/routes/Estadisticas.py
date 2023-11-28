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
        total = EstadisticasModel.get_total_recaudado_alquier_mes(fecha)
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


@main.route('/articulo_mas_alquilado_mes', methods=['GET'])
def articulo_mas_alquilado_mes():
    try:
        fecha = request.args.get('fecha')
        articulo = EstadisticasModel.get_articulo_mas_alquilado_mes(fecha)
        return jsonify({'articulo_mas_alquilado_mes': articulo}), 200
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500


@main.route('/articulo_cantidad_mas_aquilado_mes', methods=['GET'])
def articulo_cantidad_mas_aquilado_mes():
    try:
        fecha = request.args.get('fecha')
        articulo = EstadisticasModel.get_cantidad_articulo_mas_alquilado_mes(
            fecha)
        return jsonify({'articulo_cantidad_mas_aquilado_mes': articulo}), 200
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500


@main.route('/articulo_menos_alquilado_mes', methods=['GET'])
def articulo_menos_alquilado_mes():
    try:
        fecha = request.args.get('fecha')
        articulo = EstadisticasModel.get_articulo_menos_alquilado_mes(fecha)
        return jsonify({'articulo_menos_alquilado_mes': articulo}), 200
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500


@main.route('/articulo_cantidad_menos_aquilado_mes', methods=['GET'])
def articulo_cantidad_menos_aquilado_mes():
    try:
        fecha = request.args.get('fecha')
        articulo = EstadisticasModel.get_cantidad_articulo_menos_alquilado_mes(
            fecha)
        return jsonify({'articulo_cantidad_menos_aquilado_mes': articulo}), 200
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500


@main.route('/articulo_mas_prestado_mes', methods=['GET'])
def articulo_mas_prestado_mes():
    try:
        fecha = request.args.get('fecha')
        articulo = EstadisticasModel.get_articulo_mas_prestado_mes(fecha)
        return jsonify({'articulo_mas_prestado_mes': articulo}), 200
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500


@main.route('/articulo_cantidad_mas_prestado_mes', methods=['GET'])
def articulo_cantidad_mas_prestado_mes():
    try:
        fecha = request.args.get('fecha')
        articulo = EstadisticasModel.get_cantidad_articulo_mas_prestado_mes(
            fecha)
        return jsonify({'articulo_cantidad_mas_prestado_mes': articulo}), 200
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500


@main.route('/articulo_menos_prestado_mes', methods=['GET'])
def articulo_menos_prestado_mes():
    try:
        fecha = request.args.get('fecha')
        articulo = EstadisticasModel.get_articulo_menos_prestado_mes(fecha)
        return jsonify({'articulo_menos_prestado_mes': articulo}), 200
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500


@main.route('/articulo_cantidad_menos_prestado_mes', methods=['GET'])
def articulo_cantidad_menos_prestado_mes():
    try:
        fecha = request.args.get('fecha')
        articulo = EstadisticasModel.get_cantidad_articulo_menos_prestado_mes(
            fecha)
        return jsonify({'articulo_cantidad_menos_prestado_mes': articulo}), 200
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500


@main.route('/articulo_mas_vendido_mes', methods=['GET'])
def articulo_mas_vendido_mes():
    try:
        fecha = request.args.get('fecha')
        articulo = EstadisticasModel.get_articulo_mas_vendido_mes(fecha)
        return jsonify({'articulo_mas_vendido_mes': articulo}), 200
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500


@main.route('/articulo_cantidad_mas_vendido_mes', methods=['GET'])
def articulo_cantidad_mas_vendido_mes():
    try:
        fecha = request.args.get('fecha')
        articulo = EstadisticasModel.get_cantidad_articulo_mas_vendido_mes(
            fecha)
        return jsonify({'articulo_cantidad_mas_vendido_mes': articulo}), 200
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500


@main.route('/articulo_menos_vendido_mes', methods=['GET'])
def articulo_menos_vendido_mes():
    try:
        fecha = request.args.get('fecha')
        articulo = EstadisticasModel.get_articulo_menos_vendido_mes(fecha)
        return jsonify({'articulo_menos_vendido_mes': articulo}), 200
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500


@main.route('/articulo_cantidad_menos_vendido_mes', methods=['GET'])
def articulo_cantidad_menos_vendido_mes():
    try:
        fecha = request.args.get('fecha')
        articulo = EstadisticasModel.get_cantidad_articulo_menos_vendido_mes(
            fecha)
        return jsonify({'articulo_cantidad_menos_vendido_mes': articulo}), 200
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500
