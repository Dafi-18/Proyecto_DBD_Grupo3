class Encuesta():
    def __init__(self,Id_encuesta, Id_administrador, Fecha_apertura, Fecha_cierre, Cantidad_preguntas, Cantidad_respuestas, Estado_encuesta):
        self.Id_encuesta = Id_encuesta
        self.Id_administrador = Id_administrador
        self.Fecha_apertura = Fecha_apertura
        self.Fecha_cierre = Fecha_cierre
        self.Cantidad_preguntas = Cantidad_preguntas
        self.Cantidad_respuestas = Cantidad_respuestas
        self.Estado_encuesta = Estado_encuesta
        
    def to_JSON(self):
        return{
            'Id_encuesta': self.Id_encuesta,
            'Id_administrador': self.Id_administrador,
            'Fecha_apertura': self.Fecha_apertura,
            'Fecha_cierre': self.Fecha_cierre,
            'Cantidad_preguntas': self.Cantidad_preguntas,
            'Cantidad_respuestas': self.Cantidad_respuestas,
            'Estado_encuesta': self.Estado_encuesta
            
        }