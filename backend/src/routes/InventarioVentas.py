from flask import Blueprint, request, jsonify

from models.InventarioVentasModel import InventarioVentasModel
from models.ProductoModel import ProductoModel

main = Blueprint('inventario_ventas_blueprint', __name__)


@main.route('/articulos_vendidos', methods=['GET'])
def get_articulos_vendidos():
    try:
        fecha = request.json['fecha']
        articulos_vendidos = InventarioVentasModel.get_articulos_vendidos(fecha)
        return jsonify(articulos_vendidos), 200

    except Exception as ex:
        return jsonify({'error': str(ex)}), 500


@main.route('/get_inventario_ventas', methods=['GET'])
def get_inventario_ventas():
    try:
        fecha = request.json['fecha']
        inventario_ventas = InventarioVentasModel.get_inventario_ventas(fecha)
        return jsonify(inventario_ventas), 200

    except Exception as ex:
        return jsonify({'error': str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_articulo():
    try:
        id_articulo = request.json['id_articulo']
        nombre_articulo = request.json['nombre_articulo']
        cantidad = request.json['cantidad']
        precio_unitario = request.json['precio_unitario']
        descripcion = request.json['descripcion']
        
        articulo = Product(id_articulo, nombre_articulo, "venta", cantidad, descripcion, precio_unitario, "disponible")

        affected_rows = InventarioVentasModel.add_articulo(articulo)
        print(affected_rows)

        if affected_rows == 1:
            return jsonify(articulo.id_articulo)
        else:
            return jsonify({'message': "Error en insert"}), 500

        return jsonify({})

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/update/<id>', methods=['PUT'])
def update_articulo(cantidad, precio_unitario, id_articulo):
    try:
        cantidad = request.json['cantidad']
        precio_unitario = request.json['precio_unitario']
        id_articulo = Product(id_articulo)
        
        affected_rows = InventarioVentasModel.update_articulo(cantidad, precio_unitario, id_articulo)
        
        if affected_rows == 1:
            return jsonify(id_articulo)
        else:
            return jsonify({'message': "No item updated"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
    
@main.route('/delete/<id_articulo>', methods=['DELETE'])
def delete_articulo(id_articulo):
    try:
        articulo = Product(id_articulo)
        
        affected_rows = InventarioVentasModel.delete_articulo(articulo)
        
        if affected_rows == 1:
            return jsonify(articulo.id_articulo)
        else:
            return jsonify({'message': "No item deleted"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500