
CRON_FIELDS = ["second", "minute", "hour", "day", "month", "weekday"]

class CronBuilder:
    def __init__(self, second="*", minute="*", hour="*", day="*", month="*", weekday="*"):
        self.second = second
        self.minute = minute
        self.hour = hour
        self.day = day
        self.month = month
        self.weekday = weekday

    def set_second(self, second):
        self.second = second
        return self

    def set_minute(self, minute):
        self.minute = minute
        return self

    def set_hour(self, hour):
        self.hour = hour
        return self

    def set_day(self, day):
        self.day = day
        return self

    def set_month(self, month):
        self.month = month
        return self

    def set_weekday(self, weekday):
        self.weekday = weekday
        return self

    #  helper methods for common cron intervals
    def every_second(self):
        self.second = "*"
        return self
    
    def every_minute(self):
        self.minute = "*"
        return self
    
    def every_hour(self):
        self.hour = "*"
        return self
    
    def every_day(self):
        self.day = "*"
        return self
    
    def every_week(self):
        self.weekday = "*"
        return self

    def every_month(self):
        self.month = "*"
        return self

    def every(self, field, value):
        """
        Set a cron field to 'every <value>' pattern.
        Example: every('minute', 5) -> "*/5 * * * *"
        """
        if field not in CRON_FIELDS:
            raise ValueError("Invalid field. Valid fields are: second, minute, hour, day, month, weekday.")
        setattr(self, field, f"*/{value}")
        return self

    def set_range(self, field, start, end):
        """
        Set a cron field to a specific range pattern.
        Example: set_range('hour', 9, 17) -> "9-17 * * * *"
        """
        if field not in CRON_FIELDS:
            raise ValueError("Invalid field. Valid fields are: second, minute, hour, day, month, weekday.")
        setattr(self, field, f"{start}-{end}")
        return self

    def set_specific(self, field, value):
        """
        Set a cron field to a specific value pattern.
        Example: set_specific('minute', 10) -> "10 * * * *"
        """
        if field not in CRON_FIELDS:
            raise ValueError("Invalid field. Valid fields are: second, minute, hour, day, month, weekday.")
        setattr(self, field, f"{value}")
        return self

    def build(self):
        return f"{self.second} {self.minute} {self.hour} {self.day} {self.month} {self.weekday}"

