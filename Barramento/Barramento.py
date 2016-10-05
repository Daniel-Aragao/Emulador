from Memoria import Constantes as consts

class Barramento:
    """Componentes = {
        "Memoria": 1,
        "CPU": 2,
        "Entrada": 3
    }"""

    def __init__(self):
        self.components = []
        self.listas = []

    def enviar_codigo(self, alvo, dados):
        return self.components[alvo].receber_dados(dados)

    def receber_codigo(self, alvo, pos):
        return self.components[alvo].enviar_codigo(pos)

    def receber_valor(self, pos):
        return self.components[0].enviar_valor(pos)

    def enviar_valor(self, pos, valor):
        self.components[0].receber_valor(pos, valor)

    def update_interface(self):

        self.listas[0].set(self.components[0])

        size = self.listas[1].size()
        if size == 0:
            dados = self.components[1].get_code()
            if dados is not None:
                for i in range(len(dados)):
                    self.listas[1].insert('end', str(i)+". " + str(dados[i].parametros))

        dados = self.components[2].registradores
        if dados is not None:
            self.listas[2].delete(0, 'end')
            for i in dados:
                self.listas[2].insert('end', i +": "+ str(dados[i]))

        self.listas[1].see(self.components[2].selected)
        self.listas[1].activate(self.components[2].selected)
