from database.dastabase import get_connection
from .entities.Encuestas import Encuesta

class EncuestasModel():

    @classmethod
    def get_Encuesta(self):
        try:
            connection = get_connection()
            Encuestas = []

            with connection.cursor() as cursor:
                cursor.execute(
                    'SELECT Id_encuesta, Id_administrador, Fecha_apertura, Fecha_cierre, Cantidad_preguntas, Cantidad_respuestas, Estado_encuesta FROM Encuesta')
                resultset = cursor.fetchall()

                for row in resultset:
                    Encuestas.append(
                        Encuesta(row[0], row[1], row[2], row[3], row[4], row[5], row[6]).to_JSON())

            connection.close()
            return Encuestas

        except Exception as ex:
            raise ex