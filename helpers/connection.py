__author__ = 'Gaston'

import time

from restapiclient import *
from config import *

# Timeout used to make the requests to NODEMCU.
send_time_out = 3
# ip and port of node.
ip_node = '192.168.1.248'
port_node = '80'


# Function to prepare a post to send with parameters.
# Cuando se desea enviar y recibir valores hex poner en true
def send_esp_1(parameter, logger, hex=False):
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

# Function to ask for the gps screen
# retorna un diccionario con los 4 renglones.
def gps_screen():
	send = get_hex_button('SCR')
	send = send.replace('x', '').replace(' ', '')
	parameter = {'hextosend': send}
	response = send_esp_2(parameter, hex)
	renglones = {
		'renglon1': response[8:8+80].decode("hex"),
		'renglon2': response[8+80:8+80*2].decode("hex"),
		'renglon3': response[8+80*2:8+80*3].decode("hex"),
		'renglon4': response[8+80*3:8+80*4].decode("hex")
	}
	return renglones


# Function to ask for the gps screen
# retorna un diccionario con los 4 renglones.
def gps_screen_mock():
	renglones = {
		'renglon1': 'CH1-4  SV30  SV25  SV02  SV23 |MORE CHAN',
		'renglon2': 'ELEV    --    --    --    --  |      URA',
		'renglon3': 'SNR     --    --    --    --  |         ',
		'renglon4': 'AZMTH   --    --    --    --  |         '
	}
	return renglones
