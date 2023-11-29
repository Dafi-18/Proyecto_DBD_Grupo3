from database.dastabase import get_connection
from .entities.inventario_prestamos import Inventario_Prestamos, Articulos_prestados
from .entities.product import Product

class InventarioPrestamosModel():

    @classmethod
    def get_articulos_prestados(cls, fecha):
        query="""
        SELECT art.nombre_articulo, count(p.id_articulo)  FROM articulo art 
		inner join prestamo p ON art.id_articulo = p.id_articulo 
		and p.fecha_prestamo = %s
        and p.estado_prestamo = 'No devuelto'
        group by art.nombre_articulo;
        """
        try:
            connection = get_connection()
            articulos_prestados = []
    
            with connection.cursor() as cursor:
                
                cursor.execute(query, (fecha,))
                resultset = cursor.fetchall()
                
                for row in resultset:
                    articulos_prestados.append(
                        Articulos_prestados(row[0], row[1]).to_JSON())
                        
            connection.close()
            return articulos_prestados

        except Exception as ex:
            raise ex
        
    @classmethod
    def get_inventario_prestamos(self):
        query="""
        SELECT id_articulo, nombre_articulo, cantidad FROM articulo WHERE tipo_articulo = 'prestamo';
        """
        try:
            connection = get_connection()
            inventario_prestamos = []
            
            with connection.cursor() as cursor:
                cursor.execute(query)
                resultset = cursor.fetchall()

                for row in resultset:
                    inventario_prestamos.append(
                        Inventario_Prestamos(row[0], row[1], row[2]).to_JSON())

            connection.close()
            return inventario_prestamos

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
                cursor.execute('UPDATE Articulo SET cantidad = %s WHERE Id_articulo = %s;',(articulo.cantidad, articulo.id_articulo,))
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