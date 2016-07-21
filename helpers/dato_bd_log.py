

class Dato_db_log:

    def __init__(self, dtime, ttime, comand, respond):
        self.dtime = dtime
        self.ttime = ttime
        self.comand = comand
        self.respond = respond
        self.id = id(self)
