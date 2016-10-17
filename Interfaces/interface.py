from Tkinter import *
import threading


class Interface(threading.Thread):

    def __init__(self):
        super(Interface, self).__init__()
        self.top = Tk()
        self.top.title("Arquitetura de John Von Neumann")
        self.top.geometry("500x260")
        self.top.configure(background="blue")
        self.top.resizable(width=False, height=False)

        self.btnNext = None
        self.btnFinish = None
        self.textoCentro = None
        self.list3 = None
        self.list2 = None
        self.list1 = None
        self.message = None

        body = self.body_group()

        self.top_group(body)

        self.left_group(body)

        self.right_group(body)

        self.center_group(body)

        body.pack(fill="x")

        self.footer_group()

    def footer_group(self):
        footer = PanedWindow(self.top, relief=RAISED)

        self.btnNext = Button(footer, text="Avancar")
        self.btnFinish = Button(footer, text="Concluir")

        self.btnFinish.pack(side="left")
        self.btnNext.pack(side="left")
        footer.pack(side="bottom", fill="x", expand=True)

    def center_group(self, body):
        panelmiddle = PanedWindow(body)

        self.textoCentro = StringVar()
        self.textoCentro.set("Arquitetura de John Von Neumann")

        Label(panelmiddle, textvariable=self.textoCentro).pack(fill="both", expand=True)

        panelmiddle.pack(fill="both", expand=True)

    def right_group(self, body):
        panel2 = PanedWindow(body)
        self.list3 = Listbox(panel2, relief=RAISED)

        labregs = StringVar()
        labregs.set("Registradores")

        Label(panel2, textvariable=labregs).pack()
        self.list3.pack()
        panel2.pack(side="right")

    def left_group(self, body):
        panel1 = PanedWindow(body)
        self.list2 = Listbox(panel1, relief=RAISED)

        labenter = StringVar()
        labenter.set("Entrada")

        Label(panel1, textvariable=labenter).pack()
        self.list2.pack()
        panel1.pack(side="left")

    def top_group(self, body):
        toppanel = PanedWindow(body)
        self.list1 = StringVar()

        labmem = StringVar()
        labmem.set("Memoria")
        self.message = Label(toppanel, textvariable=self.list1, relief=RAISED)

        Label(toppanel, textvariable=labmem).pack()
        self.message.pack()
        toppanel.pack(side="top", fill='x')

    def body_group(self):
        body = PanedWindow(self.top, relief='solid')
        body.configure(background="red")
        return body

    def run(self):
        center(self.top)
        self.top.mainloop()


def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w / 2 - size[0] / 2
    y = h / 2 - size[1] / 2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

if __name__ == '__main__':
    Interface()
