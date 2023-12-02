class Venta():
    def __init__(self, id_venta, id_usuario, fecha_venta, monto_final, estado_pago):
        self.id_venta = id_venta
        self.id_usuario = id_usuario
        self.fecha_venta = fecha_venta
        self.monto_final = monto_final
        self.estado_pago = estado_pago

    def to_JSON(self):
        return {
            'id_venta': self.id_venta,
            'id_usuario': self.id_usuario,
            'fecha_venta': self.fecha_venta,
            'monto_final': self.monto_final,
            'estado_pago': self.estado_pago
        }
      
class Detalle_Venta():
    def __init__(self, id_venta, id_articulo, medio_pago, cantidad, subtotal):
        self.id_venta = id_venta
        self.id_articulo = id_articulo
        self.medio_pago = medio_pago
        self.cantidad = cantidad
        self.subtotal = subtotal

    def to_JSON(self):
        return {
            'id_venta': self.id_venta,
            'id_articulo': self.id_articulo,
            'medio_pago': self.medio_pago,
            'cantidad': self.cantidad,
            'subtotal': self.subtotal
        }
            
class Prestamo():
    def __init__(self, id_prestamo, id_usuario, id_articulo, fecha_prestamo, hora_prestamo, fecha_devolucion, hora_devolucion, estado_prestamo):
        self.id_prestamo = id_prestamo
        self.id_usuario = id_usuario
        self.id_articulo = id_articulo
        self.fecha_prestamo = fecha_prestamo
        self.hora_prestamo = hora_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.hora_devolucion = hora_devolucion
        self.estado_prestamo = estado_pago

    def to_JSON(self):
        return {
            'id_prestamo': self.id_prestamo,
            'id_usuario': self.id_usuario,
            'id_articulo': self.id_articulo,
            'fecha_prestamo': self.fecha_prestamo,
            'hora_prestamo': self.hora_prestamo,
            'fecha_devolucion': self.fecha_devolucion,
            'hora_devolucion': self.hora_devolucion,
            'estado_prestamo': self.estado_prestamo
        }
    
class Alquiler():
    def __init__(self, id_alquiler, id_usuario, id_articulo, fecha_alquiler, hora_inicio, hora_fin, medio_pago, monto, estado_alquiler):
        self.id_alquiler = id_alquiler
        self.id_usuario = id_usuario
        self.id_articulo = id_articulo
        self.fecha_alquiler = fecha_alquiler
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.medio_pago = medio_pago
        self.monto = monto
        self.estado_alquiler = estado_alquiler

    def to_JSON(self):
        return {
            'id_alquiler': self.id_alquiler,
            'id_usuario': self.id_usuario,
            'id_articulo': self.id_articulo,
            'fecha_alquiler': self.fecha_alquiler,
            'hora_inicio': self.hora_inicio,
            'hora_fin': self.hora_fin,
            'medio_pago': self.medio_pago,
            'monto': self.monto,
            'estado_alquiler': self.estado_alquiler
        }
