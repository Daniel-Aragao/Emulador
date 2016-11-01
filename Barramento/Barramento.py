from Computador import Componentes as Comps
from Computador import Constantes as Consts
import threading
import time


class Barramento:

    def __init__(self):
        self.sinalLock = threading.Lock()
        self.fila_sinal = []

        self.enderecoLock = threading.Lock()
        self.fila_endereco = []

        self.dadosLock = threading.Lock()
        self.fila_dados = []

    """
    def enviar_codigo(self, alvo, dados):
        return Comps.Componentes[alvo].receber_dados(dados)

    def receber_codigo(self, alvo, pos):
        return Comps.Componentes[alvo].enviar_codigo(pos)

    def receber_valor(self, pos):
        return Comps.Componentes[Comps.RAM].enviar_valor(pos)

    def enviar_valor(self, pos, valor):
        Comps.Componentes[Comps.RAM].receber_valor(pos, valor)
    """

    # Estrutura de sinais
    def enviar_sinal(self, sinal):
        self.sinalLock.acquire()

        self.fila_sinal.append(sinal)

        time.sleep(Consts.sleep)
        self.sinalLock.release()

    def checar_sinal(self, codigo):
        self.sinalLock.acquire()
        retorno = False

        if len(self.fila_sinal):
            if codigo == self.fila_sinal[0][Consts.T_DESTINO]:
                retorno = True

        self.sinalLock.release()
        return retorno

    def receber_sinal(self):
        self.sinalLock.acquire()

        retorno = self.fila_sinal.pop(0)

        time.sleep(Consts.sleep)
        self.sinalLock.release()
        return retorno

    # Estrutura de Enderecos
    def enviar_endereco(self, endereco):
        self.enderecoLock.acquire()

        self.fila_endereco.append(endereco)

        time.sleep(Consts.sleep)
        self.enderecoLock.release()

    def checar_endereco(self, codigo):
        self.enderecoLock.acquire()
        retorno = False

        if len(self.fila_sinal):
            if codigo == self.fila_endereco[0][Consts.T_DESTINO]:
                retorno = True

        self.enderecoLock.release()
        return retorno

    def receber_endereco(self):
        self.enderecoLock.acquire()

        retorno = self.fila_endereco.pop(0)

        time.sleep(Consts.sleep)
        self.enderecoLock.release()
        return retorno

    # Estrutura de dados
    def enviar_dado(self, dado):
        self.dadosLock.acquire()

        self.fila_dados.append(dado)

        time.sleep(Consts.sleep)
        self.dadosLock.release()

    def checar_dado(self, codigo):
        self.dadosLock.acquire()
        retorno = False

        if len(self.fila_sinal):
            if codigo == self.fila_dados[0][Consts.T_DESTINO]:
                retorno = True

        self.dadosLock.release()
        return retorno

    def receber_dado(self):
        self.dadosLock.acquire()

        retorno = self.fila_dados.pop(0)

        time.sleep(Consts.sleep)
        self.dadosLock.release()
        return retorno
