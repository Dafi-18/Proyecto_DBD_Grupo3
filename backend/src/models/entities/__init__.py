class Product():
    def __init__(self, id_articulo, nombre_articulo, tipo_articulo, cantidad, descripcion, precio_unitario, disponibilidad):
        self.id_articulo = id_articulo
        self.nombre_articulo = nombre_articulo
        self.tipo_articulo = tipo_articulo
        self.cantidad = cantidad
        self.descripcion = descripcion
        self.precio_unitario = precio_unitario
        self.disponibilidad = disponibilidad

    def to_JSON(self):
        return {
            'id_articulo': self.id_articulo,
            'nombre_articulo': self.nombre_articulo,
            'tipo_articulo': self.tipo_articulo,
            'cantidad': self.cantidad,
            'descripcion': self.descripcion,
            'precio_unitario': self.precio_unitario,
            'disponibilidad': self.disponibilidad
        }
