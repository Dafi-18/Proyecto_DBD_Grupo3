from utils.dateformat import DateFormat

class Noticia():
    def __init__(self, Id_noticia, Id_administrador=None, Fecha=None, Titulo=None, Descripcion=None) -> None:
        self.Id_noticia = Id_noticia
        self.Id_administrador = Id_administrador
        self.Fecha = Fecha
        self.Titulo = Titulo
        self.Descripcion = Descripcion        


    def to_JSON(self):
        return {
            'Id_noticia': self.Id_noticia,
            'Id_administrador': self.Id_administrador,
            'Fecha': DateFormat.convert_date(self.Fecha),
            'Titulo': self.Titulo,
            'Descripcion': self.Descripcion,
        }