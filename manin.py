from banco import BancoDeDados
from livro import Livro

def meu():
    db = BancoDeDados()

    while True:
        print("\n1. Cadastrar Livro")
        escolha = input("Escolha uma opção: ")
        