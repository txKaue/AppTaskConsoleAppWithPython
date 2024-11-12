from classes.Funcionario import *
from classes.ListaFuncionario import *

class Tarefa:

    def __init__ (self, id, nome, desc, funcionario ,dataFim):
        self.id = id
        self.nome = nome
        self.desc = desc
        self.funcionario = funcionario
        self.dataFim = dataFim
        self.status = False
    
    def __str__ (self):

        if (self.status == True):
            return f"Id: {self.id} | Nome: {self.nome} | Funcionário: {self.funcionario} | Status: Feito"
        else:
            return f"Id: {self.id} | Nome: {self.nome} | Funcionário: {self.funcionario} | Status: A fazer"
    
    def Concluir(self, id):
        self.status = True

    def Editar(self, id, nome=None, desc=None, dataFim=None):
        if (nome == None):
            nome = self.nome
        if (desc == None):
            desc = self.desc
        if (dataFim == None):
            dataFim = self.dataFim

        self.nome = nome
        self.desc = desc
        self.dataFim = dataFim

    def Apagar(self, id):
        del self

    def GetId(self):
        return self.id
    
    def GetStatus(self):
        return self.status
