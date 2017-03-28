__author__ = 'Luciano Mantovani & Ignacio Sambataro'

import serial
import threading
import time
import collections
import re

from helpers.base_datos import*
from helpers.conversion_data_handler import*



class ClaseSerial:



    def __init__(self):

        self.port = serial.Serial(port = '/dev/ttyAMA0',
        #self.port = serial.Serial(port = 'COM6',
                                  baudrate=9600,
                                  parity=serial.PARITY_NONE,
                                  stopbits=serial.STOPBITS_ONE,
                                  bytesize=serial.EIGHTBITS,
                                  timeout=3)
        self.keepGoing = 1
        self.buffer_mediciones = collections.deque(maxlen=20)
        self.e = threading.Event()
        self.st1 = 0
        self.waitt = 0
        self.waitt2 = 0

    def enviarYObtenerRespuesta(self, toSend):
        # self.port.Open()
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
        time.sleep(1)
        recv = self.port.readline()
        time.sleep(1)
        return recv

    def keepAlive(self):
        send = "p"
        recv = self.enviarYObtenerRespuesta(send)
        cargar_comand_log(send, recv)
        # todo: save in db: recv, in command log table
    
    def kill_threads(self):

        self.waitt = 1
        self.e.wait()
        # self.waitt2= 1
        # self.e.wait()
        # self.e1.wait()
        cargar_comand_log('kill', '1')

    def start_conversion_ST(self):
        if self.waitt == 1:
            # self.e.set()
            self.waitt = 0
            cargar_comand_log('restart', '0')
        try:
            self.e.set()
            # thread.start_new_thread(self.keepGoing_start())
            t1 = threading.Thread(name='producer', target=self.loop_productor, args=(self.e,))
            cargar_comand_log('producer on', 'ok')
            t2 = threading.Thread(name='consumer', target=self.loop_consumidor, args=(self.e,))
            cargar_comand_log('consumer on', 'ok')
            t1.start()
            time.sleep(0.5)
            t2.start()
        except:
            print "Error: unable to start thread-producer"
         
    def triggerStart(self):
        print "disparo"

        send = "SSE,0,1"
        recv = self.enviarYObtenerRespuesta(send)
        cargar_comand_log(send, recv)
        # todo: save in db: recv, in command log table

        send = "SGA,3"
        recv = self.enviarYObtenerRespuesta(send)
        cargar_comand_log(send, recv)
        # todo: save in db: recv, in command log table

        send = "PWM"
        recv = self.enviarYObtenerRespuesta(send)
        cargar_comand_log(send, recv)
        # todo: save in db: recv, in command log table

        send = "ST"
        recv = self.enviarYObtenerRespuesta(send)
        cargar_comand_log(send, recv)
        # todo: save in db: recv, in command log table

        self.keepGoing = 1
        try:
            # thread.start_new_thread(self.keepGoing_start())
            t1 = threading.Thread(name='producer', target=self.loop_productor, args=(self.e,))
            t1.start()

        except:
            print "Error: unable to start thread"

        try:
            t2 = threading.Thread(name='consumer', target=self.loop_consumidor, args=(self.e,))
            t2.start()
        except:
            print "Error: unable to start thread"


    def triggerEnd(self):

        self.keepGoing_end()
        send = "s"
        recv = self.enviarYObtenerRespuesta(send)
        cargar_comand_log(send, recv)
        # todo: save in db: recv, in command log table
        send = "NTP"
        recv = self.enviarYObtenerRespuesta(send)
        cargar_comand_log(send, recv)
        # todo: save in db: recv, in command log table
        # thread que recibe los datos desde la uart y los guarda en el buffer. PRODUCTOR

    def loop_productor(self, e):

        #TODO: guardar en la base de datos: "producer thread started", en la tabla de log del monitor
        #todo: vaciar buffer

        #todo: crear thread que ejecute la funcion guardarDatosContinuos
        #todo: guardar en la base de datos: "consumer thread started", en la tabla de log del monitor

        while self.waitt == 0:
            # toSave = self.recibir()
            #  toSave3 = retrieve_conversion(toSave)
            # if self.waitt == 1:
            #  cargar_comand_log('procesor ended','1')
            #  break
            #  else:
            toSave = self.recibir()
            cargar_comand_log('recibe', toSave)
            time.sleep(0.8)
            if self.check_entry(toSave):
                self.buffer_mediciones.append(toSave)
                e.set()
            # toSave3 = retrieve_conversion(toSave)
            # self.e.set()
        # loop forever:
        # guardar en buffer
        # despertar thread consumidor
        # if sigue conversion
        # volver al loop
        # else
        # guardar "producer thread ended" en la db
        # break loop
        # endloop

    def keepGoing_end(self):
        self.keepGoing = 0
        # todo: guardar en la base de datos que se activo el fin de adquisicion de mediciones



    def loop_consumidor(self, e):
        # thread que guarda los datos leidos del buffer en la base de datos. CONSUMIDOR
        last = "0"
        cargar_comand_log('ENTRO CONSUMIDOR',)
        while e.is_set():
            if self.buffer_mediciones:
                toSave = self.buffer_mediciones.popleft()
                cargar_comand_log('ENTRO WHILE',toSave)
                if not toSave:
                    cargar_comand_log('wait es',self.waitt)
                if self.waitt == 1:
                    cargar_comand_log('string null','exit')
                    break
                #if not self.waitt == 1:
                else:
                    conversion = retrieve_conversion(toSave)
                    current = retrieve_timestamp(toSave)
                    pin = retieve_pin(toSave)
                    cargar_comand_log('medicion es', conversion)
                    base = get_pi_timestamp_ms()
                    tstamp = generate_timestamp(current, last, base)
                    cargar_medicion(tstamp, pin, conversion)
                    last = current
            # else:
                # cargar_comand_log("wait consu",'2')
                        # self.waitt = 0
                        # break
            else:
                if self.keepGoing == 0:
                    cargar_comand_log('consumer thread ended', '0')
                    # todo: guardar "termino thread consumidor" en la db, en la tabla de log
                    break
                elif self.waitt == 1:
                    #self.waitt=0
                    cargar_comand_log('cola vacia', '3')
                    break
                        #todo: sleep hasta que haya algo en el buffer
        cargar_comand_log('salio del while', 'bien')


    def check_entry(self, data):
        pattern = re.compile("^\d{5,5}\W\d{5,5}")
        return pattern.match(data)


