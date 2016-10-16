from Computador import Componentes as Comps


class Barramento:
    """Componentes = {
        "Memoria": 1,
        "CPU": 2,
        "Entrada": 3
    }"""

    def __init__(self):
        pass

    @staticmethod
    def enviar_codigo(alvo, dados):
        return Comps.Componentes[alvo].receber_dados(dados)

    @staticmethod
    def receber_codigo(alvo, pos):
        return Comps.Componentes[alvo].enviar_codigo(pos)

    @staticmethod
    def receber_valor(pos):
        return Comps.Componentes[Comps.RAM].enviar_valor(pos)

    @staticmethod
    def enviar_valor(pos, valor):
        Comps.Componentes[Comps.RAM].receber_valor(pos, valor)


