intervals = []

class Interval:

    def __init__(self, hour_start, min_start, hour_end, min_end, sched, serial):
        self.hour_start = hour_start
        self.min_start = min_start
        self.hour_end = hour_end
        self.min_end = min_end
        self.sched = sched
        self.id = id(self)
        self.serial = serial
        intervals.append(self)

    def activate_interval(self):
        self.job_1_id = self.sched.add_job(self.serial.triggerStart, 'cron', hour=self.hour_start, minute=self.min_start)
        self.job_2_id = self.sched.add_job(self.serial.triggerEnd, 'cron', hour=self.hour_end, minute=self.min_end)

    def deactivate_interval(self):
        self.job_1_id.remove()
        self.job_2_id.remove()

    def remove_interval(self):
        self.deactivate_interval()
        intervals.remove(self)


def get_interval_by_id(id):
    for interval in intervals:
        if interval.id == int(id):
            return interval
    return None





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
