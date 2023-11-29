from database.dastabase import get_connection
from .entities.reservas import Calendario

class ReservasModel():

    @classmethod
    def generate_calendario(cls,fecha):
        query="""
        CREATE OR REPLACE PROCEDURE Generar_Calendario()
        LANGUAGE PLPGSQL
        AS
        $$
        begin
            for fecha in 0..6 loop
                for id in 1..14 loop
                    insert into Calendario(Id_hora, Fecha, Hora_inicio, Hora_fin , Estado) values
                    (id, (%s AS DATE)+fecha, ('08:00:00'::time + (id - 1) * interval '1 hour')::time, ('08:00:00'::time + (id) * interval '1 hour')::time,'Disponible');
                end loop;
            end loop;
        END;
        $$

        DO
        $$
        BEGIN
            call Generar_Calendario();
        END;
        $$
        """
        try:
            connection = get_connection()
    
            with connection.cursor() as cursor:
                
                cursor.execute(query, (fecha,))
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
        AND EXTRACT(MONTH FROM fecha) = EXTRACT(MONTH FROM current_date)
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
                        Calendario(row[0], row[1], row[2], row[3], row[4]).to_JSON())

            connection.close()
            return calendario_semana

        except Exception as ex:
            raise ex
        
    
    @classmethod
    def update_disponibilidad(self, calendario):
        query="""
        update calendario set estado = 
        case 
            when estado = 'Ocupado' then 'Disponible' 
            when estado = 'Disponible' then 'Ocupado' 
        end 
        where id_hora = %s and Fecha = %s;
        """
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(query,(calendario.id_hora, calendario.fecha,))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows

        except Exception as ex:
            raise ex
    