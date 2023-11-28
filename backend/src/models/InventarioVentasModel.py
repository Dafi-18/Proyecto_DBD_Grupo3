from database.dastabase import get_connection
from .entities.inventario_ventas import Inventario_Ventas, Articulos_vendidos
from .entities.product import Product


class InventarioVentasModel():

    @classmethod
    def get_articulos_vendidos(fecha):
        query="""
        SELECT art.nombre_articulo, sum(dv.cantidad) 
        FROM detalle_venta dv 
        inner join venta v 
        ON dv.id_venta = v.id_venta and v.fecha_venta = (%s AS DATE)
        inner join articulo art 
        on dv.id_articulo = art.id_articulo 
        group by art.id_articulo;
        """
        try:
            connection = get_connection()
            articulos_vendidos = []
            with connection.cursor() as cursor:
                cursor.execute(query, fecha)
                resultset = cursor.fetchall()
                
                for row in resultset:
                    articulos_vendidos.append(
                        #Articulos_vendidos(row[0], row[1]).to_JSON())
                        Product((row[0], row[1]).to_JSON()))
                    
            connection.close()
            return articulos_vendidos

        except Exception as ex:
            raise ex
        
    @classmethod
    def get_inventario_ventas(self):
        try:
            connection = get_connection()
            inventario_ventas = []

            with connection.cursor() as cursor:
                cursor.execute(
                    'SELECT id_articulo, nombre_articulo, precio_unitario, cantidad FROM articulo WHERE tipo_articulo="venta";')
                resultset = cursor.fetchall()

                for row in resultset:
                    inventario_ventas.append(
                        #Inventario_Ventas(row[0], row[1], row[2], row[3]).to_JSON())
                        Product(row[0], row[1], row[2], row[3]).to_JSON())

            connection.close()
            return inventario_ventas

        except Exception as ex:
            raise ex
        
    @classmethod
    def update_articulo(self, cantidad, precio_unitario, id_articulo):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute('UPDATE Articulo SET cantidad = %d , precio_unitario = %f WHERE Id_articulo = %s;',(cantidad, precio_unitario, id_articulo))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows

        except Exception as ex:
            raise ex
        
    @classmethod
    def add_articulo(self, articulo):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO Articulo (Id_articulo, Nombre_articulo, Tipo_articulo, Cantidad, Descripcion, Precio_unitario, Disponibilidad) VALUES (%s, %s, %s, %d, %s, %f, %s);", (
                    Product.id_articulo, Product.nombre_articulo, Product.tipo_articulo, Product.cantidad, Product.descripcion, Product.precio_unitario, Product.disponibilidad))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows

        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def delete_articulo(self, articulo):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute('DELETE FROM articulo WHERE id_articulo = %s;', (articulo.id_articulo)) 
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows

        except Exception as ex:
            raise Exception(ex)