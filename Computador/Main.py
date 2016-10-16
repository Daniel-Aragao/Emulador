from Barramento.Barramento import Barramento
from Memoria.RAM import Ram
from Cpu.CPU import CPU
from EntradaSaida.Entrada import Entrada
from Utils.interface import Interface
from Computador import Componentes as Comps


class Computador:
    # implementar 3 barramentos, memoria dinamica, clock, largura de memoria

    def __init__(self):
        self.iniciar_constantes()

        self.criar_componentes()

        # Interface principal
        self.criar_interface_principal()

        # Iniciando programa
        self.executar_assembly()

    def iniciar_constantes(self):
        pass

    def executar_assembly(self):
        Comps.Entrada.preencher_memoria(Comps.Entrada.read_file())
        self.update_interface()

    def criar_interface_principal(self):
        interface = Interface()
        interface.start()
        Comps.interface_listas = [interface.list1, interface.list2, interface.list3, interface.textoCentro]
        interface.list2.focus_set()
        interface.btnNext.configure(command=self.avancar_codigo)
        interface.btnFinish.configure(command=self.concluir_codigo)

    def criar_componentes(self):
        Comps.Ram = Ram()
        Comps.Entrada = Entrada()
        Comps.Cpu = CPU()
        Comps.Componentes[Comps.RAM] = Comps.Ram
        Comps.Componentes[Comps.ENTRADA] = Comps.Entrada
        Comps.Componentes[Comps.CPU] = Comps.Cpu

    def avancar_codigo(self):
        Comps.Cpu.executar_codigo()
        self.update_interface()

    def concluir_codigo(self):
        while Comps.Cpu.running:
            self.avancar_codigo()

    @staticmethod
    def update_interface():
        Comps.interface_listas[0].set(Comps.Componentes[0])

        size = Comps.interface_listas[1].size()
        if size == 0:
            dados = Comps.Componentes[1].get_code()
            if dados is not None:
                for i in range(len(dados)):
                    Comps.interface_listas[1].insert('end', str(i) + ". " + str(dados[i].parametros))

        dados = Comps.Componentes[2].registradores
        if dados is not None:
            Comps.interface_listas[2].delete(0, 'end')
            for i in dados:
                Comps.interface_listas[2].insert('end', i + ": " + str(dados[i]))

        Comps.interface_listas[1].see(Comps.Componentes[2].interface_selected)
        Comps.interface_listas[1].activate(Comps.Componentes[2].interface_selected)

        if Comps.Componentes[2].running:
            Comps.interface_listas[3].set("Executando")
        else:
            Comps.interface_listas[3].set("Finalizado")


if __name__ == '__main__':
    Computador()
