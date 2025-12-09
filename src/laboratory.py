class Laboratory:
    def __init__(self, substances):
        if substances is None:
            raise TypeError("Substances list cannot be None")
        self._stocks = {s: 0.0 for s in substances}

    def get_quantity(self, substance):
      if substance not in self._stocks:
          raise ValueError(f"Unknown substance: {substance}")
      return self._stocks[substance]