__author__ = 'Gaston'

import time
import webbrowser
import socket
import logging
import io


# Function to get a free port
def get_free_port():
	"""
	:return: the value of free port
	"""
	s = socket.socket()
	s.bind(('', 0))
	port = s.getsockname()[1]
	s.close()
	return port


# Function to open a browser
def open_browser(port):
	"""
	:param port: the port to open localhost on.
	:return:
	"""
	time.sleep(1)  # Wait for server to open
	webbrowser.open('http://localhost:%s' % port)


# Function to create and configure the logger
def create_logger():
	logger = logging.getLogger('logger')
	logger.setLevel(logging.DEBUG)
	log_string = io.BytesIO()
	log_handler = logging.StreamHandler(log_string)
	log_handler.setLevel(logging.INFO)
	log_handler.setLevel(logging.DEBUG)
	log_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', "%H:%M:%S"))
	logger.addHandler(log_handler)
	return logger
