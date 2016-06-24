__author__ = 'Luciano Mantovani & Ignacio Sambataro'

import serial
from apscheduler.schedulers.background import BackgroundScheduler
import threading
import time
import collections

from helpers.base_datos import*
from helpers.conversion_data_handler import*

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
        self.buffer_mediciones = collections.deque(maxlen=20)
        self.e = threading.Event()
	self.st1 = 0
	self.waitt = 0
	self.waitt2 = 0

    def enviarYObtenerRespuesta(self,toSend):
        #self.port.Open()
        self.port.flushInput()
        self.port.flushOutput()
        self.port.write(str(toSend) + "\n")
        time.sleep(1)
	self.port.flushOutput()
        recv = self.port.read(20)
        time.sleep(1)
        return recv

    def recibir(self):
        self.port.flushInput()
        self.port.flushOutput()
        recv = self.port.read(20)
        time.sleep(1)
        return recv

    def startSched(self):
        self.sched.start()

    def keepAlive(self):
        send = "p"
        recv = self.enviarYObtenerRespuesta(send)
        cargar_comand_log(send, recv)
        #todo: save in db: recv, in command log table
    
    def kill_threads(self):
	
	self.waitt = 1
	self.waitt2= 1
	#self.e.wait()
	#self.e1.wait()
	#cargar_comand_log('wait', '1')

    def start_conversion_ST(self):
        if self.waitt == 1 and self.waitt2 == 1:
	    #self.st1 = 0
	    self.e.set()
	else:
	    self.st1 = 1
            try:
            	# thread.start_new_thread(self.keepGoing_start())
            	t1 = threading.Thread(name='producer',
                                  target=self.loop_productor,
                                  args=(self.e,))
            	t1.start()

            except:
            	print "Error: unable to start thread-producer"

            try:
            	t2 = threading.Thread(name='consumer',
                                  target=self.loop_consumidor,
                                  args=(self.e,))
            	t2.start()
            except:
            	print "Error: unable to start thread-consumer"

         
    def triggerStart(self):
        print "disparo"

        send = "SSE,0,1"
        recv = self.enviarYObtenerRespuesta(send)
        cargar_comand_log(send, recv)
        #todo: save in db: recv, in command log table

        send = "SGA,3"
        recv = self.enviarYObtenerRespuesta(send)
        cargar_comand_log(send, recv)
        #todo: save in db: recv, in command log table

        send = "PWM"
        recv = self.enviarYObtenerRespuesta(send)
        cargar_comand_log(send, recv)
        #todo: save in db: recv, in command log table

        send = "ST"
        recv = self.enviarYObtenerRespuesta(send)
        cargar_comand_log(send, recv)
        #todo: save in db: recv, in command log table

        self.keepGoing = 1
        try:
            #thread.start_new_thread(self.keepGoing_start())
            t1 = threading.Thread(name='producer',
                        target=self.loop_productor,
                        args=[])
            t1.start()

        except:
            print "Error: unable to start thread"

        try:
            t2 = threading.Thread(name='consumer',
                        target=self.loop_consumidor,
                        args=[])
            t2.start()
        except:
            print "Error: unable to start thread"


    def triggerEnd(self):

        self.keepGoing_end()
        send = "s"
        recv = self.enviarYObtenerRespuesta(send)
        cargar_comand_log(send, recv)
        #todo: save in db: recv, in command log table
        send = "NTP"
        recv = self.enviarYObtenerRespuesta(send)
        cargar_comand_log(send, recv)
	#todo: save in db: recv, in command log table

    #thread que recibe los datos desde la uart y los guarda en el buffer. PRODUCTOR
    def loop_productor(self, e):

        #todo: guardar en la base de datos: "producer thread started", en la tabla de log del monitor
        #todo: vaciar buffer

        #todo: crear thread que ejecute la funcion guardarDatosContinuos
        #todo: guardar en la base de datos: "consumer thread started", en la tabla de log del monitor

        while 1:
            #toSave = self.recibir()
	    #toSave3 = retrieve_conversion(toSave)
            if self.waitt2 == 1:
		cargar_comand_log('procesor ended','1')
		self.waitt2 = 0
		#self.e.wait()
		break
	    #else:
	    toSave = self.recibir()
	    self.buffer_mediciones.append(toSave)
	    self.e.set()
            #toSave3 = retrieve_conversion(toSave)
            #self.e.set()

        #loop forever:
        #guardar en buffer
        #despertar thread consumidor
        #if sigue conversion
        #volver al loop
        #else
        # guardar "producer thread ended" en la db
        #break loop
        #endloop

    def keepGoing_end(self):
        self.keepGoing = 0
        #todo: guardar en la base de datos que se activo el fin de adquisicion de mediciones



    def loop_consumidor(self, e): #thread que guarda los datos leidos del buffer en la base de datos. CONSUMIDOR
        last = "0"
        while 1:
            if not self.buffer_mediciones:
            	if self.keepGoing == 0:
                    cargar_comand_log('consumer thread ended', '0')
                    #todo: guardar "termino thread consumidor" en la db, en la tabla de log
                    self.e.wait()
		    break
                elif self.waitt == 1:
		    self.waitt=0
                    cargar_comand_log('wait primer consu', '3')
		    self.e.wait()
                    #todo: sleep hasta que haya algo en el buffer
            else:
                toSave=self.buffer_mediciones.popleft()		
		if self.waitt == 1:
		    cargar_comand_log('wait consu','2')
		    self.waitt =0
		    #self.e.wait()
		    break
                else:
		    toSave1 = retrieve_conversion(toSave)
		    current = retrieve_timestamp(toSave)
                    base = get_pi_timestamp_ms()
                    tstamp = generate_timestamp(current, last, base)
                    cargar_medicion(tstamp,"0",toSave1)
                    last = current
                #todo: despertar al otro thread
                #todo: guardar "termino thread consumidor" en la db, en la tabla de mediciones
