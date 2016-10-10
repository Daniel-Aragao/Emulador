from Barramento.Barramento import Barramento
from Memoria.RAM import Ram
from Cpu.CPU import CPU
from EntradaSaida.Entrada import Entrada
from Utils.interface import Interface


class Computador:

    def __init__(self):
        self.barramento = Barramento()
        self.ram = Ram(self.barramento)
        self.entrada = Entrada(self.barramento)
        self.cpu = CPU(self.barramento)

#               0         1             2
        comp = [self.ram, self.entrada, self.cpu]
        self.barramento.components = comp

        interface = Interface()
        interface.start()

        interface_listas = [interface.list1, interface.list2, interface.list3, interface.textoCentro]
        self.barramento.listas = interface_listas

        interface.list2.focus_set()

        self.entrada.preencher_memoria()

        interface.btn.configure(command=self.cpu.executar_codigo)


if __name__ == '__main__':
    Computador()
