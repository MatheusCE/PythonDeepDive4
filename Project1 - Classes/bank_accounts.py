from .time_zone import TimeZone

class Account:

    # time_zone_offset = timezone()
    
    def __init__(self, account_number, first_name, last_name):
        self._account_number = account_number
        self.first_name = first_name
        self.last_name = last_name

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, value):
        # if 
        pass
