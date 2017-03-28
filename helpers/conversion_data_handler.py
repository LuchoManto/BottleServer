__author__ = 'Luciano Mantovani'

import time
import datetime

#LA INFORMACION QUE LLEGA DESDE LA PLACA TIENE EL SIGUIENTE FORMATO :
#               TIPO DE CONVERSION, PIN, CONVERSION, TIMESTAMP
#EN CANTIDADES DE CARACTERES SON :
#               2, 1, 5, 5,

def retrieve_conversion(data):
    return data[5:10]
def retrieve_timestamp(data):
       #Al igual que en retrieve_conversion(), solo que ahora dejo el tstamp y elimino el resto.
    return data[11:]
def retieve_pin(data):
    return data[3]

def generate_timestamp(current_relative_ts, last_relative_ts, base_ts):
    current_relative = int(current_relative_ts)
    last_relative = int(last_relative_ts)
    base = int(base_ts)
    timestamp_ms = current_relative - last_relative + base
    return datetime.datetime.fromtimestamp(timestamp_ms / 1000) #returns a string with the formatted timestamp

def get_pi_timestamp_ms():
    return int(round(time.time() * 1000)) #returns a int with a raw timestamp measured in miliseconds
