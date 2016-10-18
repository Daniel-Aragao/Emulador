from Computador import Componentes as Comps
from Computador import Constantes as Const
from Utils.ArrayTools import ArrayTools as at


class Ram:

    def __init__(self, barramento):
        self.dados = [0 for i in range(Const.MEMORIA_TAMANHO)]
        self.barramento = barramento
        self.pointer = 0

    def receber_dados(self, dado):
        if not isinstance(dado, type([])) or len(dado) != Const.CODIGO_SIZE:
            raise Exception("entrada invalida na memoria: " + str(dado))

        at.append_array(dado, self.dados, self.pointer, Const.CODIGO_SIZE)
        self.pointer_inc()
        return self.pointer

    def pointer_inc(self):
        self.pointer = (self.pointer + Const.CODIGO_SIZE) % Const.memoria_particao_codigo()

    def pointer_dec(self):
        self.pointer = (self.pointer - Const.CODIGO_SIZE) % Const.memoria_particao_codigo()

    def enviar_codigo(self, pos):
        if pos != self.pointer:
            raise MemoryError("Memoria corrompida: pointer = "+str(self.pointer)+" search position: " + str(pos))

        instrucao = at.sub_array(self.dados, pos, Const.CODIGO_SIZE)

        dado = self.barramento.receber_codigo(Comps.ENTRADA, -1)
        if dado != -1:
            at.append_array(dado, self.dados, pos, Const.CODIGO_SIZE)
        else:
            at.append_array([-1 for i in range(Const.CODIGO_SIZE)], self.dados, pos, Const.CODIGO_SIZE)

        self.pointer_inc()
        return instrucao, self.pointer

    def enviar_valor(self, pos):
        if pos > Const.memoria_particao_dados():
            raise MemoryError("accessViolationException")

        return self.dados[Const.memoria_particao_codigo() + pos]

    def receber_valor(self, pos, valor):
        if pos > Const.memoria_particao_dados():
            raise MemoryError("accessViolationException")

        self.dados[Const.memoria_particao_codigo() + pos] = valor

    def __str__(self):
        string = ""
        p = 0
        while p < Const.memoria_particao_codigo():
            if p == self.pointer:
                string += "==>"
            string += str(at.sub_array(self.dados, start=p, size=Const.CODIGO_SIZE))

            p += Const.CODIGO_SIZE

        string += str(at.sub_array(self.dados, start=p, size=Const.memoria_particao_codigo()))

        return string
