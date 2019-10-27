class Temperature:
    def __init__(self):
        self._celsius = 0.0
        self._fahrenheit = 32.0

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value
        self._fahrenheit = value * 1.8 + 32.0

    # --or--
    # celsius = property(fget=get_celsius,
    #                    fset=set_celsius)

    # --or--
    # celsius = property(get_celsius)
    # celsius.setter(set_celsius)

    @property
    def fahrenheit(self):
        return self._fahrenheit

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._fahrenheit = value
        self._celsius = (value - 32.0) / 1.8


if __name__ == '__main__':
    t = Temperature()
    t.celsius = 20
    print(t.fahrenheit)
