__author__ = 'Luciano'

import serial
from apscheduler.schedulers.background import BackgroundScheduler
import thread

class ClaseSerial:

    global buffer_intermedio
    buffer_intermedio=[]

    def __init__(self):
        self.port = serial.Serial(port = '/dev/ttyAMA0',
                         baudrate=9600,
                         parity=serial.PARITY_NONE,
                         stopbits=serial.STOPBITS_ONE,
                         bytesize=serial.EIGHTBITS,
                         timeout=3)
        self.keepGoing = 1
        self.sched = BackgroundScheduler()

    def enviarYObtenerRespuesta(self,toSend):
        self.port.write(str(toSend) + "\n")
        recv = self.port.readline()
        #todo: save in db: recv, in command log table
        return recv


    def recibir(self):
        recv = self.port.readline()
        return recv

    def startSched(self):
        self.sched.start()


    def keepAlive(self):
        send = "p"
        recv = self.enviarYObtenerRespuesta(send)
        #todo: save in db: recv, in command log table


    def triggerStart(self):
        send = "SSE,0,1"
        recv = self.enviarYObtenerRespuesta(send)
        #todo: save in db: recv, in command log table
        send = "SGA,3"
        recv = self.enviarYObtenerRespuesta(send)
        #todo: save in db: recv, in command log table
        send = "PWM"
        recv = self.enviarYObtenerRespuesta(send)
        #todo: save in db: recv, in command log table

        send = "ST"
        recv = self.enviarYObtenerRespuesta(send)
        #todo: save in db: recv, in command log table

        self.keepGoing = 1
        try:
            thread.start_new_thread(self.keepGoing_start())
        except:
            print "Error: unable to start thread"

    def triggerEnd(self):

        self.keepGoing_end()
        send = "s"
        recv = self.enviarYObtenerRespuesta(send)
        #todo: save in db: recv, in command log table
        send = "NTP"
        recv = self.enviarYObtenerRespuesta(send)
        #todo: save in db: recv, in command log table

    def keepGoing_start(self):
        #todo: save in db: "thread started", in monitor log table
        while self.keepGoing == 1:
            #Miro en un buffer compartido entre el productor y consumidor,
            #si no esta vacio entonces puedo recibir, sino tendre que esperar
            #a que vuelva a tener algo dentro.
            send = 'e'
            toprove = self.enviarYObtenerRespuesta(send)
            if toprove != 504:
                toSave = self.recibir()
                #todo: save in db: toSave, in sensor data table
                #todo: save in db: "thread ended", in monitor log table

    def keepGoing_end(self):
        self.keepGoing = 0


class ClaseSerialPcTemp:
    def __init__(self):
        self.keepGoing = 1
        self.sched = BackgroundScheduler()

    def enviarYObtenerRespuesta(self,toSend):
        return


    def recibir(self):
        return

    def startSched(self):
        self.sched.start()


    def keepAlive(self):
        send = "p"
        recv = self.enviarYObtenerRespuesta(send)
        #todo: save in db: recv, in command log table


    def triggerStart(self):
        send = "SSE,0,1"
        recv = self.enviarYObtenerRespuesta(send)
        #todo: save in db: recv, in command log table
        send = "SGA,3"
        recv = self.enviarYObtenerRespuesta(send)
        #todo: save in db: recv, in command log table
        send = "PWM"
        recv = self.enviarYObtenerRespuesta(send)
        #todo: save in db: recv, in command log table

        send = "ST"
        recv = self.enviarYObtenerRespuesta(send)
        #todo: save in db: recv, in command log table

        self.keepGoing = 1
        try:
            thread.start_new_thread(self.keepGoing_start())
        except:
            print "Error: unable to start thread"

    def triggerEnd(self):

        self.keepGoing_end()
        send = "s"
        recv = self.enviarYObtenerRespuesta(send)
        #todo: save in db: recv, in command log table
        send = "NTP"
        recv = self.enviarYObtenerRespuesta(send)
        #todo: save in db: recv, in command log table

    def keepGoing_start(self):
        #todo: save in db: "thread started", in monitor log table
        while self.keepGoing == 1:
            toSave = self.recibir()
            #todo: save in db: toSave, in sensor data table
        #todo: save in db: "thread ended", in monitor log table
    def keepGoing_end(self):
        self.keepGoing = 0
