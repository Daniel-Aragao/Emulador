class Barramento:
    """Componentes = {
        "Memoria": 1,
        "CPU": 2,
        "Entrada": 3
    }"""

    def __init__(self):
        self.memoria = {}
        self.cpu = {}
        self.entrada = {}
        self.components = {}
        pass

    def enviar_codigo(self, alvo, dados):
        return self.components[alvo].receber_dados(dados)

    def receber_codigo(self, alvo, pos):
        return self.components[alvo].enviar_codigo(pos)
