'''
Faca uma lista de comprar. com listas
O usuario deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Nao permita que o programa quebre com erros de indices inexistentes na lista.

'''
import os 
lista_compras = []

while True:
    seletor = input('\nSelecione uma opção\n[i]inserir [a]pagar [l]istar [s]air : ')
    
    # Sair
    if seletor.lower().startswith('s'):
        break
    
    # Adicionar item
    elif seletor.lower().startswith('i'):
        add = input('\nDigite um item:\n')
        lista_compras.append(add)
        os.system('cls')
    
    # Deletar item
    elif seletor.lower().startswith('a'):
        os.system('cls')
        try:
            for index, item in enumerate(lista_compras):
                print(index, item)
            delete = int(input('\nDigite o indice do item a ser apagado:\n'))
            del lista_compras[delete]
            os.system('cls')
            for index, item in enumerate(lista_compras):
                print(index, item)
                
        except IndexError:
            print('\nEsse indice não existe, por favor tente novamente\n')
    # Listar 
    elif seletor.lower().startswith('l'):
        os.system('cls')
        if len(lista_compras) == 0:
            print('\nLista vazia')
        else:
            for index, item in enumerate(lista_compras):
                print(index, item)
            