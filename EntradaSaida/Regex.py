import re
from Codigo import Codigo


class Regex:
    def __init__(self, linhas):
        self.linhas = linhas
        self.traducao = Regex.traduzir(linhas)

    @staticmethod
    def traduzir(linhas):
        pettern = r"(\w+)\s*"
        traducao = []

        operacao = re.compile(pettern)
        patterns = {
            "add": r"^\s*(\w+)\s+(\w+)\s*,\s*(\w+)\s*$",
            "mov": r"^\s*(\w+)\s+(\w+)\s*,\s*(\w+)\s*$",
            "imul": r"^\s*(\w+)\s+(\w+)\s*,\s*(\w+)\s*,\s*(\w+)\s*$",
            "inc": r"^\s*(\w+)\s+(\w+)\s*$",
            "dec": r"^\s*(\w+)\s+(\w+)\s*$",
            "label": r"^\s*(\w+)\s+(\w+)\s*$"
        }
refatorar
        for linha in linhas:
            expressao = None

            expressao = patterns[operacao.match(linha).group(1)]

            if expressao == None:
                raise Exception('Operador inexistente')

            comandos = re.findall(expressao, linha)[0]

            codigo = Codigo(comandos)

            traducao.append(codigo)

        return traducao
