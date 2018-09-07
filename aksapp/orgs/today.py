import datetime

days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

class Today():
         
        def __init__(self):
            self._now  = datetime.datetime.now()
            self.date = self._now.strftime("%Y-%m-%d")
            self.day = days[self._now.weekday()]
            self.position = int(self._now.day/7) + 1

