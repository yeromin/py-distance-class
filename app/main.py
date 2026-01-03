class Distance:
    def __init__(self, km):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        other_km = self._get_number_or_distance(other)
        if other_km is NotImplemented:
            return NotImplemented
        return Distance(self.km + other_km)

    def __iadd__(self, other):
        other_km = self._get_number_or_distance(other)
        if other_km is NotImplemented:
            return NotImplemented
        self.km += other_km
        return self

    def __mul__(self, other):
        if isinstance(other, Distance):
            raise TypeError("Distance can only be multiplied by a number")
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Distance(self.km * other)

    def __truediv__(self, other):
        if isinstance(other, Distance):
            raise TypeError("Distance can only be divided by a number")
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Distance(round(self.km / other, 2))

    def __eq__(self, other):
        other_km = self._get_number_or_distance(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km == other_km

    def __lt__(self, other):
        other_km = self._get_number_or_distance(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km < other_km

    def __le__(self, other):
        other_km = self._get_number_or_distance(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km <= other_km

    def __gt__(self, other):
        other_km = self._get_number_or_distance(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km > other_km

    def __ge__(self, other):
        other_km = self._get_number_or_distance(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km >= other_km

    @staticmethod
    def _get_number_or_distance(value):
        if isinstance(value, Distance):
            return value.km
        if isinstance(value, (int, float)):
            return value
        return NotImplemented