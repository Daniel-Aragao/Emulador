from Computador import Componentes as Comps
from Computador import Constantes as Consts


class Barramento:
    """Componentes = {
        "Memoria": 1,
        "CPU": 2,
        "Entrada": 3
    }"""

    def __init__(self):
        self.largura = Consts.LARGURA_BARRAMENTO

    def enviar_codigo(self, alvo, dados):
        return Comps.Componentes[alvo].receber_dados(dados)

    def receber_codigo(self, alvo, pos):
        return Comps.Componentes[alvo].enviar_codigo(pos)

    def receber_valor(self, pos):
        return Comps.Componentes[Comps.RAM].enviar_valor(pos)

    def enviar_valor(self, pos, valor):
        Comps.Componentes[Comps.RAM].receber_valor(pos, valor)


