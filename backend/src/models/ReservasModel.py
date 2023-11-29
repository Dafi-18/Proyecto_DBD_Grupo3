from database.dastabase import get_connection
from .entities.reservas import Calendario

class ReservasModel():

    @classmethod
    def generate_calendario(cls,fecha):
        try:
            connection = get_connection()
    
            with connection.cursor() as cursor:
                
                cursor.execute('CALL generate_calendario(%s)', (fecha,))
                affected_rows = cursor.rowcount
                connection.commit()
                
            connection.close()
            return affected_rows
        
        except Exception as ex:
            raise ex
        
    @classmethod
    def get_calendario(self):
        query="""
        SELECT * FROM calendario 
        WHERE EXTRACT(WEEK FROM fecha) = EXTRACT(WEEK FROM current_date)
        AND EXTRACT(YEAR FROM fecha) = EXTRACT(YEAR FROM current_date)
        order by fecha, id_hora;
        """
        try:
            connection = get_connection()
            calendario_semana = []
            
            with connection.cursor() as cursor:
                cursor.execute(query)
                resultset = cursor.fetchall()

                for row in resultset:
                    calendario_semana.append(
                        Calendario(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4])).to_JSON())

            connection.close()
            return calendario_semana

        except Exception as ex:
            raise ex
        
    
    @classmethod
    def update_disponibilidad(self, fecha, id_hora):
        query="""
        update calendario set estado = case when estado = 'Ocupado' then 'Disponible' when estado = 'Disponible' then 'Ocupado' end where Fecha = %s and id_hora = %s;
        """
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(query, (fecha, id_hora))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows

        except Exception as ex:
            raise ex
    