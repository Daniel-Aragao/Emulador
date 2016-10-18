from Tkinter import *
import math
from Computador import Constantes as Consts
from Interfaces import interface


class BarramentoConfig:

    def __init__(self):
        root = Tk()
        root.title("Configuracao do barramento")
        root.resizable(width=False, height=False)
        root.configure(background="blue")
        self.quit_root = root.destroy

        body = PanedWindow(root, relief='solid')
        body.configure()

        label_largura = Label(body, text="Largura do barramento("+str(Consts.TAMANHO_MINIMO_LARGURA_BARRAMENTO) +
                                         " <= x <= "+str(Consts.TAMANHO_MAXIMO_LARGURA_BARRAMENTO)+")")
        label_largura.pack()

        self.largura = Entry(body)
        self.largura.pack()

        self.text_resultado = StringVar()
        label_resultado = Label(body, textvariable=self.text_resultado)
        label_resultado.pack()

        self.clock = {}
        self.text_result_clock = StringVar()
        self.clock_settings(body)

        self.btnConcluir = Button(body, text="Avancar", command=self.btn_concluir)
        self.btnConcluir.pack()

        body.pack(fill="both")

        interface.center(root)
        root.mainloop()

    def clock_settings(self, body):
        label_clock = Label(body, text="Clock da memoria(" + str(Consts.CLOCK_MINIMO) + " <= y <= " + str(
            Consts.CLOCK_MAXIMO) + ")")
        label_clock.pack()

        self.clock = Entry(body)
        self.clock.pack()

        text_result_clock = Label(body, textvariable=self.text_result_clock)
        text_result_clock.pack()

    def btn_concluir(self):
        is_valido, largura = self.validar()
        is_valido_clock, clock = self.validar_clock()

        if is_valido and is_valido_clock:
            Consts.LARGURA_BARRAMENTO = largura
            Consts.CLOCK = clock

            self.quit_root()
        else:
            self.text_resultado.set("")
            self.text_result_clock.set("")

        if not is_valido:
            self.text_resultado.set("Valor invalido")

        if not is_valido_clock:
            self.text_result_clock.set("Clock invalido")

    def validar(self):
        largura = int(self.largura.get())
        if Consts.TAMANHO_MINIMO_LARGURA_BARRAMENTO <= largura:
            if Consts.TAMANHO_MAXIMO_LARGURA_BARRAMENTO >= largura:
                if ispot(largura):
                    return True, largura
        return False, largura

    def validar_clock(self):
        clock = int(self.clock.get())
        if Consts.CLOCK_MINIMO <= clock:
            if Consts.CLOCK_MAXIMO >= clock:
                return True, clock
        return False, clock


class MemoriaConfig:
    def __init__(self):
        root = Tk()
        root.title("Configuracao da memoria")
        root.resizable(width=False, height=False)
        root.configure(background="blue")
        self.quit_root = root.destroy

        body = PanedWindow(root, relief='solid')
        body.configure()

        self.tamanho = {}
        self.text_result_tamanho = StringVar()
        self.tamanho_settings(body)

        self.btnConcluir = Button(body, text="Avancar", command=self.btn_concluir)
        self.btnConcluir.pack()

        body.pack(fill="both")

        interface.center(root)
        root.mainloop()

    def tamanho_settings(self, body):
        label_tamanho = Label(body, text="Tamanho da memoria("+str(Consts.MEMORIA_TAMANHO_MINIMO)+" <= x <= " +
                                         str(Consts.MEMORIA_TAMANHO_MAXIMO)+")")
        label_tamanho.pack()

        self.tamanho = Entry(body)
        self.tamanho.pack()

        text_result_tamanho = Label(body, textvariable=self.text_result_tamanho)
        text_result_tamanho.pack()

    def btn_concluir(self):
        is_valido_tamanho, tamanho = self.validar_tamanho()

        if is_valido_tamanho:
            Consts.MEMORIA_TAMANHO = tamanho
            self.quit_root()
        else:
            self.text_result_tamanho.set("Tamanho invalido")

    def validar_tamanho(self):
        tamanho = int(self.tamanho.get())
        if Consts.MEMORIA_TAMANHO_MINIMO <= tamanho:
            if Consts.MEMORIA_TAMANHO_MAXIMO >= tamanho:
                if ispot(tamanho):
                    return True, tamanho
        return False, tamanho


def ispot(value):
    return (math.log(value, 2) % 1) == 0


if __name__ == "__main__":
    # BarramentoConfig()
    MemoriaConfig()
