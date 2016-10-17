from Tkinter import *
from Interfaces import interface
from Memoria import Constantes as Consts


class BarramentoConfig:

    def __init__(self):
        root = Tk()
        root.title("Configuracao do barramento")
        root.resizable(width=False, height=False)
        root.configure(background="blue")
        self.quit_root = root.destroy

        body = PanedWindow(root, relief='solid')
        body.configure()

        label_largura = Label(body, text="Largura do barramento")
        label_largura.pack()

        self.largura = Entry(body)
        self.largura.pack()

        self.text_resultado = StringVar()
        label_resultado = Label(body, textvariable=self.text_resultado)
        label_resultado.pack()

        self.btnConcluir = Button(body, text="Avancar", command=self.btn_concluir)
        self.btnConcluir.pack()

        body.pack(fill="both")

        interface.center(root)
        root.mainloop()

    def btn_concluir(self):
        is_valido, largura = self.validar()
        if is_valido:
            Consts.LARGURA_BARRAMENTO = largura
            self.quit_root()
        else:
            self.text_resultado.set("Valor invalido")

    def validar(self):
        largura = int(self.largura.get())
        if Consts.TAMANHO_MINIMO_LARGURA_BARRAMENTO <= largura:
            if Consts.TAMANHO_MAXIMO_LARGURA_BARRAMENTO >= largura:
                return True, largura
        return False, largura


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

        self.clock = {}
        self.text_result_clock = StringVar()
        self.clock_settings(body)

        self.btnConcluir = Button(body, text="Avancar", command=self.btn_concluir)
        self.btnConcluir.pack()

        body.pack(fill="both")

        interface.center(root)
        root.mainloop()

    def tamanho_settings(self, body):
        label_tamanho = Label(body, text="Tamanho da memoria("+str(Consts.TAMANHO_MINIMO_MEMORIA)+" <= x <= "+str(Consts.TAMANHO_MAXIMO_MEMORIA)+")")
        label_tamanho.pack()

        self.tamanho = Entry(body)
        self.tamanho.pack()

        text_result_tamanho = Label(body, textvariable=self.text_result_tamanho)
        text_result_tamanho.pack()

    def clock_settings(self, body):
        label_clock = Label(body, text="Clock da memoria("+str(Consts.CLOCK_MINIMO)+" <= y <= "+str(Consts.CLOCK_MAXIMO)+")")
        label_clock.pack()

        self.clock = Entry(body)
        self.clock.pack()

        text_result_clock = Label(body, textvariable=self.text_result_clock)
        text_result_clock.pack()

    def btn_concluir(self):
        is_valido_tamanho, tamanho = self.validar_tamanho()
        is_valido_clock, clock = self.validar_clock()

        if is_valido_tamanho and is_valido_clock:
            Consts.TAMANHO_MEMORIA_REAL = tamanho
            Consts.CLOCK = clock
            self.quit_root()

        if not is_valido_tamanho:
            self.text_result_tamanho.set("Tamanho invalido")

        if not is_valido_clock:
            self.text_result_clock.set("Clock invalido")

    def validar_tamanho(self):
        tamanho = int(self.tamanho.get())
        if Consts.TAMANHO_MINIMO_MEMORIA <= tamanho:
            if Consts.TAMANHO_MAXIMO_MEMORIA >= tamanho:
                return True, tamanho
        return False, tamanho

    def validar_clock(self):
        clock = int(self.clock.get())
        if Consts.CLOCK_MINIMO <= clock:
            if Consts.CLOCK_MAXIMO >= clock:
                return True, clock
        return False, clock

if __name__ == "__main__":
    # BarramentoConfig()
    MemoriaConfig()
