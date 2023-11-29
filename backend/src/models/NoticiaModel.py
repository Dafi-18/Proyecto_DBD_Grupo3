from database.dastabase import get_connection
from .entities.Noticia import Noticia 

class NoticiaModel():

    @classmethod
    def get_Noticia(self):
        try:
            connection = get_connection()
            noticia = []

            with connection.cursor() as cursor:
                cursor.execute(
                    'SELECT Id_noticia, Id_administrador, Fecha, Titulo, Descripcion FROM Noticia')
                resultset = cursor.fetchall()

                for row in resultset:
                    noticia.append(
                        Noticia(row[0], row[1], row[2], row[3], row[4]).to_JSON())

            connection.close()
            return noticia

        except Exception as ex:
            raise Exception(ex)
        

        
    @classmethod
    def add_Noticia(self, noticia):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """INSERT INTO Noticia(Id_noticia, Id_administrador, Fecha, Titulo, Descripcion) 
                    VALUES (%s, %s, %s, %s, %s)""", (noticia.Id_noticia, noticia.Id_administrador, noticia.Fecha, noticia.Titulo, noticia.Descripcion))
                affected_rows=cursor.rowcount
                connection.commit()
                

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        

        
    @classmethod
    def update_Noticia(self, noticia):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """UPDATE Noticia SET Fecha = %s, Titulo = %s, Descripcion = %s) 
                    WHERE Id_noticia = %s""", (noticia.Fecha, noticia.Titulo, noticia.Descripcion, noticia.Id_noticia))
                affected_rows=cursor.rowcount
                connection.commit()
                

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
        

    @classmethod
    def adelete_Noticia(self, noticia):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM Noticia WHERE Id_noticia = $s", (noticia.Id_noticia,))
                affected_rows=cursor.rowcount
                connection.commit()
                

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
