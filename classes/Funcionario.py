class Funcionario:
    
    def __init__ (self, id, nome, setor):
        self.id = id
        self.nome = nome
        self.setor = setor
    
    def __str__ (self):
        return f"Id: {self.id} | Nome: {self.nome} | Setor: {self.setor}"
    
    def Edit (self, nome=None, Setor=None):
        if (nome == None):
            nome = self.nome
        if (setor == None):
            setor = self.setor
            
        self.nome = nome
        self.setor = setor
    
    def GetId(self):
        return self.id
