__author__ = 'Luciano Mantovani'

import time
import datetime

def retrieve_conversion(data):
    #data.split(".")[0]
    #data[0].replace('\r',' ').replace('\n',' ')
    return data[:5] #el dato es medicion.tstamp.medicion.2basuras, entonces saco la primera medicion mas el tstamp y las dos basuras, tambien los puntos.
    #return data[0]
def retrieve_timestamp(data):
    #data.split(".")[1]
       #Al igual que en retrieve_conversion(), solo que ahora dejo el tstamp y elimino el resto.
    #return dato1    
    return data[6:].replace("\r"," ").replace("\n"," ")
def retieve_pin(data):
    return  data[7]


def generate_timestamp(current_relative_ts, last_relative_ts, base_ts):
    #base_ts is obtained w/get_pi_tiemstamp at begginning of continuous conversion
    current_relative = int(current_relative_ts)
    #current = map(int, current_relative.strip().split('\r\n'))
    last_relative = int(last_relative_ts)
    base = int(base_ts)
    timestamp_ms = current_relative - last_relative + base  
    #timestamp = map(int, timestamp.strip().split('\r\n'))    
    return datetime.datetime.fromtimestamp(timestamp_ms / 1000) #returns a string with the formatted timestamp

def get_pi_timestamp_ms():
    return int(round(time.time() * 1000)) #returns a int with a raw timestamp measured in miliseconds
