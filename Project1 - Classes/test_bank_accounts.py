from unittest import TestCase

from .bank_accounts import Account
from .time_zone import TimeZone


class TestTimeZone(TestCase):

    def setUp(self) -> None:
        self.t1 = TimeZone(name='ABC', offset_hours=-2, offset_minutes=-7)


class TestAccounts(TestCase):

    def setUp(self):
        self.a1 = Account()
