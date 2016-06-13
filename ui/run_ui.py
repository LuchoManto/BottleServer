__author__ = 'Gaston'


import threading
import time

 #import MySQLdb

import bottle
from bottle import Bottle
from bottle import debug as bottle_debug, static_file, view, response, request

from helpers.connection import *
from helpers.start import *
from helpers.serial_uart import *
from helpers.base_datos import*


from datetime import date

bottle.TEMPLATE_PATH.insert(0, os.path.join(os.getcwd(), 'ui/views'))

app = Bottle()
logger = create_logger()

#create serial object
serial_obj = ClaseSerial()

# Function to run the UI. host='localhost'
def run_ui(debug=False, host='0.0.0.0', port=50505, browser=True):
    """
    :param debug:  to run bottle in mode debug, default False.
    :param host: where to run the app, default localhost.
    :param port: port of the app, default None.
    :param browser: open browser when run, default True.
    :return:
    """

    #start the scheduler
    serial_obj.startSched()

    # If not specified search for a free port.
    if not port:
        port = get_free_port()
    # Open browser.
    if browser:
        th = threading.Thread()
        th.run = lambda: open_browser(port)
        th.start()
    bottle_debug(debug)
    app.run(host=host, port=port)

    return


# Route for the home.
@app.get('/')
@view('motor')
def home():
    return

# Post send by serial
@app.post('/send_serial/<value>')
def send_serial(value):
    """
    Post cuando se envia valor de string por serial.
    :param value: valor a enviar por serial
    """
    send = value
    resp = serial_obj.enviarYObtenerRespuesta(send)
    resp1 = resp[-5:]
    cargar_comand_log(send,resp1)
    if send == 'ST':
        #llamar a la funcion que va a llamar a los hilos.
        serial_obj.start_conversion_ST()
    #if send == 'GSE,0':
    #   time.sleep(1)
    #    med = serial_obj.recibir()
	#    med1 = med[5:]
    #    cargar_medicion('0',med1)


# Post to change uart state
@app.post('/uart_state/<value>')
def uart_state(value):
    """
    post para cambiar el estado de la uart del modulo
    :param value: valor a enviar en diccionario uartstate
    """
    send = value
    send = 'uartstate=' + str(send)
    send_esp_1(send, logger)
    return

# Route to get the dynamic log.
@app.get('/logger')
@view('logger')
def show_logger():
    return dict()


# Route to fill the log.
@app.get('/raw_log')
@app.get('/raw_log/<offset>')
def show_raw_log(offset='0'):
    return logger.handlers[0].stream.getvalue()[int(offset):]


# Route to search the images in the write folder.
@app.route('/images/<filename>')
def serve_images(filename):
    return static_file(filename, root='ui/images')


# Route to search for the css files.
@app.route('/css/<filename>')
def serve_css_static(filename):
    return static_file(filename, root='ui/css')

# Route to search for the css externs files.
@app.route('/css/externs/<filename>')
def serve_css_static(filename):
    return static_file(filename, root='ui/css/externs')

# Post send by serial
@app.post('/set_interval')
def handler():
    start = request.params.dict['start'][0]
    end = request.params.dict['end'][0]
    hour_start = int(start.split(":")[0])
    min_start = int(start.split(":")[1])
    hour_end = int(end.split(":")[0])
    min_end = int(end.split(":")[1])
    serial_obj.sched.add_job(serial_obj.triggerStart, 'cron', hour=hour_start, minute=min_start)
    serial_obj.sched.add_job(serial_obj.triggerEnd, 'cron', hour=hour_end, minute=min_end)

# def triggerStart():
# 		send = "SSE,0,1"
# 		parameter = {'tosend': send}
# 		send_esp_1(parameter, logger)

# 		send = "SGA,3"
# 		parameter = {'tosend': send}
# 		send_esp_1(parameter, logger)

# 	send = "PWM"
# 	parameter = {'tosend': send}
# 	send_esp_1(parameter, logger)

# 	sched.add_job(keepAlive, 'cron', second=8)

# def triggerEnd():
# 	send = "NTP"
# 	parameter = {'tosend': send}
# 	send_esp_1(parameter, logger)
