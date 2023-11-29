from flask import Blueprint, request, jsonify
from models.ReservasModel import ReservasModel
from models.entities.reservas import Calendario

main = Blueprint('reservas_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_calendario():
    try:
        calendario_semana = ReservasModel.get_calendario()
        return jsonify(calendario_semana), 200

    except Exception as ex:
        return jsonify({'error': str(ex)}), 500


@main.route('/generate_calendario', methods=['POST'])
def generate_calendario():
    try:
        fecha = request.json['fecha']
        affected_rows = InventarioPrestamosModel.add_articulo(fecha)
        print(affected_rows)

        if affected_rows == 1:
            return jsonify({'message': "Se ha generado los horarios de la semana"})
        else:
            return jsonify({'message': "Error en la generación de los horarios de la semana"}), 500

        return jsonify({})

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/update/<fecha>/<id_hora>', methods=['PUT'])
def update_disponibilidad(fecha, id_hora):
    try:
        fecha = request.json['fecha']
        calendario = Calendario(id_hora, fecha, "", "", "")
        
        affected_rows = ReservasModel.update_disponibilidad(calendario)
        
        if affected_rows == 1:
            return jsonify({'message': f"Se ha cambiado la disponibilidad del calendario del dia {calendario.fecha} con el id_hora {calendario.id_hora}"})
        else:
            return jsonify({'message': "No se pudo cambiar la disponibilidad"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
