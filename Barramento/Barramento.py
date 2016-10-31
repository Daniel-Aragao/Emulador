from Computador import Componentes as Comps
from Computador import Constantes as Consts
from Computador import IComponent
from Queue import Queue
import threading
import time


class Barramento(IComponent):
    """Componentes = {
        "Memoria": 1,
        "CPU": 2,
        "Entrada": 3
    }"""

    def __init__(self):
        self.largura = Consts.LARGURA_BARRAMENTO
        self.barramento = None

        self.sinalLock = threading.Lock()
        self.fila_sinal = Queue()

        self.enderecoLock = threading.Lock()
        self.fila_endereco = Queue()

        self.dadosLock = threading.Lock()
        self.fila_dados = Queue()

    def enviar_codigo(self, alvo, dados):
        return Comps.Componentes[alvo].receber_dados(dados)

    def receber_codigo(self, alvo, pos):
        return Comps.Componentes[alvo].enviar_codigo(pos)

    def receber_valor(self, pos):
        return Comps.Componentes[Comps.RAM].enviar_valor(pos)

    def enviar_valor(self, pos, valor):
        Comps.Componentes[Comps.RAM].receber_valor(pos, valor)

    # Estrutura de sinais
    def enviar_sinal(self, sinal):
        self.sinalLock.acquire()

        time.sleep(Consts.sleep)
        self.sinalLock.release()

    def checar_sinal(self, codigo):
        self.sinalLock.acquire()

        time.sleep(Consts.sleep)
        self.sinalLock.release()
        return False

    def receber_sinal(self, sinal):
        self.sinalLock.acquire()

        time.sleep(Consts.sleep)
        self.sinalLock.release()

    # Estrutura de Enderecos
    def enviar_endereco(self, endereco):
        self.enderecoLock.acquire()

        time.sleep(Consts.sleep)
        self.enderecoLock.release()

    def checar_endereco(self, codigo):
        self.enderecoLock.acquire()

        time.sleep(Consts.sleep)
        self.enderecoLock.release()
        return False

    def receber_endereco(self):
        self.enderecoLock.acquire()

        time.sleep(Consts.sleep)
        self.enderecoLock.release()

    # Estrutura de dados
    def enviar_dado(self, dado):
        self.dadosLock.acquire()

        time.sleep(Consts.sleep)
        self.dadosLock.release()

    def checar_dado(self, codigo):
        self.dadosLock.acquire()
        self.dadosLock.release()
        return False

    def receber_dado(self, endereco):
        self.dadosLock.acquire()

        time.sleep(Consts.sleep)
        self.dadosLock.release()
