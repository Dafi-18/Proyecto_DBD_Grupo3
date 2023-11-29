class Calendario():
    def __init__(self, id_hora, fecha, hora_inicio, hora_fin , estado):
        self.id_hora = id_hora
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.estado = estado

    def to_JSON(self):
        return {
            'id_hora': self.id_hora,
            'fecha': self.fecha,
            'hora_inicio': self.hora_inicio,
            'hora_fin': self.hora_fin,
            'estado': self.estado
        }