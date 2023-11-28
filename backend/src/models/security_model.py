from database.dastabase import get_connection
from .entities.seguridad import usuario, persona


class SeguridadModel():

    @classmethod
    def get_usuario(self):
        try:
            connection = get_connection()
            usuarios = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT Id_usuario,Dni,Cod_uni,Correo_uni,Contrasena from Usuario")
                resultset = cursor.fetchall()

                for row in resultset:
                    user = usuario(row[0], row[1], row[2], row[3], row[4])
                    usuarios.append(user.to_JSON())
            connection.close()
            return usuarios

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_user(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT Id_usuario,Dni,Cod_uni,Correo_uni,Contrasena from Usuario WHERE Id_usuario=%s", (id,))
                row = cursor.fetchone()

                user = None
                if row != None:
                    user = usuario(row[0], row[1], row[2], row[3], row[4])
                    user = user.to_JSON()
            connection.close()
            return user

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_person(self, persona, usuario):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("BEGIN;")
                cursor.execute("INSERT INTO persona (Dni, Primer_nombre, Segundo_nombre, Primer_apellido,Segundo_apellido,Celular) VALUES (%s, %s, %s, %s, %s, %s) RETURNING dni;", (
                    persona.dni, persona.primer_nombre, persona. segundo_nombre, persona.primer_apellido, persona.segundo_apellido, persona.celular))

                if cursor.rowcount > 0:
                    dni_persona = cursor.fetchone()[0]
                    cursor.execute("INSERT INTO usuario (Dni, Cod_uni, Correo_uni, Contrasena) VALUES (%s, %s, %s, %s);", (
                        dni_persona, usuario.codigouni, usuario.correouni, usuario.contrasena))
                    cursor.execute("COMMIT;")

            affected_rows = cursor.rowcount
            connection.commit()
            connection.close()
            return affected_rows

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def login(self, usuario):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT Id_usuario,Dni,Cod_uni,Correo_uni,Contrasena from Usuario WHERE Correo_uni =%s", (usuario.correouni,))
                row = cursor.fetchone()

                if row:
                    if usuario.check_password(row[4], usuario.contrasena):
                        user = usuario(row[0], row[1], row[2], row[3], row[4])
                        connection.close()
                        return user.to_JSON()
                    else:
                        return None

                else:
                    return None

        except Exception as ex:
            raise Exception(ex)
