from Tkinter import *
import threading


class Interface(threading.Thread):

    def __init__(self):
        super(Interface, self).__init__()
        self.top = Tk()
        #self.top.geometry("500x300")
        self.list1 = Listbox(self.top)
        self.list1.pack(side="left")

        self.list2 = Listbox(self.top)
        self.list2.pack(side="left")

        self.list3 = Listbox(self.top)
        self.list3.pack(side="left")

    def run(self):
        self.top.mainloop()



if __name__ == '__main__':
    Interface()
