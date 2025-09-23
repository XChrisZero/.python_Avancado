class Carro: # Carro tem um Motor e um Fabricante
    def __init__(self, nome): # método construtor
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property # getter
    def motor(self):
        return self._motor

    @motor.setter # setter
    def motor(self, valor):
        self._motor = valor

    @property # getter
    def fabricante(self):
        return self._fabricante

    @fabricante.setter # setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor: # Motor pode ser de vários carros
    def __init__(self, nome):
        self.nome = nome


class Fabricante: # Fabricante pode fabricar vários carros
    def __init__(self, nome):
        self.nome = nome
