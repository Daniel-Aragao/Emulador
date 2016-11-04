import threading
import time
from Computador import Componentes as Comps
from EntradaSaida.Codigo import Codigo
from Computador import Constantes as Consts


class CPU(threading.Thread):

    def __init__(self, barramento):
        super(CPU, self).__init__()
        self.registradores = {"A": 0, "B": 0, "C": 0, "D": 0, "CI": 0}
        self.barramento = barramento
        self.esperando_dado = False
        self.esperando_endereco = False
        """
        self.running = True
        self.interface_selected = 0

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
        """

    def run(self):
        while Comps.running:
            self.enviar_sinal()
            self.receber_endereco()
            self.receber_dado()

            time.sleep(Consts.sleep)

    def enviar_sinal(self):
        if (not self.esperando_dado) and (not self.esperando_endereco) and self.registradores["CI"] != -1:
            sinal = [0 for i in Consts.T_LENGTH]
            sinal[Consts.T_ORIGEM] = Comps.CPU
            sinal[Consts.T_DESTINO] = Comps.RAM
            sinal[Consts.T_DADOS] = self.registradores["CI"]
            sinal[Consts.T_TIPO] = Consts.T_L_INSTRUCAO

            self.barramento.enviar_sinal(sinal)

            # self.esperando_dado = True
            # self.esperando_endereco = True

            # problema: se eu mandar dois sinais(ci's) iguais o processador
            # acabara por processar a mesma instrucao duas vezes

    def receber_endereco(self):
        if (not self.esperando_dado) and self.barramento.checar_endereco(Comps.CPU):
            endereco = self.barramento.receber_endereco()
            # if endereco != -1:
            self.registradores["CI"] = endereco

            if not self.esperando_endereco:
                self.esperando_dado = True

            self.esperando_endereco = False

    def receber_dado(self):
        if (not self.esperando_endereco) and self.barramento.checar_dado(Comps.CPU):
            dado = self.barramento.receber_dado()

            # processar

            if not self.esperando_dado:
                self.esperando_endereco = True

            self.esperando_dado = False
