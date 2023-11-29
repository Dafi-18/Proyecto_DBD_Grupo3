from database.dastabase import get_connection
from .entities.inventario_ventas import Inventario_Ventas, Articulos_vendidos
from .entities.product import Product


class InventarioVentasModel():

    @classmethod
    def get_articulos_vendidos(cls,fecha):
        query="""
        SELECT art.nombre_articulo, sum(dv.cantidad) FROM detalle_venta dv 
        inner join venta v ON dv.id_venta = v.id_venta and EXTRACT(MONTH FROM v.Fecha_venta) = EXTRACT(MONTH FROM CAST(%s AS DATE)) 
        AND EXTRACT(YEAR FROM v.Fecha_venta) = EXTRACT(YEAR FROM CAST(%s AS DATE))
        inner join articulo art on dv.id_articulo = art.id_articulo 
        group by art.id_articulo;
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
    def get_inventario_ventas(self):
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