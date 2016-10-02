from Barramento import Barramento
from Memoria import RAM
from Cpu import CPU
from EntradaSaida import Entrada


class Computador:

    def __init__(self):
        self.barramento = Barramento()
        self.ram = RAM(self.barramento)
        self.entrada = Entrada(self.barramento)
        self.cpu = CPU(self.barramento)

        self.barramento.memoria = self.ram
        self.barramento.entrada = self.entrada
        self.barramento.cpu = self.cpu
