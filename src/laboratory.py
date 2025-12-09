class Laboratory:
    def __init__(self, substances):
        if substances is None:
            raise TypeError("Substances list cannot be None")
        for s in substances:
            if not isinstance(s, str):
                raise TypeError("All substances must be strings")
            if not s.strip():
                raise ValueError("Substance name cannot be empty or whitespace")
        if len(set(substances)) != len(substances):
            raise ValueError("Substances list cannot contain duplicates")
        self._stocks = {s: 0.0 for s in substances}

    def get_quantity(self, substance):
      if substance not in self._stocks:
          raise ValueError(f"Unknown substance: {substance}")
      return self._stocks[substance]