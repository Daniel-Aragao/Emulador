from Barramento.Barramento import Barramento
from Memoria.RAM import Ram
from Cpu.CPU import CPU
from EntradaSaida.Entrada import Entrada


class Computador:

    def __init__(self):
        self.barramento = Barramento()
        self.ram = Ram(self.barramento)
        self.entrada = Entrada(self.barramento)
        self.cpu = CPU(self.barramento)

#               0         1             2
        comp = [self.ram, self.entrada, self.cpu]
        self.barramento.components = comp

        self.entrada.preencher_memoria()

        self.cpu.executar_codigo()


if __name__ == '__main__':
    Computador()
