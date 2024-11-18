from classes.Tarefa import *
from classes.Funcionario import *
from classes.ListaFuncionario import *
from classes.ListaTarefa import *
from classes.Utils import Utils as ut

def criar_funcionarios(listaFunc):
    print("\n** Criando Funcionários **")

    funcionarios = [
        Funcionario("F001", "João Silva", "Desenvolvimento"),
        Funcionario("F002", "Maria Oliveira", "Marketing"),
        Funcionario("F003", "Carlos Santos", "Recursos Humanos"),
        Funcionario("F004", "Ana Souza", "TI")
    ]

    for func in funcionarios:
        listaFunc.AddFuncionario(func)


def listar_funcionarios(listaFunc):
    print("\n** Lista de Funcionários **")
    for funcionario in listaFunc.itens:
        print(funcionario)


def criar_tarefas(lista, listaFunc):
    print("\n** Criando Tarefas **")

    tarefas = [
        Tarefa("T001", "Desenvolver Algoritmo", "Desenvolver um algoritmo de testes", "F001", "2024-12-01"),
        Tarefa("T002", "Analisar Mercado", "Analisar o mercado para estratégia de marketing", "F002", "2024-12-10"),
        Tarefa("T003", "Recrutamento", "Realizar recrutamento de novos funcionários", "F003", "2024-11-30"),
        Tarefa("T004", "Migrar Sistemas", "Migrar sistemas para a nova infraestrutura", "F004", "2024-12-15")
    ]

    for tarefa in tarefas:
        lista.AddTarefa(tarefa)


def listar_tarefas(lista):
    print("\n** Lista de Tarefas **")
    for tarefa in lista.itens:
        print(tarefa)


def concluir_metade_tarefas(lista):
    print("\n** Concluindo Metade das Tarefas **")
    for i, tarefa in enumerate(lista.itens):
        if i % 2 == 0:  
            tarefa.Concluir(tarefa.GetId())


def listar_tarefas_concluidas(lista):
    print("\n** Lista de Tarefas Concluídas **")
    for tarefa in lista.itens:
        if tarefa.GetStatus():  
            print(tarefa)


def listar_tarefas_pendentes(lista):
    print("\n** Lista de Tarefas Pendentes **")
    for tarefa in lista.itens:
        if not tarefa.GetStatus(): 
            print(tarefa)


def excluir_tarefas(lista):
    print("\n** Excluindo Todas as Tarefas **")
    for tarefa in lista.itens:
        lista.RemoveTarefa(tarefa.GetId())  
    
   
    print("Lista de tarefas após remoção:")
    for tarefa in lista.itens:
        print(tarefa)


def rodar_testes():
    lista = ListaTarefa()  
    listaFunc = ListaFuncionario()  

    criar_funcionarios(listaFunc)
    
    listar_funcionarios(listaFunc)
    
    criar_tarefas(lista, listaFunc)

    listar_tarefas(lista)
    
    concluir_metade_tarefas(lista)
    
    listar_tarefas_concluidas(lista)
    
    listar_tarefas_pendentes(lista)
    
    excluir_tarefas(lista)


rodar_testes()
