from database.dastabase import get_connection
from .entities.inventario_ventas import Inventario_Ventas, Articulos_vendidos
from .entities.product import Product


class VentasModel():

    @classmethod
    def registrar_venta(cls, id_venta, id_usuario, monto_final):
        query="""
        INSERT INTO Venta (Id_venta, Id_usuario, Fecha_venta, Monto_final, Estado_pago) VALUES ();
        """
        try:
            connection = get_connection()
            articulos_vendidos = []
    
            with connection.cursor() as cursor:
                
                cursor.execute(query, (fecha, fecha))
                resultset = cursor.fetchall()
                
                for row in resultset:
                    articulos_vendidos.append(
                        Articulos_vendidos(row[0], row[1]).to_JSON())
                        
            connection.close()
            return articulos_vendidos

        except Exception as ex:
            raise ex
        
    @classmethod
    def registrar_producto(self, id_venta, id_articulo, medio_pago, cantidad, subtotal):
        query="""
        SELECT id_articulo, nombre_articulo, precio_unitario, cantidad FROM articulo WHERE tipo_articulo = 'venta';
        """
        try:
            connection = get_connection()
            inventario_ventas = []
            
            with connection.cursor() as cursor:
                cursor.execute(query)
                resultset = cursor.fetchall()

                for row in resultset:
                    inventario_ventas.append(
                        Inventario_Ventas(row[0], row[1], row[2], row[3]).to_JSON())

            connection.close()
            return inventario_ventas

        except Exception as ex:
            raise ex
        
        
    @classmethod
    def add_articulo(self, articulo):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO Articulo (id_articulo, nombre_articulo, tipo_articulo, cantidad, descripcion, precio_unitario, disponibilidad) VALUES (%s, %s, %s, %s, %s, %s, %s);", (
                    articulo.id_articulo, articulo.nombre_articulo, articulo.tipo_articulo, articulo.cantidad, articulo.descripcion, articulo.precio_unitario, articulo.disponibilidad))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows

        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def update_articulo(self, articulo):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute('UPDATE Articulo SET cantidad = %s , precio_unitario = %s WHERE Id_articulo = %s;',(articulo.cantidad, articulo.precio_unitario, articulo.id_articulo,))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows

        except Exception as ex:
            raise ex
    
    @classmethod
    def delete_articulo(self, articulo):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute('DELETE FROM articulo WHERE id_articulo = %s;', (articulo.id_articulo,)) 
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows

        except Exception as ex:
            raise Exception(ex)