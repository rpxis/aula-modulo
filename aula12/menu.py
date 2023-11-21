from use_cases.adicionar import adicionarProduto
from use_cases.editar import editarProduto
from use_cases.deletar import deletarProduto
from use_cases.listar import listarProdutos


def menu():
    while True:
        print('--- Menu de produtos ---')
        print('1 - Cadatrar produto')
        print('2 - Editar produto')
        print('3 - Deletar produto')
        print('4 - Listar todos os produtos')
        print('5 - Sair do sistema')

        option = input('Selecione uma opção: ')

        if option == '1':
            nameProduct = input('Digite o nome do produto: ')
            category = input('Digite a categoria do produto: ')
            price = float(input('Digite o preço do produto: '))
            adicionarProduto(nameProduct, category, price)
        elif option == '2':
            code = int(input('Digite o código do produto: '))
            nameProduct = input('Digite o nome do produto: ')
            category = input('Digite a categoria do produto: ')
            price = float(input('Digite o preço do produto: '))
            editarProduto(code, nameProduct, category, price)
        elif option == '3':
            code = int(input('Digite o código do produto: '))
            deletarProduto(code)
        elif option == '4':
            listarProdutos()
        else:
            print('Você saiu do programa')





menu()