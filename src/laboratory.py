class Laboratory:
    def __init__(self, substances, reactions=None):
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
        self._reactions = reactions if reactions is not None else {}

        for product in self._reactions:
            self._stocks[product] = 0.0

        for product, ingredients in self._reactions.items():
            for substance, qty in ingredients:
                if substance not in self._stocks:
                    raise ValueError(f"Unknown substance: {substance} in reaction for {product}")

    def get_quantity(self, substance):
      if substance not in self._stocks:
          raise ValueError(f"Unknown substance: {substance}")
      return self._stocks[substance]

    def add(self, name, quantity):
        if name not in self._stocks:
            raise ValueError(f"Unknown substance: {name}")
        if not isinstance(quantity, (int, float)):
            raise TypeError("Quantity must be a number")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self._stocks[name] += quantity