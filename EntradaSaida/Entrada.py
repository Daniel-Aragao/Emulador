from Barramento import Barramento
from Regex import Regex
from BufferReader import BufferReader


class Entrada:
    filepath = r"C:\Users\danda_000\Documents\Estudos, Unifor\Python\workspace\Arquitetura\res\file_sample.txt"

    def __init__(self, barramento):
        self.barramento = barramento
        self.buffer = {}
        pass

    def executar_codigo(self, path=filepath):
        vetor_strings = self.importar_codigo(path)
        regex = Regex(vetor_strings)
        buffer = BufferReader(regex.traducao)
        """
        criar um while que vai executar até receber um false do barramento,
        pois o objetivo é enviar pro barramento, por consequencia para memória,
        todas (ou o que puder) das linhas que estão no buffer,
        dessa forma vai ser retirado do buffer utilizando o método buffer.get_codigo(1)
        que vai retirar codigo por codigo pra cada iteração do laço
        quando receber um false o laço morre e então será tratado o caso do recebimento
        da memória um pedido de dados que será efetuado toda vez que houver espaço na memória
        essa mesma terá que enviar pro barramento anteriormente que acionará o método da entrada

        """

    @staticmethod
    def importar_codigo(path=filepath):
        f = open(path, 'r')
        return f.readlines()
