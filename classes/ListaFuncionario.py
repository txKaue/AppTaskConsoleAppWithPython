from classes.Funcionario import *

class ListaFuncionario:
    def __init__ (self):
        self.itens = []

    def __str__ (self):
        for i in self.itens:
            print(i)

    def AddFuncionario(self, Funcionario):
        self.itens.append(Funcionario)

    def RemoveFuncionario(self, Funcionario):
        for i in self.itens:
            if (i.GetId() == Funcionario):
                self.itens.pop(self.itens.index(i))
                
        print("Não foi possível encontrar a Funcionario")