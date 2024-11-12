from classes.Tarefa import *
from classes.Funcionario import *
from classes.ListaFuncionario import *
from classes.ListaTarefa import *
from classes.Utils import Utils as ut

lista = ListaTarefa() #criando a lista de tarefas
listaFunc = ListaFuncionario() #criando lista de funcionarios

while (True):

    escolha = ut.CriarMenu()

    match escolha:
        case 1:
            print("\n Adicionar Tarefa \n")
            id = input("Id da tarefa: ")
            nome = input("Nome da tarefa: ")
            desc = input("Descrição: ")
            func = input("Funcionário responsável (id): ")
            data = input("Data limite: ")
            lista.AddTarefa(Tarefa(id, nome, desc, func, data))
            print("\n Tarefa adicionada \n")

        case 2:
            print("\n Remover Tarefa \n")
            id = input("Id da tarefa: ")
            lista.RemoveTarefa(lista.RemoveTarefa(id))
        
        case 3:
            print("\n Tarefas \n")
            for i in lista.itens:
                print(i)

        case 4:
            print("\n Cadastrar Funcionário \n")
            id = input("Id do funcionário ")
            nome = input("Nome do funcionário : ")
            setor = input("Setor: ")
            listaFunc.AddFuncionario(Funcionario(id, nome, setor))
            print("\n Funcionário Cadastrado \n")

        case 5:
            print("\n Funcionários \n")
            for i in listaFunc.itens:
                print(i)

        case 6:
            print("\n Concluir tarefa \n")
            id = input("Id da tarefa: ")
            for i in lista.itens:
                if (i.GetId() == id):
                    i.Concluir(id)
                    print("\n Tarefa Concluida \n")

        case 7:
            for i in lista.itens:
                if (i.GetStatus() == True):
                    print(i)

        case 8:
            for i in lista.itens:
                if (i.GetStatus() == False):
                    print(i)
                    
        case 9:
            break
        case _:
            print("")
    