
class ArrayTools:
    def __init__(self):
        pass

    @staticmethod
    def sub_array(lista, start, size, step=1):
        novalista = []
        for i in range(start, start + size, step):
            novalista.append(lista[i])

        return novalista

