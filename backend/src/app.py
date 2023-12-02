from flask import Flask
from flask_cors import CORS

from config import config

# Routes
from routes import Product
from routes import Estadisticas, Finanzas
from routes import security
from routes import Encuesta
from routes import InventarioPrestamos, InventarioVentas
from routes import Reservas
from routes import Noticia
from routes import Transacciones

app = Flask(__name__)
CORS(app)


def page_not_found(error):
    return 'This page does not exist', 404


if __name__ == '__main__':
    app.config.from_object(config['development'])

    # BluePrints
    app.register_blueprint(Product.main, url_prefix='/api/products')

    # Blueprints Estadisticas
    app.register_blueprint(Estadisticas.main, url_prefix='/api/estadisticas')

    # Blueprints Security
    app.register_blueprint(security.main, url_prefix='/api/security')
    # Blueprints Encuesta
    app.register_blueprint(Encuesta.main, url_prefix='/api/encuesta')

    # BluePrints Finanzas
    app.register_blueprint(Finanzas.main, url_prefix='/api/finanzas')
    
    #BluePrints Ventas
    app.register_blueprint(Finanzas.main, url_prefix='/api/ventas')
    
    #BluePrints Prestamos
    app.register_blueprint(Finanzas.main, url_prefix='/api/prestamos')
    
    #BluePrints Alquileres
    app.register_blueprint(Finanzas.main, url_prefix='/api/alquileres')

    # BluePrints Inventario ventas
    app.register_blueprint(InventarioVentas.main, url_prefix='/api/inventario/ventas')

    # BluePrints Inventario préstamos
    app.register_blueprint(InventarioPrestamos.main, url_prefix='/api/inventario/prestamos')

    # BluePrints Reservas
    app.register_blueprint(Reservas.main, url_prefix='/api/reservas')

    # BluePrints Noticias
    app.register_blueprint(Noticia.main, url_prefix='/api/noticia')

    # Error handlers
    app.register_error_handler(404, page_not_found)

    app.run()
