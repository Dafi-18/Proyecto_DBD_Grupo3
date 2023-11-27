from  werkzeug.security import check_password_hash,generate_password_hash

class persona():

    def __init__(self,Dni,Primer_nombre=None,Segundo_nombre=None,Primer_apellido=None,Segundo_apellido=None,Celular=None) -> None:
        
        self.dni = Dni
        self.primer_nombre= Primer_nombre
        self.segundo_nombre = Segundo_nombre
        self.primer_apellido = Primer_apellido
        self.segundo_apellido = Segundo_apellido
        self.celular = Celular

    def to_JSON(self):
        return {
            'dni' : self.dni,
            'primer_nombre' : self.primer_nombre,
            'segundo_nombre' : self.segundo_nombre,
            'primer_apellido' : self.primer_apellido,
            'segundo_apellido' : self.segundo_apellido,
            'celular' : self.celular
        }

class usuario():

    def __init__(self,id_usuario,Dni=None,Cod_uni=None,Correo_uni=None,Contrasena=None) -> None:
        
        self.id = id_usuario
        self.dni= Dni
        self.codigouni = Cod_uni
        self.correouni = Correo_uni
        self.contrasena = Contrasena

    def to_JSON(self):
        return {
            'id_usuario' : self.id,
            'dni' : self.dni,
            'codigo_uni' : self.codigouni,
            'correo_uni' : self.correouni,
            'contrasena' : self.contrasena
        }
    
    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password,password)