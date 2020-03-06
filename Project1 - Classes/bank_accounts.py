import itertools
from .time_zone import TimeZone

class Account:
    transaction_counter = itertools.count(100)

    def __init__(self, account_number, first_name, last_name, timezone=None, initial_balance=0):
        self._account_number = account_number
        self.validate_and_set_name('_first_name', first_name, 'First Name')
        self.validate_and_set_name('_last_name', last_name, 'First Name')

        if timezone is None:
            timezone = TimeZone('UTC', 0, 0)
        self.timezone = timezone

        self._balance = float(initial_balance)

    @property
    def account_number(self):
        return self._account_number

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self.validate_and_set_name('_first_name', value, 'First Name')

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self.validate_and_set_name('_last_name', value, 'Last Name')

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def balance(self):
        return self._balance

    @property
    def timezone(self):
        return self._timezone

    @timezone.setter
    def timezone(self, value):
        if not isinstance(value, TimeZone):
            raise ValueError("The value must be an instance of TimeZone")
        self._timezone = value

    def validate_and_set_name(self, attr_name, value, field):
        if len(str(value).strip()) == 0:
            raise ValueError(f'{field} can not be empty.')
        setattr(self, attr_name, str(value).strip())
    