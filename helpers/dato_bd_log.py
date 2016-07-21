

class Dato_db_log:

    def __init__(self, tdate, ttime, comand, respond):
        self.tdate = tdate
        self.ttime = ttime
        self.comand = comand
        self.respond = respond
        self.id = id(self)
