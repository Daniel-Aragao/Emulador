from Utils import ArrayTools as at


class BufferReader:

    def __init__(self, codigos):
        self.codigo = codigos
        self.ponteiro = 0

    def its_missing(self):
        return len(self.codigo) - self.ponteiro

    def get_codigo(self, qtde_lines=1):
        if (self.ponteiro + qtde_lines) > len(self.codigo):
            return -1

        self.ponteiro += qtde_lines

        retorno = at.sub_array(self.codigo, self.ponteiro, qtde_lines)
        return retorno

    def seek(self, value):
        if value < len(self.codigo):
            self.ponteiro = value
        else:
            raise Exception("Seek value:"+value+" code length:"+len(self.codigo))
