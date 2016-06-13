__author__ = 'Luciano Mantovani'

import time
import datetime

def retrieve_conversion(data):
    return data.split(".")[0]
def retrieve_timestamp(data):
    return data.split(".")[1]

def generate_timestamp(current_relative_ts, last_relative_ts, base_ts):
    #base_ts is obtained w/get_pi_tiemstamp at begginning of continuous conversion
    timestamp_ms = int(current_relative_ts) - int(last_relative_ts) + int(base_ts)

    return datetime.datetime.fromtimestamp(timestamp_ms / 1000) #returns a string with the formatted timestamp

def get_pi_timestamp_ms():
    return int(round(time.time() * 1000)) #returns a strimg with a raw timestamp measured in miliseconds