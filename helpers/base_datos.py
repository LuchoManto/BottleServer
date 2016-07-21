__author__ = 'Ignacio'

import MySQLdb

from helpers.dato_db import *

pila_medicion = []
pila_comando = []

def cargar_comand_log(valor,respuesta):
    db = MySQLdb.connect("localhost", "tesis", "1234", "rayito")
    curs = db.cursor()
    curs.execute("""INSERT INTO comandlog
        values(CURRENT_DATE(), NOW(),%s, %s)""", (valor, respuesta,))
    db.commit()
    db.close()

def cargar_medicion(timestamp, pin, valor):
    db = MySQLdb.connect("localhost", "tesis", "1234", "rayito")
    curs = db.cursor()
    curs.execute("""INSERT INTO medicion
            values(%s, %s,%s)""", (timestamp, pin, valor,))
    db.commit()
    db.close()

def cargar_desde_bd_medicion():
    db = MySQLdb.connect("localhost", "tesis", "1234", "rayito")
    curs = db.cursor()
    curs.excecute("SELECT tdate, pin, electrostatic FROM medicion")
    for (tdate, pin, electrostatic) in curs:
        dato_medicion = Dato_db(tdate, pin, electrostatic)
    curs.close()
    return dato_medicion

def cargar_desde_bd_comando():
    db = MySQLdb.connect("localhost", "tesis", "1234", "rayito")
    curs = db.cursor()
    curs.excecute("SELECT dtime, ttime, comand, respond, electrostatic FROM comandlog")
    for (dtime, ttime, comand, respond) in curs:
        dato_comando = Dato_db(dtime, ttime, comand, respond)
    curs.close()
    return dato_comando
