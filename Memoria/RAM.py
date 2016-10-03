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

        at.append_array(self.dados, self.pointer, const.CODIGO_SIZE)

        return self.pointer_inc()

    def pointer_inc(self):
        self.pointer = (self.pointer + const.CODIGO_SIZE) % const.CODIGO_AREA

    def pointer_dec(self):
        self.pointer = (self.pointer - const.CODIGO_SIZE) % const.CODIGO_AREA

    def enviar_codigo(self, pos):
        pass

