__author__ = 'Luciano'

import serial

port = serial.Serial(port = '/dev/ttyAMA0',
                 baudrate=9600,
                 parity=serial.PARITY_NONE,
                 stopbits=serial.STOPBITS_ONE,
                 bytesize=serial.EIGHTBITS,
                 timeout=3)


def enviarYObtenerRespuesta(toSend):
    port.write(str(toSend) + "\n")
    recv = port.readline()
    return recv