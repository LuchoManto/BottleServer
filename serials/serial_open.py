__author__ = 'Gaston'

import serial

# Configuramos el puerto serials.
serial = serial.Serial(port="COM4",
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

def main():
    print "Iniciado"
    while 1:
        command = serial.readline()
        print 'Recieved from NODEMcu: ' + command

        if command == 'respuesta\n':
            enviar = '04'
            print 'Send to Node: ' + str(enviar.decode("hex"))
            serial.write(enviar.decode("hex"))

    return

if __name__ == "__main__":
    main()