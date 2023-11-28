class Inventario_Ventas():
    def __init__(self, id_articulo, nombre_articulo, precio_unitario, cantidad):
        self.id_articulo = id_articulo
        self.nombre_articulo = nombre_articulo
        self.precio_unitario = precio_unitario
        self.cantidad = cantidad

    def to_JSON(self):
        return {
            'id_articulo': self.id_articulo,
            'nombre_articulo': self.nombre_articulo,
            'precio_unitario': self.precio_unitario,
            'cantidad': self.cantidad
        }
