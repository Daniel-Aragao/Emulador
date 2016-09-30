
class Entrada:
    filepath = r"C:\Users\danda_000\Documents\Estudos, Unifor\Python\workspace\Arquitetura\res\file_sample.txt"

    def __init__(self):
        pass

    def executar_codigo(self, path=filepath):
        vetor_strings = self.importar_codigo(path)


    def importar_codigo(self, path=filepath):
        f = open(path, 'r')
        return f.readlines()


