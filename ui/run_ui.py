__author__ = 'Gaston'

from apscheduler.schedulers.background import BackgroundScheduler

import threading

import bottle
from bottle import Bottle
from bottle import debug as bottle_debug, static_file, view, response, request

from helpers.connection import *
from helpers.start import *
from helpers.motor import triggerEnd, triggerStart

bottle.TEMPLATE_PATH.insert(0, os.path.join(os.getcwd(), 'ui/views'))

app = Bottle()
logger = create_logger()
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

    #start the scheduler
    sched.start()
    #Creo mqtt client.
    crear_mqtt_client()

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
    parameter = {'tosend': send}
    send_esp_1(parameter, logger)
    return

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

    sched.add_job(lambda: triggerStart(logger), 'cron', hour=hour_start, minute=min_start)
    sched.add_job(lambda: triggerEnd(logger), 'cron', hour=hour_end, minute=min_end)
    return