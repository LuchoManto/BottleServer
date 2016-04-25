__author__ = 'Luciano'
from apscheduler.schedulers.background import BackgroundScheduler
from helpers.serial_uart import *

sched = BackgroundScheduler()

def startSched():
    sched.start()


def keepAlive():

	send = "p"
	recv = enviarYObtenerRespuesta(send)


def triggerStart():
    send = "SSE,0,1"
    recv = enviarYObtenerRespuesta(send)
    send = "SGA,3"
    recv = enviarYObtenerRespuesta(send)
    send = "PWM"
    recv = enviarYObtenerRespuesta(send)



    # thread1 = thread.start_new_thread(keepAlive)
    # sched.add_job(keepAlive, 'cron', second=8)


def triggerEnd():
    send = "NTP"
    recv = enviarYObtenerRespuesta(send)