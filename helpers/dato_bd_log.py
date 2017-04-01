

class Dato_db_log:

    def __init__(self, fecha, hora, comando, respuesta):
        self.fecha = fecha
        self.hora = hora
        self.comando = comando
        self.respuesta = respuesta
        self.id = id(self)
