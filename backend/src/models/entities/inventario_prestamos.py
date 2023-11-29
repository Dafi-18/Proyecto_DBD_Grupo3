class Inventario_Prestamos():
    def __init__(self, id_articulo, nombre_articulo, cantidad):
        self.id_articulo = id_articulo
        self.nombre_articulo = nombre_articulo
        self.cantidad = cantidad

    def to_JSON(self):
        return {
            'id_articulo': self.id_articulo,
            'nombre_articulo': self.nombre_articulo,
            'cantidad': self.cantidad
        }

class Articulos_prestados():
    def __init__(self, nombre_articulo, cantidad):
        self.nombre_articulo = nombre_articulo
        self.cantidad = cantidad

    def to_JSON(self):
        return {
            'nombre_articulo': self.nombre_articulo,
            'cantidad': self.cantidad
        }