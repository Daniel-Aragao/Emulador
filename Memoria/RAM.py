from Utils.ArrayTools import ArrayTools as at
from Memoria import Constantes as Const
from Barramento.Barramento import Barramento
from Computador import Componentes as Comps


class Ram:

    def __init__(self):
        self.dados = [0 for i in range(Const.TAMANHO_MEMORIA_REAL)]
        self.pointer = 0

    def receber_dados(self, dado):
        if len(dado) != Const.CODIGO_SIZE:
            raise Exception("entrada invalida na memoria")

        at.append_array(dado, self.dados, self.pointer, Const.CODIGO_SIZE)
        self.pointer_inc()
        return self.pointer

    def pointer_inc(self):
        self.pointer = (self.pointer + Const.CODIGO_SIZE) % Const.CODIGO_AREA

    def pointer_dec(self):
        self.pointer = (self.pointer - Const.CODIGO_SIZE) % Const.CODIGO_AREA

    def enviar_codigo(self, pos):
        pass

    def enviar_codigo(self, pos):
        if pos != self.pointer:
            raise MemoryError("Memoria corrompida")

        instrucao = at.sub_array(self.dados, pos, Const.CODIGO_SIZE)

        dado = Barramento.receber_codigo(Comps.ENTRADA, -1)
        if dado != -1:
            at.append_array(dado, self.dados, pos, Const.CODIGO_SIZE)
        else:
            at.append_array([-1 for i in range(Const.CODIGO_SIZE)], self.dados, pos, Const.CODIGO_SIZE)

        self.pointer_inc()
        return instrucao, self.pointer

    def enviar_valor(self, pos):
        if pos > Const.TAMANHO_MEMORIA_DADOS:
            raise MemoryError("accessViolationException")

        return self.dados[Const.OFFSET + pos]

    def receber_valor(self, pos, valor):
        if pos > Const.TAMANHO_MEMORIA_DADOS:
            raise MemoryError("accessViolationException")

        self.dados[Const.OFFSET + pos] = valor

    def __str__(self):
        string = ""
        p = 0
        while p < Const.CODIGO_AREA:
            if p == self.pointer:
                string += "*"
            string += str(at.sub_array(self.dados, start=p, size=Const.CODIGO_SIZE))

            p += Const.CODIGO_SIZE

        string += str(at.sub_array(self.dados, start=p, size=Const.CODIGO_AREA))

        return string
