__author__ = 'Gaston'
import os
from time import localtime, strftime

LOG_PATH = os.path.join(os.getcwd(), 'logger.txt')

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
