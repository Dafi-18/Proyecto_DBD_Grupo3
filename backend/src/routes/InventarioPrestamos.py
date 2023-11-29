from flask import Blueprint, request, jsonify

from models.InventarioPrestamosModel import InventarioPrestamosModel
from models.ProductoModel import ProductoModel
from models.entities.product import Product

main = Blueprint('inventario_prestamos_blueprint', __name__)


@main.route('/articulos_prestados', methods=['GET'])
def get_articulos_prestados():
    try:
        fecha = request.json['fecha']
        articulos_prestados = InventarioPrestamosModel.get_articulos_prestados(fecha)
        return jsonify(articulos_prestados), 200

    except Exception as ex:
        return jsonify({'error': str(ex)}), 500


@main.route('/', methods=['GET'])
def get_inventario_prestamos():
    try:
        inventario_prestamos = InventarioPrestamosModel.get_inventario_prestamos()
        return jsonify(inventario_prestamos), 200

    except Exception as ex:
        return jsonify({'error': str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_articulo():
    try:
        id_articulo = request.json['id_articulo']
        nombre_articulo = request.json['nombre_articulo']
        cantidad = request.json['cantidad']
        descripcion = request.json['descripcion']
        
        articulo = Product(id_articulo, nombre_articulo, "prestamo", cantidad, descripcion, None, "disponible")

        affected_rows = InventarioPrestamosModel.add_articulo(articulo)
        print(affected_rows)

        if affected_rows == 1:
            return jsonify(articulo.to_JSON())
        else:
            return jsonify({'message': "Error en insert"}), 500

        return jsonify({})

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/update/<id_articulo>', methods=['PUT'])
def update_articulo(id_articulo):
    try:
        cantidad = request.json['cantidad']
        articulo = Product(id_articulo,"","",cantidad,"","","")
        
        affected_rows = InventarioPrestamosModel.update_articulo(articulo)
        
        if affected_rows == 1:
            return jsonify({'message': f"Se ha actualizado el artículo con el id {articulo.id_articulo}"})
        else:
            return jsonify({'message': "No item updated"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
    
@main.route('/delete/<id_articulo>', methods=['DELETE'])
def delete_articulo(id_articulo):
    try:
        articulo = Product(id_articulo,"","","","","","")
        affected_rows = InventarioPrestamosModel.delete_articulo(articulo)
        
        if affected_rows == 1:
            return jsonify({'message': f"Se eliminó el artículo con el id {id_articulo}"})
        else:
            return jsonify({'message': "No item deleted"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500