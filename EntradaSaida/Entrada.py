from Barramento import Barramento
from Regex import Regex
from BufferReader import BufferReader


class Entrada:
    filepath = r"C:\\Users\danda_000\\Documents\\Estudos, Unifor\\Python\\workspace\\Arquitetura\\res\\file_sample.txt"

    def __init__(self, barramento):
        self.barramento = barramento
        self.buffer = {}

    def preencher_memoria(self, path=filepath):
        vetor_strings = self.importar_codigo(path)
        regex = Regex(vetor_strings)
        self.buffer = BufferReader(regex.traducao)

        enviando = True
        while enviando:
            enviando = self.barramento.enviar_codigo(0, self.buffer.get_codigo(1)) != 0

    def receber_codigo(self, pos):
        return self.buffer.get_codigo()

    @staticmethod
    def importar_codigo(path=filepath):
        f = open(path, 'r')
        return f.readlines()
