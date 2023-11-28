from database.dastabase import get_connection
from .entities.InventarioVentas import Inventario_Ventas


class InventarioVentasModel():

    @classmethod
    def get_InventarioVentas(self):
        try:
            connection = get_connection()
            inventario_ventas = []

            with connection.cursor() as cursor:
                cursor.execute(
                    'SELECT id_articulo, nombre_articulo, precio_unitario, cantidad FROM articulo WHERE tipo_articulo="venta"')
                resultset = cursor.fetchall()

                for row in resultset:
                    inventario_ventas.append(
                        Inventario_Ventas(row[0], row[1], row[2], row[3]).to_JSON())

            connection.close()
            return inventario_ventas

        except Exception as ex:
            raise ex