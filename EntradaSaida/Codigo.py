from Computador import Constantes


class Codigo:
    operacoes = {
        "inc": 1,
        "add": 2,
        "mov": 3,
        "imul": 4
    }

    def __init__(self, args):
        self.parametros = args
        self.byteArray = self.to_byte_array(self.parametros)

    def to_byte_array(self, parametros):
        ops = self.__class__.operacoes

        byte_array = [-1, -1, -1, -1]

        # pegando qual operacao sera executada
        byte_array[0] = ops[parametros[0]]

        # pegando o primeiro valor, independe da operacao
        byte_array[1] = self.solve_value(parametros[1])
        if byte_array[1] > 0:
            raise Exception("primeiro valor nao pode ser uma constante")

        # se a operacao for add, mov ou imul existe o 3 parametro
        if byte_array[0] > ops["inc"]:
            byte_array[2] = self.solve_value(parametros[2])

            # se a operacao for imul existe o 4 parametro
            if byte_array[0] > ops["mov"]:
                byte_array[3] = self.solve_value(parametros[3])

        return byte_array

    # converte o valor para posicao da memoria, registrador ou inteiro
    @staticmethod
    def solve_value(valor):
        retorno = None
        try:
            # tenta covnerter para inteiro
            retorno = int(valor)
            if retorno > Constantes.MAIOR_INTEIRO:
                raise MemoryError("Nao e possivel armazenar valores maiores que " + Constantes.MAIOR_INTEIRO)
            return retorno
        except ValueError:
            pass

        try:
            # tenta converter para registrador
            retorno = -ord(valor)
            if -retorno > Constantes.MAIOR_REGISTRADOR or -retorno < Constantes.MENOR_REGISTRADOR:
                raise MemoryError("Registrador inexistente")
            return retorno
        except TypeError:
            pass

        # converte para posicao de memoria
        if retorno is None:
            retorno = -int(valor, 16)
            if -retorno > Constantes.memoria_particao_dados():
                raise MemoryError("Posicao de memoria inexistente")
        return retorno
