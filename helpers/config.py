__author__ = 'Gaston'
import os
from time import localtime, strftime


LOG_PATH = os.path.join(os.getcwd(), 'logger.txt')


# Value of buttons
buttons = {
	'LEFT': 'x02x00x81x01x1Dx9Fx03',
	'RIGHT': 'x02x00x81x01x1Cx9Ex03',
	'NUM1': 'x02x00x81x01x31xB3x03',
	'NUM2': 'x02x00x81x01x32xB4x03',
	'NUM3': 'x02x00x81x01x33xB5x03',
	'NUM4': 'x02x00x81x01x34xB6x03',
	'NUM5': 'x02x00x81x01x35xB7x03',
	'NUM6': 'x02x00x81x01x36xB8x03',
	'NUM7': 'x02x00x81x01x37xB9x03',
	'NUM8': 'x02x00x81x01x38xBAx03',
	'NUM9': 'x02x00x81x01x39xBBx03',
	'NUM0': 'x02x00x81x01x30xB2x03',
	'ENTER': 'x02x00x81x01x0Dx8Fx03',
	'CLEAR': 'x02x00x81x01x7Fx01x03',
	'ALPHA': 'x02x00x81x01x50xD2x03',
	'STATUS': 'x02x00x81x01x4CxCEx03',
	'SATINFO': 'x02x00x81x01x4BxCDx03',
	'SESSIONS': 'x02x00x81x01x4AxCCx03',
	'CONTROL': 'x02x00x81x01x4DxCFx03',
	'LOGDATA': 'x02x00x81x01x4FxD1x03',
	'MODIFY': 'x02x00x81x01x4ExD0x03',
	'OP1': 'x02x00x81x01x41xC3x03',
	'OP2': 'x02x00x81x01x42xC4x03',
	'OP3': 'x02x00x81x01x43xC5x03',
	'OP4': 'x02x00x81x01x44xC6x03',
	'POWER': 'x02x00x81x01x1Bx9Dx03',
	'SCR': 'x02x00x82x00x82x03'
}


# Function to return the hex code of a button from the dictionary.
def get_hex_button(button):
	"""
	:param button:name of the button.
	:return: hexcode of the desire button.
	"""
	return buttons[button]


# Save response into the log, using LOG_PATH
def log_response(response):
	"""
	:param response: response to save into the log
	:return:
	"""
	with open(LOG_PATH, 'a') as f:
		f.write(strftime("%Y-%m-%d %H:%M:%S", localtime()) + ' Response - ' + response + '\n')


# Save the sending to the log, using LOG_PATH
def log_send(send):
	"""
	:param send: valor enviado al modulo para guardar en el log
	:return:
	"""
	with open(LOG_PATH, 'a') as f:
		f.write(strftime("%Y-%m-%d %H:%M:%S", localtime()) + ' Send     - ' + send + '\n')


# Function used to print al the keys of and object
def pprint(obj):
	for attr in dir(obj):
		print "obj.%s = %s" % (attr, getattr(obj, attr))
