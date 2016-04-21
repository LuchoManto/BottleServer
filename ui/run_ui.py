

__author__ = 'Gaston'

from apscheduler.schedulers.background import BackgroundScheduler

import threading
import serial
import thread

import bottle
from bottle import Bottle
from bottle import debug as bottle_debug, static_file, view, response, request

from helpers.connection import *
from helpers.start import *

from datetime import date


bottle.TEMPLATE_PATH.insert(0, os.path.join(os.getcwd(), 'ui/views'))


app = Bottle()
logger = create_logger()
sched = BackgroundScheduler()
port = serial.Serial(port = '/dev/ttyAMA0',
                     baudrate=9600,
                     parity=serial.PARITY_NONE,
                     stopbits=serial.STOPBITS_ONE,
                     bytesize=serial.EIGHTBITS,
                     timeout=3)


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
    sched.start()

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

def triggerStart():
    send = "SSE,0,1"
    parameter = {'tosend': send}
    send_esp_1(parameter, logger)
    send = "SGA,3"
    parameter = {'tosend': send}
    send_esp_1(parameter, logger)
    send = "PWM"
    parameter = {'tosend': send}
    send_esp_1(parameter, logger)



    # thread1 = thread.start_new_thread(keepAlive)
    # sched.add_job(keepAlive, 'cron', second=8)


def triggerEnd():
    send = "NTP"
    parameter = {'tosend': send}
    send_esp_1(parameter, logger)



# Route for the home.
@app.get('/')
@view('home')
def home():
    return


# Route for the module controller.
@app.get('/module')
@view('module')
def module():
    return


# Route for the electrostatic field sensor.
@app.get('/motor')
@view('motor')
def module():
    return


# Route for the GPS controller.
@app.get('/gps')
@view('gps')
def module():
    return


# Post GPS_BUTTON PRESSED
@app.get('/button_press/<button_pressed>')
def button_pressed(button_pressed):
    """
    Post cuando se preciona un boton del GPS
    :param button_pressed: nombre del boton precionado.
    """
    response.content_type = 'application/json'

    send = get_hex_button(button_pressed)
    send = send.replace('x', '').replace(' ', '')
    parameter = {'hextosend': send}
    send_esp_1(parameter, logger, hex=True)

    return gps_screen()


# Post send hex values
@app.post('/send_hex/<value>')
def send_hex(value):
    """
    Post cuando envio un valor hex
    :param value: valor hex a enviar las x y ' ' se quitaran.
    """
    send = value.replace('x', '').replace(' ', '')
    parameter = {'hextosend': send}
    send_esp_1(parameter, logger, hex=True)
    return

# Post send by serial
@app.post('/send_serial/<value>')
def send_serial(value):
    """
    Post cuando se envia valor de string por serial.
    :param value: valor a enviar por serial
    """
    send = value
    # parameter = {'tosend': send}
    # send_esp_1(parameter, logger)
    enviarYObtenerRespuesta(send)
    return


# Post to change uart state
@app.post('/uart_state/<value>')
def uart_state(value):
    """
    post para cambiar el estado de la uart del modulo
    :param value: valor a enviar en diccionario uartstate
    """
    send = value
    parameter = {'uartstate': send}
    send_esp_1(parameter, logger)
    return


# Ruta para obtener un json con los renglones del gps
@app.get('/gpslines')
def get_gps_lines():
    response.content_type = 'application/json'
    renglones = gps_screen()
    return renglones


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

    sched.add_job(triggerStart, 'cron', hour=hour_start, minute=min_start)
    sched.add_job(triggerEnd, 'cron', hour=hour_end, minute=min_end)
    return


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

def keepAlive():

	send = "p"
	parameter = {'tosend': send}
	send_esp_1(parameter, logger)

def enviarYObtenerRespuesta(toSend):
    port.write(toSend)
    recv = port.readline()
    return recv
