

class Dato_db_log:

    def __init__(self, fecha, hora, comando, respuesta):
        self.tdate = fecha
        self.ttime = hora
        self.comand = comando
        self.respond = respuesta
        self.id = id(self)
