from helpers.connection import send_esp_1

def triggerStart(logger):
    send = "PWM"
    parameter = {'tosend': send}
    send_esp_1(parameter, logger)


def triggerEnd(logger):
    send = "NTP"
    parameter = {'tosend': send}
    send_esp_1(parameter, logger)