__author__ = 'Gaston'

import json
import bottle
from bottle import Bottle, template, response
from bottle import debug as bottle_debug, static_file, view, request

from helpers.connection import *
from helpers.start import *
from helpers.interval import *
from helpers.serial_uart import *
from helpers.base_datos import *
from apscheduler.schedulers.background import BackgroundScheduler


from datetime import date

bottle.TEMPLATE_PATH.insert(0, os.path.join(os.getcwd(), 'ui/views'))

app = Bottle()
logger = create_logger()

#create serial object
serial_obj = ClaseSerial()


#start the scheduler
sched = BackgroundScheduler()

# Function to run the UI. host='localhost'
def run_ui(debug=False, host='0.0.0.0', port=50505, browser=True):
    """
    :param debug:  to run bottle in mode debug, default False.
    :param host: where to run the app, default localhost.
    :param port: port of the app, default None.
    :param browser: open browser when run, default True.
    :return:
    """
    #start running the scheduler
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
    # operacion,pin,vel = send.split(",")
    resp = serial_obj.enviarYObtenerRespuesta(send)
    resp1 = resp[-5:]
    cargar_comand_log(send,resp1)
    if send == 'ST':
        #llamar a la funcion que va a llamar a los hilos.
        serial_obj.start_conversion_ST()
    elif send == 's':
	    serial_obj.kill_threads()
    # if send == 'GSE,0':
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
def set_interval():
    start = request.params.dict['start'][0]
    end = request.params.dict['end'][0]
    hour_start = int(start.split(":")[0])
    min_start = int(start.split(":")[1])
    hour_end = int(end.split(":")[0])
    min_end = int(end.split(":")[1])
    # interv = Interval(hour_start, min_start, hour_end, min_end, sched, serial_obj)
    # interv.activate_interval()
    return

@app.post('/remove_interval/<value>')
def remove_interval(value):
    id_regla = value
    interv = get_interval_by_id(id_regla)
    if interv is not None:
        interv.remove_interval()
    return

@app.get('/graphic.html')
def graphic():
    cargar_desde_bd_medicion()
    cargar_desde_bd_comando()
    return template('graphic.tpl')

@app.get('/all.html')
def graphic():
    cargar_desde_bd_medicion()
    cargar_desde_bd_comando()
    return template('all.tpl')

@app.get('/data')
def graphic():
    cargar_desde_bd_medicion()
    cargar_desde_bd_comando()
    pila_medicion = get_pila_medicion()
    pila_comando = get_pila_comando()

    response.content_type = 'application/json'
    return json.dumps({'pila_medicion': pila_medicion, 'pila_comando': pila_comando})


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
