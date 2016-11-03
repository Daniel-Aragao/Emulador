from Computador import Componentes as Comps
from Computador import Constantes as Consts
from Cpu.CPU import CPU
from EntradaSaida.Entrada import Entrada
from Interfaces.interface import Interface
from Memoria.RAM import Ram
from Barramento.Barramento import Barramento
from Interfaces.Configurations import BarramentoConfig
from Interfaces.Configurations import MemoriaConfig


class Computador:
    # 07/11 entrega da alteracao do barramento
    # implementar 3 barramentos, memoria maior, clock e largura do barramento
    # largura de banda eh clock * largura do barramento
    # exemplo: (clock = 100hz) * (largura = 8bits)  = 800 bits/s
    #largura vai de 8 a 128, potencia de base 2
    #ram vai de 32 a 32*2^30, potencia de base 2
    #clock vai de 100hz a 1ghz, multiplo de 100
    #corrigir constantes que deveriam ser funcoes
    # tamanho maximo da memoria fisica eh de 2**24

    def __init__(self):
        # interface
        self.iniciar_interfaces_configuracao()

        # Instanciando componentes do computador
        self.criar_componentes()
        """
        # interface
        self.criar_interface_principal()

        # Iniciando programa
        self.executar_assembly()
        """

    @staticmethod
    def iniciar_interfaces_configuracao():
        BarramentoConfig()
        MemoriaConfig()

    @staticmethod
    def criar_componentes():
        barramento = Barramento()

        Comps.Ram = Ram(barramento)
        Comps.Entrada = Entrada(barramento)
        Comps.Cpu = CPU(barramento)

        Comps.Ram.start()
        Comps.Entrada.start()
        Comps.Cpu.start()

        Comps.Componentes[Comps.RAM] = Comps.Ram
        Comps.Componentes[Comps.ENTRADA] = Comps.Entrada
        Comps.Componentes[Comps.CPU] = Comps.Cpu

    """
    def executar_assembly(self):
        Comps.Entrada.preencher_memoria(Comps.Entrada.read_file())
        # famosa gambiarra
        Comps.Ram.pointer = 0
        self.update_interface()

    def criar_interface_principal(self):
        interface = Interface()
        interface.start()

        Comps.interface_listas = [interface.list1, interface.list2, interface.list3, interface.textoCentro]
        interface.list2.focus_set()

        interface.btnNext.configure(command=self.avancar_codigo)
        interface.btnFinish.configure(command=self.concluir_codigo)

    def avancar_codigo(self):
        Comps.Cpu.executar_codigo()
        self.update_interface()

    def concluir_codigo(self):
        while Comps.Cpu.running:
            self.avancar_codigo()

    @staticmethod
    def update_interface():
        Comps.interface_listas[0].set(Comps.Componentes[Comps.RAM])

        size = Comps.interface_listas[1].size()
        if size == 0:
            dados = Comps.Componentes[Comps.ENTRADA].get_code()
            if dados is not None:
                for i in range(len(dados)):
                    Comps.interface_listas[1].insert('end', str(i) + ". " + str(dados[i].parametros))

        dados = Comps.Componentes[Comps.CPU].registradores
        if dados is not None:
            Comps.interface_listas[2].delete(0, 'end')
            for i in dados:
                Comps.interface_listas[2].insert('end', i + ": " + str(dados[i]))

        Comps.interface_listas[1].see(Comps.Componentes[Comps.CPU].interface_selected)
        Comps.interface_listas[1].activate(Comps.Componentes[Comps.CPU].interface_selected)

        if Comps.Componentes[Comps.CPU].running:
            Comps.interface_listas[3].set("Executando")
        else:
            Comps.interface_listas[3].set("Finalizado")
"""

if __name__ == '__main__':
    Computador()
