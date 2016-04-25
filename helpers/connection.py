__author__ = 'Gaston'

import time
import paho.mqtt.client as mqtt
import threading
from restapiclient import *
from config import *

# Timeout used to make the requests to NODEMCU.
send_time_out = 3
# ip and port of node.
ip_node = '192.168.1.248'
port_node = '80'


# Function to prepare a post to send with parameters.
# Cuando se desea enviar y recibir valores hex poner en true
def send_esp_1(send, logger):
    """
    :param parameter: parametro enviado en el post al modulo es un diccionario {'key':'value'}
    :param logger: logger para mostrar el envio y la respuesta
    :param hex: si se desea enviar y recibir valor hex poner True
    :return: retorna la respuesta del modulo.
    """
    logger.info('Sending: ' + str(send))

    log_send(str(send))
    try:
        mqtt_publish(send)

    except Exception as exc:
        logger.info('Error publicando al broker: ' + str(exc))
        log_response('Error publicando al broker: ' + str(exc))
        return ''
        pass
    return

# Function to prepare a post to send with parameters.
# Cuando se desea enviar y recibir valores hex poner en true
def send_esp_1_old(parameter, logger, hex=False):
    """
    :param parameter: parametro enviado en el post al modulo es un diccionario {'key':'value'}
    :param logger: logger para mostrar el envio y la respuesta
    :param hex: si se desea enviar y recibir valor hex poner True
    :return: retorna la respuesta del modulo.
    """
    logger.info('Sending: ' + str(parameter))

    log_send(str(parameter))
    try:
        response = send_esp_2(parameter, hex)

        if not hex:
            # Split, como el modulo me devuelve lo que el fue enviando por UART
            # quiero solo la respuesta que obtuvo por la UART. Lo tenia post tosend.
            # Ver que los otros post como uart_state no tenia este split y no tiene len.
            # TODO: ver comportamiento de uart_state con split
            response = response.split('\n')
            logger.info('Response: ' + str(response[len(response) - 1]))

            log_response(str(response[len(response) - 1]))
            return str(response[len(response) - 1])
        else:
            logger.info('Response: ' + response)
            log_response(response)
            return response

    except Exception as exc:
        logger.info('Response as exc: ' + str(exc))

        log_response('Exception: ' + str(exc))
        return ''
        pass
    return


# Function that send a POST to NODEMCU with some parameters
def send_esp_2(parameter, hex=False):
    """
    :param parameter: parametro enviando en el post, debe ser un diccionario {'key':'valor'}
    :param hex: si se va a enviar y recibir valor hex poner True
    :return: valor de respuesta del modulo
    """
    # Try to Send the post to the wifi module
    try:
        client = RestAPIClient(ip_node, port_node)
        response = client.do_get(params=parameter, timeout=send_time_out)

        parameter = {'getresponse': 'esperando_respuesta'}
        time.sleep(1)
        response = client.do_get(params=parameter, timeout=send_time_out)

        if not hex:
            return response.text
        else:
            # Tener en cuenta que antes del join podemos poner cualquier caracter para separar los byte (2 hex)
            return "".join("{:02x}".format(ord(c)) for c in response.text)

    except Exception as exc:
        print str(exc)
        raise exc
    return


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
    print 'Connected to broker with result code ' + str(rc)
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe('/motoresp/data')


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print 'Topic: ', msg.topic + '\nMessage: ' + str(msg.payload)


def crear_mqtt_client():
    global MQTT_CLIENT
    MQTT_CLIENT = mqtt.Client()
    MQTT_CLIENT.on_connect = on_connect
    MQTT_CLIENT.on_message = on_message
    MQTT_CLIENT.connect('test.mosquitto.org', 1883, 60)
    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    th = threading.Thread()
    th.run = lambda: MQTT_CLIENT.loop_forever()
    th.daemon = True
    th.start()


def mqtt_publish(msj):
    global MQTT_CLIENT
    # MQTT_CLIENT.publish('/espgaston/data', 'uartstate=disconnected')
    # msj= 'tosend=' + data['data']
    # msj= 'uartstate=disconnected'
    # msj= 'uartstate=connected'
    MQTT_CLIENT.publish('/motoresp/data', msj)
