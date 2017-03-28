__author__ = 'Ignacio'

import MySQLdb

from helpers.dato_db import *
from helpers.dato_bd_log import *

pila_medicion = []
pila_comando = []

def cargar_comand_log(valor,respuesta):
    db = MySQLdb.connect("localhost", "ignacio", "mantosamba", "SensorCampoElectroEstatico")
    curs = db.cursor()
    curs.execute("""INSERT INTO comandlog
        values(CURRENT_DATE(), NOW(),%s, %s)""", (valor, respuesta,))
    db.commit()
    db.close()

def cargar_medicion(timestamp, pin, valor):
    db = MySQLdb.connect("localhost", "ignacio", "mantosamba", "SensorCampoElectroEstatico")
    curs = db.cursor()
    curs.execute("""INSERT INTO medicion
            values(%s, %s,%s)""", (timestamp, pin, valor,))
    db.commit()
    db.close()

def cargar_desde_bd_medicion():
    pila_medicion = []
    db = MySQLdb.connect("localhost", "ignacio", "mantosamba", "SensorCampoElectroEstatico")
    curs = db.cursor()
    curs.execute("SELECT timestamp, pin, medicion FROM medicion")
    for (tdate, pin, electrostatic) in curs:
        dato_medicion = Dato_db(tdate, pin, electrostatic)
        pila_medicion.append(dato_medicion)
    curs.close()
    return pila_medicion


def cargar_desde_bd_comando():
    pila_comando = []
    db = MySQLdb.connect("localhost", "ignacio", "mantosamba", "SensorCampoElectroEstatico")
    curs = db.cursor()
    curs.execute("SELECT fecha, timestamp, comando, respuesta FROM comandlog")
    for (tdate, ttime, comand, respond) in curs:
        dato_comando = Dato_db_log(tdate, ttime, comand, respond)
        pila_comando.append(dato_comando)
    curs.close()
    return pila_comando

