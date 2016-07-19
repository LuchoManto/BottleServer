__author__ = 'Ignacio'

import MySQLdb

pila_medicion = []

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

def cargar_desde_bd():
    db = MySQLdb.connect("localhost", "tesis", "1234", "rayito")
    curs = db.cursor()
    curs.execute("SELECT tdate, pin, electrostatic FROM medicion")
    for (tdate, pin, electrostatic) in curs:
        pila_medicion.append(tdate)
	pila_medicion.append(pin)
	pila_medicion.append(electrostatic)
    return pila_medicion
