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
    curs.execute("SELECT hora, pin, medicion FROM medicion")
    for (hora, pin, medicion) in curs:
        dato_medicion = Dato_db(hora, pin, medicion)
        pila_medicion.append(dato_medicion)
    curs.close()
    return pila_medicion


def cargar_desde_bd_comando():
    pila_comando = []
    db = MySQLdb.connect("localhost", "ignacio", "mantosamba", "SensorCampoElectroEstatico")
    curs = db.cursor()
    curs.execute("SELECT fecha, hora, comando, respuesta FROM comandlog")
    for (fecha, hora, comando, respuesta) in curs:
        dato_comando = Dato_db_log(fecha, hora, comando, respuesta)
        pila_comando.append(dato_comando)
    curs.close()
    return pila_comando

