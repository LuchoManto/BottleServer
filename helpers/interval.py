class Interval:

    def __init__(self, hour_start, min_start, hour_end, min_end, sched):
        self.hour_start = hour_start
        self.min_start = min_start
        self.hour_end = hour_end
        self.min_end = min_end
        self.sched = sched
        self.id = id(self)

    def activate_interval(self):
        self.job_1_id = self.sched.add_job(serial_obj.triggerStart, 'cron', hour=hour_start, minute=min_start)
        self.job_2_id = self.sched.add_job(serial_obj.triggerEnd, 'cron', hour=hour_end, minute=min_end)

    def deactivate_interval(self):
        self.job_1_id.remove()
        self.job_2_id.remove()


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