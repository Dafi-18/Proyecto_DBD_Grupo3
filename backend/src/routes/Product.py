from flask import Blueprint, request, jsonify

# Models
from models.ProductoModel import ProductoModel

main = Blueprint('product_blueprint', __name__)


@main.route('/', methods=['GET'])
def get_products():
    try:
        productos = ProductoModel.get_Product()
        return jsonify(productos), 200

    except Exception as ex:
        return jsonify({'error': str(ex)}), 500
