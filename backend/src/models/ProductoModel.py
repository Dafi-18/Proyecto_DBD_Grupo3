from database.dastabase import get_connection
from .entities.product import Product


class ProductoModel():

    @classmethod
    def get_Product(self):
        try:
            connection = get_connection()
            productos = []

            with connection.cursor() as cursor:
                cursor.execute(
                    'SELECT id_articulo, nombre_articulo, tipo_articulo, cantidad, descripcion, precio_unitario, disponibilidad FROM articulo')
                resultset = cursor.fetchall()

                for row in resultset:
                    productos.append(
                        Product(row[0], row[1], row[2], row[3], row[4], row[5], row[6]).to_JSON())

            connection.close()
            return productos

        except Exception as ex:
            raise ex
