__author__ = 'Luciano'

import serial
from apscheduler.schedulers.background import BackgroundScheduler
import threading
import time
import collections

class ClaseSerial:


    def __init__(self):
        self.port = serial.Serial(port = '/dev/ttyAMA0',
                                  baudrate=9600,
                                  parity=serial.PARITY_NONE,
                                  stopbits=serial.STOPBITS_ONE,
                                  bytesize=serial.EIGHTBITS,
                                  timeout=3)
        self.keepGoing = 1
        self.sched = BackgroundScheduler()
        self.buffer_mediciones = collections.deque(maxlen=10)

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
        print "disparo"
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
            #thread.start_new_thread(self.keepGoing_start())
            t1 = threading.Thread(name='producer',
                        target=self.loop_productor,
                        args=(self))

        except:
            print "Error: unable to start thread"

        try:
            t1 = threading.Thread(name='consumer',
                        target=self.loop_consumidor,
                        args=(self))

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

    #thread que recibe los datos desde la uart y los guarda en el buffer. PRODUCTOR
    def loop_productor(self):
        #todo: guardar en la base de datos: "producer thread started", en la tabla de log del monitor
        #todo: vaciar buffer

        #loop forever:
        #guardar en buffer
        #despertar thread consumidor
        #if sigue conversion
        #volver al loop
        #else
        # guardar "producer thread ended" en la db
        #break loop
        #endloop

        while self.keepGoing == 1:
            toSave = self.recibir()
            #todo: save in db: toSave, in sensor data table
            #todo: save in db: "thread ended", in monitor log table

    def keepGoing_end(self):
        self.keepGoing = 0
        #todo: guardar en la base de datos que se activo el fin de adquisicion de mediciones



    def loop_consumidor(self): #thread que guarda los datos leidos del buffer en la base de datos. CONSUMIDOR
        while 1:
            if self.buffer_mediciones:
                if self.keepGoing == 0:
                    #todo: guardar "termino thread consumidor" en la db, en la tabla de log
                    break
                else:
                    #todo: sleep hasta que haya algo en el buffer
            else:
                self.buffer_mediciones.popleft()
                #todo: despertar al otro thread
                #todo: guardar "termino thread consumidor" en la db, en la tabla de mediciones





































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
            print "thrediando como un campeon"
            time.sleep(1)
            #todo: save in db: toSave, in sensor data table
        #todo: save in db: "thread ended", in monitor log table
        return
    def keepGoing_end(self):
        self.keepGoing = 0
        # print "no more thread"
        return
