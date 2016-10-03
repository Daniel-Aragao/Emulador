from EntradaSaida.Codigo import Codigo


class CPU:
    def __init__(self, barramento):
        self.barramento = barramento
        self.registradores = {"A": 0, "B": 0, "C": 0, "D": 0, "CI": 0}

    def executar_codigo(self):
        regs = self.registradores
        running = True

        while running:
            cod, ci = self.barramento.receber_codigo(0, regs["CI"])
            if ci == -1:
                regs["CI"] = 0
                running = False
                break

        if Codigo.operacoes["inc"] == cod[0]:
            pass
        elif Codigo.operacoes["add"] == cod[0]:
            pass
        elif Codigo.operacoes["mov"] == cod[0]:
            pass
        elif Codigo.operacoes["imul"] == cod[0]:
            pass
