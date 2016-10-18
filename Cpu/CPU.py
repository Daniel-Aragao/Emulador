from Computador import Componentes as Comps
from EntradaSaida.Codigo import Codigo
from Computador import Constantes as Consts


class CPU:
    def __init__(self, barramento):
        self.registradores = {"A": 0, "B": 0, "C": 0, "D": 0, "CI": 0}
        self.running = True
        self.interface_selected = 0
        self.barramento = barramento

    def executar_codigo(self):
        regs = self.registradores

        if self.running:
            self.interface_selected += 1
            #                         self.barramento.update_interface()
            cod, ci = self.barramento.receber_codigo(Comps.RAM, regs["CI"])

            if cod[0] == -1:
                regs["CI"] = 0
                self.running = False

            else:
                regs["CI"] = ci

                if Codigo.operacoes["inc"] == cod[0]:
                    incrementado = -cod[1]

                    if self.is_registrador(incrementado):
                        regs[chr(incrementado)] += 1
                    else:
                        valor_antigo = self.barramento.receber_valor(incrementado)
                        self.barramento.enviar_valor(incrementado, valor_antigo + 1)

                elif Codigo.operacoes["add"] == cod[0]:
                    added = -cod[1]
                    valor_antigo = 0

                    if self.is_registrador(added):
                        valor_antigo = regs[chr(added)]
                    else:
                        valor_antigo = self.barramento.receber_valor(added)

                    valor_added = self.get_valor(cod[2])

                    valor_novo = valor_antigo + valor_added

                    if self.is_registrador(added):
                        regs[chr(added)] = valor_novo
                    else:
                        self.barramento.enviar_valor(added, valor_novo)

                elif Codigo.operacoes["mov"] == cod[0]:
                    valor_novo = self.get_valor(cod[2])

                    target = -cod[1]

                    if self.is_registrador(target):
                        regs[chr(target)] = valor_novo
                    else:
                        self.barramento.enviar_valor(target, valor_novo)

                elif Codigo.operacoes["imul"] == cod[0]:
                    target = -cod[1]

                    mult1 = self.get_valor(cod[2])
                    mult2 = self.get_valor(cod[3])
                    result = mult1 * mult2

                    if self.is_registrador(target):
                        regs[chr(target)] = result
                    else:
                        self.barramento.enviar_valor(target, result)

    @staticmethod
    def is_registrador(val):
        if val >= Consts.MENOR_REGISTRADOR:
            return True

        return False

    def get_valor(self, valor):
        if valor >= 0:
            return valor

        valor = -valor

        if self.is_registrador(valor):
            return self.registradores[chr(valor)]

        return self.barramento.receber_valor(valor)
