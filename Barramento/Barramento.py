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
        self.update_interface()
        return self.components[alvo].receber_dados(dados)

    def receber_codigo(self, alvo, pos):
        self.update_interface()
        return self.components[alvo].enviar_codigo(pos)

    def receber_valor(self, pos):
        self.update_interface()
        return self.components[0].enviar_valor(pos)

    def enviar_valor(self, pos, valor):
        self.update_interface()
        self.components[0].receber_valor(pos, valor)

    def update_interface(self):
        dados = self.components[0].dados
        if dados is not None:
            self.listas[0].delete(0, 'end')
            for i in range(len(dados)):
                self.listas[0].insert('end', str(i)+": " + str(dados[i]))

        dados = self.components[1].get_not_read()
        if dados is not None:
            self.listas[1].delete(0, 'end')
            for i in range(len(dados)):
                self.listas[1].insert('end', str(i)+". " + str(dados[i]))

        dados = self.components[2].registradores
        if dados is not None:
            self.listas[2].delete(0, 'end')
            for i in dados:
                self.listas[2].insert('end', i +": "+ str(dados[i]))
