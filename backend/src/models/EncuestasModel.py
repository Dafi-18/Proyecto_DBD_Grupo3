from database.dastabase import get_connection
from .entities.Encuestas import Encuesta, Pregunta

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
        
    @classmethod
    def get_Encuesta_ID(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    'SELECT Id_encuesta, Id_administrador, Fecha_apertura, Fecha_cierre, Cantidad_preguntas, Cantidad_respuestas, Estado_encuesta FROM Encuesta WHERE Id_encuesta=%s',(id,))
                row = cursor.fetchone()
                encuesta=None
                if row !=None:
                    encuesta=Encuesta(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    encuesta=encuesta.to_JSON()
            connection.close()
            return encuesta
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_Encuesta_fecha(self, fe):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    'SELECT Id_encuesta, Id_administrador, Fecha_apertura, Fecha_cierre, Cantidad_preguntas, Cantidad_respuestas, Estado_encuesta FROM Encuesta E WHERE E.Fecha_apertura=%s',(fe,))
                row = cursor.fetchone()
                encuesta=None
                if row !=None:
                    encuesta=Encuesta(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    encuesta=encuesta.to_JSON()
            connection.close()
            return encuesta
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_Encuesta_COUNT(self):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    'SELECT COUNT(E.Id_encuesta) FROM Encuesta E')
                row = cursor.fetchone()
                #encuesta=None
                #if row !=None:
                    #encuesta=row[0]
                    #encuesta=encuesta.to_JSON()
            connection.close()
            return row[0]
        except Exception as ex:
            raise Exception(ex)
##################################################################################################### PREGUNTAS##############################################
    @classmethod
    def get_Pregunta(self):
        try:
            connection = get_connection()
            Preguntas = []

            with connection.cursor() as cursor:
                cursor.execute(
                    'SELECT Id_pregunta, Id_encuesta, Id_administrador, tipo_respuesta FROM pregunta')
                resultset = cursor.fetchall()

                for row in resultset:
                    Preguntas.append(
                        Pregunta(row[0], row[1], row[2], row[3]).to_JSON())

            connection.close()
            return Preguntas

        except Exception as ex:
            raise ex