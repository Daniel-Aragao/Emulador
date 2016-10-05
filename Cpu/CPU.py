from EntradaSaida.Codigo import Codigo
from Memoria import Constantes as consts


class CPU:
    def __init__(self, barramento):
        self.barramento = barramento
        self.registradores = {"A": 0, "B": 0, "C": 0, "D": 0, "CI": 0}

    def executar_codigo(self):
        regs = self.registradores
        running = True

        while running:
            cod, ci = self.barramento.receber_codigo(0, regs["CI"])
            if ci == -1:
                regs["CI"] = 0
                running = False
                break

            regs["CI"] = ci

            if Codigo.operacoes["inc"] == cod[0]:
                regs[unichr(-(cod[1]))] += 1

            elif Codigo.operacoes["add"] == cod[0]:
                valor_inicial = regs[unichr(-(cod[1]))]

                self.get_valor(cod[1])

                pass
            elif Codigo.operacoes["mov"] == cod[0]:
                pass
            elif Codigo.operacoes["imul"] == cod[0]:
                pass

    def get_valor(self, cod):
        if cod < 0:
            if -cod >= consts.MENOR_REGISTRADOR:
                return self.registradores[unichr(-(cod))]
            #elif -cod <= consts.TAMANHO_MEMORIA_DADOS