from classes.Tarefa import *

class ListaTarefa:
    def __init__ (self):
        self.itens = []

    def __str__ (self):
        for i in self.itens:
            print(i)

    def AddTarefa(self, tarefa):
        self.itens.append(tarefa)

    def RemoveTarefa(self, tarefa):
        for i in self.itens:
            if (i.GetId() == tarefa):
                self.itens.pop(self.itens.index(i))
                


    