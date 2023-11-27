class Estadisticas:
    def __init__(self, ventas, alquileres, prestamos, total_recaudado_alquileres, total_recaudado_ventas, articulo_mas_alquilado, articulo_menos_alquilado, articulo_mas_prestado, articulo_menos_prestado, articulo_mas_vendido, articulo_menos_vendido):
        self.ventas = ventas
        self.alquileres = alquileres
        self.prestamos = prestamos
        self.total_recaudado_alquileres = total_recaudado_alquileres
        self.total_recaudado_ventas = total_recaudado_ventas
        self.articulo_mas_alquilado = articulo_mas_alquilado
        self.articulo_menos_alquilado = articulo_menos_alquilado
        self.articulo_mas_prestado = articulo_mas_prestado
        self.articulo_menos_prestado = articulo_menos_prestado
        self.articulo_mas_vendido = articulo_mas_vendido
        self.articulo_menos_vendido = articulo_menos_vendido

    def to_JSON(self):
        return {
            'ventas': self.ventas,
            'alquileres': self.alquileres,
            'prestamos': self.prestamos,
            'total_recaudado_alquileres': self.total_recaudado_alquileres,
            'total_recaudado_ventas': self.total_recaudado_ventas,
            'articulo_mas_alquilado': self.articulo_mas_alquilado,
            'articulo_menos_alquilado': self.articulo_menos_alquilado,
            'articulo_mas_prestado': self.articulo_mas_prestado,
            'articulo_menos_prestado': self.articulo_menos_prestado,
            'articulo_mas_vendido': self.articulo_mas_vendido,
            'articulo_menos_vendido': self.articulo_menos_vendido
        }
