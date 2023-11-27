from flask import Flask

from config import config

# Routes
from routes import Product
from routes import Estadisticas
from routes import security
from routes import Encuesta

app = Flask(__name__)


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

    # Error handlers
    app.register_error_handler(404, page_not_found)

    app.run()
