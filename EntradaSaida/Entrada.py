import threading
import time
from Regex import Regex
from BufferReader import BufferReader
from Computador import Componentes as Comps
from Computador import Constantes as Consts


class Entrada(threading.Thread):
    filepath = r"C:\\Users\danda_000\\Documents\\Estudos, Unifor\\Python\\workspace\\Arquitetura\\res\\file_sample.txt"

    def __init__(self, barramento):
        super(Entrada, self).__init__()
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

    def run(self):
        while Comps.running:
            """
            se tiver dado no buffer
                enviar sinal T_origem = ram, T_destino = entrada, T_dado = instrucao_index, T_tipo =  T_E_Instrucao
                receber endereco
                se o endereco for valido
                    enviar dado
            """
            time.sleep(Consts.sleep)
