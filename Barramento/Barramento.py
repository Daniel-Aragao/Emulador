class Barramento:
    Componentes = {
        "Memoria": 1,
        "CPU": 2,
        "Entrada": 3
    }

    def __init__(self):
        self.memoria = {}
        self.cpu = {}
        self.entrada = {}
        pass

    def enviar_codigo(self, alvo, dados):
        pass

    def receber_codigo(self, alvo, dados):
        pass
