from flask import Blueprint, request, jsonify
import uuid

# Entities
from models.entities.Noticia import Noticia

#Models
from models.NoticiaModel import NoticiaModel

main = Blueprint('noticia_blueprint', __name__)


@main.route('/', methods=['GET'])
def get_Noticia():
    try:
        noticia = NoticiaModel.get_Noticia()
        return jsonify(noticia), 200

    except Exception as ex:
        return jsonify({'error': str(ex)}), 500
    
    
    
@main.route('/add', methods=['POST'])
def add_Noticia():
    try:
        Id_noticia = request.json['Id_noticia']
        Id_administrador = request.json['Id_administrador']
        Fecha = request.json['Fecha']
        Titulo = request.json['Titulo']
        Descripcion = request.json['Descripcion']

        noticia=Noticia(Id_noticia, Id_administrador, Fecha, Titulo, Descripcion)

        affected_rows=NoticiaModel.add_Noticia(noticia)

        if affected_rows == 1:
            return jsonify(noticia.Id_noticia)
        else:
            return jsonify({'message': 'Error en la insercion'}), 500
    
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    

    
@main.route('/update/<Id_noticia>', methods=['PUT'])
def update_Noticia():
    try:
        Id_noticia = request.json['Id_noticia']
        Id_administrador = request.json['Id_administrador']
        Fecha = request.json['Fecha']
        Titulo = request.json['Titulo']
        Descripcion = request.json['Descripcion']

        noticia=Noticia(Id_noticia, Id_administrador, Fecha, Titulo, Descripcion)

        affected_rows=NoticiaModel.update_Noticia(noticia)

        if affected_rows == 1:
            return jsonify(noticia.Id_noticia)
        else:
            return jsonify({'message': 'Ningunna pelicula actualizada'}), 404
    
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    


@main.route('/delete/<Id_noticia>', methods=['DELETE'])
def delete_Noticia(Id_noticia):
    try:
        noticia=Noticia(Id_noticia)

        affected_rows=NoticiaModel.delete_Noticia(noticia)

        if affected_rows == 1:
            return jsonify(noticia.Id_noticia)
        else:
            return jsonify({'message': 'Ninguna noticia borrada'}), 404
    
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
    