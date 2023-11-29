from flask import Blueprint, request, jsonify

# Models
from models.EncuestasModel import EncuestasModel
from models.entities.Encuestas import Encuesta, Pregunta

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

@main.route('/contador', methods=['GET'])
def get_Encuesta_COUNT():
    try:
        # Lógica para obtener la encuesta por ID
        encuesta = EncuestasModel.get_Encuesta_COUNT()
        if encuesta != None:
            return jsonify(encuesta), 200
        else:
            return jsonify({}), 404

    except Exception as ex:
        return jsonify({'error': str(ex)}), 500
    
@main.route('/add', methods=['POST'])
def add_encuesta():
    try:
        
        Id_encuesta = request.json['Id_encuesta']
        Id_administrador = request.json['Id_administrador']
        Fecha_apertura = (request.json['Fecha_apertura'])
        Fecha_cierre = request.json['Fecha_cierre']
        Cantidad_preguntas = int(request.json['Cantidad_preguntas'])
        Cantidad_respuestas = int(request.json['Cantidad_respuestas'])
        Estado_encuesta = request.json['Estado_encuesta']
        encuesta = Encuesta(Id_encuesta, Id_administrador, Fecha_apertura, Fecha_cierre, Cantidad_preguntas, Cantidad_respuestas, Estado_encuesta)

        affected_rows = EncuestasModel.add_encuesta(encuesta)
        
        if affected_rows == 1:
            return jsonify(encuesta.Id_encuesta)
        else:
            return jsonify({'message': "Error on insert"}), 500


    except Exception as ex:
        return jsonify({'masage': str(ex)}), 500
    
@main.route('/update/<id>', methods=['PUT'])
def update_encuesta(id):
    try:
        Id_encuesta = request.json['Id_encuesta']
        Id_administrador = request.json['Id_administrador']
        Fecha_apertura = (request.json['Fecha_apertura'])
        Fecha_cierre = request.json['Fecha_cierre']
        Cantidad_preguntas = int(request.json['Cantidad_preguntas'])
        Cantidad_respuestas = int(request.json['Cantidad_respuestas'])
        Estado_encuesta = request.json['Estado_encuesta']
        encuesta = Encuesta(Id_encuesta, Id_administrador, Fecha_apertura, Fecha_cierre, Cantidad_preguntas, Cantidad_respuestas, Estado_encuesta)

        affected_rows = EncuestasModel.update_encuesta(encuesta)
        
        if affected_rows == 1:
            return jsonify(encuesta.Id_encuesta)
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


    #######################################################################preguntas##############################################################
    
@main.route('/preguntas', methods=['GET'])
def get_Pregunta():
    try:
        preguntas = EncuestasModel.get_Pregunta()
        return jsonify(preguntas), 200

    except Exception as ex:
        return jsonify({'error': str(ex)}), 500
    
@main.route('/preguntas/add', methods=['POST'])
def add_pregunta():
    try:
        Id_pregunta=(request.json['Id_pregunta'])
        Id_encuesta = request.json['Id_encuesta']
        Id_administrador = request.json['Id_administrador']
        tipo_respuesta = (request.json['tipo_respuesta'])
       
        pre = Pregunta(Id_pregunta,Id_encuesta, Id_administrador, tipo_respuesta)

        affected_rows = EncuestasModel.add_pregunta(pre)
        
        if affected_rows == 1:
            return jsonify(pre.Id_pregunta)
        else:
            return jsonify({'message': "Error on insert"}), 500


    except Exception as ex:
        return jsonify({'masage': str(ex)}), 500
    

@main.route('/preguntas/update/<id>', methods=['PUT'])
def update_pregunta(id):
    try:
        Id_pregunta=(request.json['Id_pregunta'])
        Id_encuesta = request.json['Id_encuesta']
        Id_administrador = request.json['Id_administrador']
        tipo_respuesta = (request.json['tipo_respuesta'])
       
        pre = Pregunta(Id_pregunta,Id_encuesta, Id_administrador, tipo_respuesta)

        affected_rows = EncuestasModel.update_pregunta(pre)
        
        if affected_rows == 1:
            return jsonify(pre.Id_encuesta)
        else:
            return jsonify({'message': "Error on insert"}), 500


    except Exception as ex:
        return jsonify({'masage': str(ex)}), 500
    