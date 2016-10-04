from Utils.ArrayTools import ArrayTools as at
from Memoria import Constantes as const


class Ram:

    def __init__(self, barramento):
        self.barramento = barramento
        self.dados = []
        self.pointer = 0

    def receber_dados(self, dado):
        if len(dado) != const.CODIGO_SIZE:
            raise Exception("entrada inválida na memória")

        at.append_array(dado, self.dados, self.pointer, const.CODIGO_SIZE)

        return self.pointer_inc()

    def pointer_inc(self):
        self.pointer = (self.pointer + const.CODIGO_SIZE) % const.CODIGO_AREA

    def pointer_dec(self):
        self.pointer = (self.pointer - const.CODIGO_SIZE) % const.CODIGO_AREA

    def enviar_codigo(self, pos):
        pass

    def enviar_codigo(self, pos):
        if pos != self.pointer:
            raise MemoryError("Memoria corrompida")

        instrucao = at.sub_array(self.dados, pos, const.CODIGO_SIZE)
        """
        nesse ponto pedir ao barramento informacao
        para inserir os dados novos onde estava o
        codigo enviado para cpu
        """
        dado = self.barramento.receber_codigo(1, 0)
        at.append_array(dado, self.dados, pos, const.CODIGO_SIZE)

        self.pointer_inc()
        return instrucao, self.pointer
