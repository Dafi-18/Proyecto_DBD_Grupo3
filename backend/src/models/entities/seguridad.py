from werkzeug.security import check_password_hash, generate_password_hash


class persona():

    def __init__(self, Dni, Primer_nombre=None, Segundo_nombre=None, Primer_apellido=None, Segundo_apellido=None, Celular=None) -> None:

        self.dni = Dni
        self.primer_nombre = Primer_nombre
        self.segundo_nombre = Segundo_nombre
        self.primer_apellido = Primer_apellido
        self.segundo_apellido = Segundo_apellido
        self.celular = Celular

    def to_JSON(self):
        return {
            'dni': self.dni,
            'primer_nombre': self.primer_nombre,
            'segundo_nombre': self.segundo_nombre,
            'primer_apellido': self.primer_apellido,
            'segundo_apellido': self.segundo_apellido,
            'celular': self.celular
        }


class usuario():

    def __init__(self, id_usuario, Dni=None, Cod_uni=None, Correo_uni=None, Contrasena=None) -> None:

        self.id = id_usuario
        self.dni = Dni
        self.codigouni = Cod_uni
        self.correouni = Correo_uni
        self.contrasena = Contrasena

    def to_JSON(self):
        return {
            'id_usuario': self.id,
            'dni': self.dni,
            'codigo_uni': self.codigouni,
            'correo_uni': self.correouni,
            'contrasena': self.contrasena
        }

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)

class venta:
    def __init__(self, nombre_producto, tipo_servicio, fecha_operacion, monto, estado_operacion, id_usuario):
        self.nombre_producto = nombre_producto
        self.tipo_servicio = tipo_servicio
        self.fecha_operacion = fecha_operacion
        self.monto = monto
        self.estado_operacion = estado_operacion
        self.id_usuario = id_usuario

    def to_JSON(self):
        # Implementa la lógica para convertir la instancia a un diccionario JSON
        # Puedes personalizar esto según tus necesidades
        return {
            "nombre_producto": self.nombre_producto,
            "tipo_servicio": self.tipo_servicio,
            "fecha_operacion": str(self.fecha_operacion),
            "monto": self.monto,
            "estado_operacion": self.estado_operacion,
            "id_usuario": self.id_usuario
        }
    
class prestamo:
    def __init__(self, nombre_producto, tipo_servicio, fecha_operacion, hora_inicio, hora_fin, fecha_devolucion, estado_operacion, id_usuario):
        self.nombre_producto = nombre_producto
        self.tipo_servicio = tipo_servicio
        self.fecha_operacion = fecha_operacion
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.fecha_devolucion = fecha_devolucion
        self.estado_operacion = estado_operacion
        self.id_usuario = id_usuario

    def to_JSON(self):
        return {
            "nombre_producto": self.nombre_producto,
            "tipo_servicio": self.tipo_servicio,
            "fecha_operacion": str(self.fecha_operacion),
            "hora_inicio": str(self.hora_inicio),
            "hora_fin": str(self.hora_fin),
            "fecha_devolucion": str(self.fecha_devolucion),
            "estado_operacion": self.estado_operacion,
            "id_usuario": self.id_usuario
        }

class alquiler:
    def __init__(self, nombre_producto, tipo_servicio, fecha_operacion, hora_inicio, hora_fin, fecha_devolucion, monto, estado_operacion, id_usuario):
        self.nombre_producto = nombre_producto
        self.tipo_servicio = tipo_servicio
        self.fecha_operacion = fecha_operacion
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.fecha_devolucion = fecha_devolucion
        self.monto = monto
        self.estado_operacion = estado_operacion
        self.id_usuario = id_usuario

    def to_JSON(self):
        return {
            "nombre_producto": self.nombre_producto,
            "tipo_servicio": self.tipo_servicio,
            "fecha_operacion": str(self.fecha_operacion),
            "hora_inicio": str(self.hora_inicio),
            "hora_fin": str(self.hora_fin),
            "fecha_devolucion": str(self.fecha_devolucion),
            "monto": self.monto,
            "estado_operacion": self.estado_operacion,
            "id_usuario": self.id_usuario
        }
