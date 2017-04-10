__author__ = 'Ignacio'

import MySQLdb

from helpers.dato_db import *
from helpers.dato_bd_log import *

pila_medicion = []
pila_comando = []
count_medicion = 0
row_numb_medicion = 0
count_log = 0
row_numb_log = 0


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
    global row_numb_medicion
    global count_medicion
    db = MySQLdb.connect("localhost", "ignacio", "mantosamba", "SensorCampoElectroEstatico")
    curs = db.cursor()
    first_row_numb_medicion = curs.execute("SELECT COUNT(*) FROM medicion")
    curs.execute("SELECT * FROM medicion LIMIT %s , 99999", int(count_medicion),)
    for (hora, pin, medicion) in curs:
        dato_medicion = Dato_db(hora, pin, medicion)
        pila_medicion.append(dato_medicion)
        count_medicion = count_medicion + 1
    row_numb_medicion = curs.execute("SELECT COUNT(*) FROM medicion")
    curs.close()
    return pila_medicion


def cargar_desde_bd_comando():
    global row_numb_log
    global count_log
    db = MySQLdb.connect("localhost", "ignacio", "mantosamba", "SensorCampoElectroEstatico")
    curs = db.cursor()
    curs.execute("SELECT * FROM comandlog LIMIT %s , 99999", int(count_log),)
    for (fecha, hora, comando, respuesta) in curs:
        dato_comando = Dato_db_log(fecha, hora, comando, respuesta)
        pila_comando.append(dato_comando)
        count_log = count_log + 1
    row_numb_log = curs.execute("SELECT COUNT(*) FROM comandlog")
    curs.close()
    return pila_comando
