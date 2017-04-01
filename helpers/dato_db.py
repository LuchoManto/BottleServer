
class Dato_db:

    def __init__(self, hora, pin, medicion):
        self.tdate = hora
        self.pin = pin
        self.electrostatic = medicion
        self.id = id(self)

