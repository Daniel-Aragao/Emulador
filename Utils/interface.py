from Tkinter import *
import threading


class Interface(threading.Thread):

    def __init__(self):
        super(Interface, self).__init__()
        self.top = Tk()
        self.top.title("Arquitetura de John Von Neumann")
        #self.top.geometry("480x280")
        self.top.configure(background="blue")

        # body group
        body = PanedWindow(self.top, relief='solid')
        body.configure(background="red")

        # top group
        toppanel = PanedWindow(body)
        self.list1 = StringVar()
        labmem = StringVar()
        labmem.set("Memoria")

        self.message = Label(toppanel, textvariable=self.list1, relief=RAISED)

        Label(toppanel, textvariable=labmem).pack()
        self.message.pack()
        toppanel.pack(side="top", fill='x')

        # left group
        panel1 = PanedWindow(body)
        self.list2 = Listbox(panel1, relief=RAISED)
        labenter = StringVar()

        labenter.set("Entrada")
        Label(panel1, textvariable=labenter).pack()
        self.list2.pack()

        panel1.pack(side="left")

        # right group
        panel2 = PanedWindow(body)
        self.list3 = Listbox(panel2, relief=RAISED)
        labregs = StringVar()

        labregs.set("Registradores")
        Label(panel2, textvariable=labregs).pack()
        self.list3.pack()

        panel2.pack(side="right")

        # center group
        panelmiddle = PanedWindow(body)
        self.textoCentro = StringVar()
        self.textoCentro.set("Arquitetura de John Von Neumann")

        Label(panelmiddle, textvariable=self.textoCentro).pack(fill="both", expand=True)
        panelmiddle.pack(fill="both", expand=True)


        body.pack()

        # footer group
        footer = PanedWindow(self.top, relief=RAISED)

        self.btn = Button(footer, text="Avancar")

        self.btn.pack()
        footer.pack(side="bottom", fill="x", expand=True)

    def run(self):
        self.top.mainloop()



if __name__ == '__main__':
    Interface()
