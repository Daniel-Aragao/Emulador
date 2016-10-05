class Barramento:
    """Componentes = {
        "Memoria": 1,
        "CPU": 2,
        "Entrada": 3
    }"""

    def __init__(self):
            self.components = {}

    def enviar_codigo(self, alvo, dados):
        return self.components[alvo].receber_dados(dados)

    def receber_codigo(self, alvo, pos):
        return self.components[alvo].enviar_codigo(pos)

    def receber_valor(self, pos):
        return self.components[0].enviar_valor(pos)

    def enviar_valor(self, pos, valor):
        self.components[0].receber_valor(pos, valor)
