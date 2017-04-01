
class Dato_db:

    def __init__(self, hora, pin, medicion):
        self.hora = hora
        self.pin = pin
        self.medicion = medicion
        self.id = id(self)

