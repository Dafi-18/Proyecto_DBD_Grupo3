from database.dastabase import get_connection
from .entities.seguridad import usuario, persona, venta
import json


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
        connection = None
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT Id_usuario,Dni,Cod_uni,Correo_uni,Contrasena from Usuario WHERE Correo_uni =%s", (usuario.correouni,))
                row = cursor.fetchone()

                if row:
                    # Print the row from the database
                    print(f"Row from database: {row}")

                    # Print the password stored in the database
                    print(f"Stored password: {row[4]}")
                    # Print the password provided by the user
                    print(f"Provided password: {usuario.contrasena}")

                    if row[4] == usuario.contrasena:  # Compare the passwords directly
                        # Print a message if the passwords match
                        print(f"Password match for user {usuario.correouni}")
                        user = {
                            "id_usuario": row[0],
                            "dni": row[1],
                            "cod_uni": row[2],
                            "correo_uni": row[3],
                            "contrasena": row[4]
                        }
                        # Convert the user dictionary to JSON
                        return json.dumps(user)
                    else:
                        # Print a message if the passwords do not match
                        print(
                            f"Password mismatch for user {usuario.correouni}")
                        return None
                else:
                    # Print a message if no user was found
                    print(f"No user found with email {usuario.correouni}")
                    return None

        except Exception as ex:
            print(f"Error: {ex}")  # Print any error that occurs
            raise Exception(ex)

        finally:
            if connection:
                connection.close()  # Ensure the database connection is closed
    @classmethod
    def update_contrasena(self,usuario):
            try:
                connection=get_connection()
                
                with connection.cursor() as cursor:
                    
                    cursor.execute("UPDATE usuario SET contrasena= %s WHERE id_usuario= %s;", (usuario.contrasena, usuario.id))
                    
                    affected_rows=cursor.rowcount
                    connection.commit()


                connection.close()
                return affected_rows
            
            except Exception as ex:
                raise Exception(ex)
        
    @classmethod
    def get_servicios_user(self,usuario):
        try:
            connection=get_connection()
            servicios=[]

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM REPORTE_FULL_U WHERE Id_usuario  = %s ;",(usuario.id))
                rows=cursor.fetchall()

                
                for row in rows :
                    servicio = venta(row[0], row[1], str(row[2]), row[3], row[4],row[5])
                    servicios.append(servicio.to_JSON())
            
            connection.close()
            print(servicios)
            return servicios
        
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_cantidad_servicios(self,id):
        try:
            connection=get_connection()
            services=[]

            with connection.cursor() as cursor:
                cursor.execute("""SELECT 
                    (
                    -- Subconsulta para contar registros de préstamos
                      COALESCE((SELECT COUNT(*) FROM Prestamo P WHERE P.Id_usuario = U.Id_usuario), 0) +
                     -- Subconsulta para contar registros de ventas
                      COALESCE((SELECT COUNT(*) FROM Venta V WHERE V.Id_usuario = U.Id_usuario), 0) +
                     -- Subconsulta para contar registros de alquileres
                      COALESCE((SELECT COUNT(*) FROM Alquiler A WHERE A.Id_usuario = U.Id_usuario), 0)
                    ) AS Total_registros
                    FROM
                        Usuario U 
                    WHERE 
                        Id_usuario  = %s ;""" , (id))
                
                row=cursor.fetchone()
                
            
            connection.close()
         
            return  row
                
        
        except Exception as ex:
            raise Exception(ex)