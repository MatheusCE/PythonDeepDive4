class TransactionID:

    def __init__(self, start_id):
        self._start_id = start_id

    def next(self):
        self._start_id += 1
        return self._start_id
    