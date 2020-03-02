from unittest import TestCase

from bank_accounts import TimeZone, Account


class TestTimeZone(TestCase):

    def setUp(self) -> None:
        self.t1 = TimeZone()


class TestAccounts(TestCase):

    def setUp(self):
        self.a1 = Account()
