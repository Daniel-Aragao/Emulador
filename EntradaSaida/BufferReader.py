from Utils.ArrayTools import ArrayTools as at


class BufferReader:

    def __init__(self, codigos):
        self.codigo = codigos
        self.ponteiro = 0

    def its_missing(self):
        return len(self.codigo) - self.ponteiro

    def get_codigo(self):
        if self.ponteiro + 1 > len(self.codigo):
            return -1

        retorno = self.codigo[self.ponteiro]

        self.ponteiro += 1

        return retorno.byteArray

    def seek(self, value):
        if value < len(self.codigo):
            self.ponteiro = value
        else:
            raise Exception("Seek value:"+value+" code length:"+len(self.codigo))

    def dec_pointer(self):
        if self.ponteiro >= 0:
            self.ponteiro -= 1
