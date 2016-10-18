from Regex import Regex
from BufferReader import BufferReader
from Computador import Componentes as Comps


class Entrada:
    filepath = r"C:\\Users\danda_000\\Documents\\Estudos, Unifor\\Python\\workspace\\Arquitetura\\res\\file_sample.txt"

    def __init__(self, barramento):
        self.buffer = {}
        self.barramento = barramento

    def preencher_memoria(self, regex):
        self.buffer = BufferReader(regex.traducao)

        enviando = True
        while enviando:
            codigo = self.buffer.get_codigo()
            if codigo != -1:
                enviando = self.barramento.enviar_codigo(Comps.RAM, codigo) != 0
            else:
                enviando = False

    def read_file(self, path=filepath):
        vetor_strings = self.importar_codigo(path)
        regex = Regex(vetor_strings)
        return regex

    def enviar_codigo(self, pos):
        return self.buffer.get_codigo()

    def get_code(self):
        return self.buffer.get_code()

    @staticmethod
    def importar_codigo(path=filepath):
        f = open(path, 'r')
        return f.read().splitlines()
