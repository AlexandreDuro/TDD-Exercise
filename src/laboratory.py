class Laboratory:
    def __init__(self, substances):
        self._stocks = {s: 0.0 for s in substances}

    def get_quantity(self, substance):
        return self._stocks[substance]