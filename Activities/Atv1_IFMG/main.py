# Escreva os códigos em Python modularizados e com tratamento de exceções para resolver os problemas a seguir:
# A) Desenvolver um algoritmo que construa uma lista de tuplas com nome e salário de
# funcionários. Em seguida, o código deve recalcular os salários considerando os seguintes
# aumentos:
# • 20% para salários de até R$2.000,00;
# • 15% para salários entre R$2.000,00 e R$5.000,00;
# • 5% para salários maiores que R$5.000,00;

lista_cadastro = []
lista_correcao = []
lista_salario_corrigido = []
lista_menor2k = []

def cadastro():
    global lista_cadastro
    try:
        nome = input('Digite seu nome: ')
        salario = int(input('Digite seu salario: '))
    except:
        print('Voce passou dados incorretos!')
        
    item = (nome, salario)
    lista_cadastro.append(item)
    
def correcao_sal(lista):
    for pessoa,salario in lista:
        if salario < 2000:
            correcao = salario * 0.2
            lista_correcao.append((pessoa,correcao))
            lista_salario_corrigido.append((pessoa,correcao+salario))
            
        elif 2000 <= salario < 5000:
            correcao = salario * 0.15
            lista_correcao.append((pessoa,correcao))
            lista_salario_corrigido.append((pessoa,correcao+salario))
            
        else:
            correcao = salario * 0.05
            lista_correcao.append((pessoa,correcao))
            lista_salario_corrigido.append((pessoa,correcao+salario))
            
    return lista_correcao

def menor2k(lista):
    for funcionario,salario in lista:
        if salario < 2000:
            lista_menor2k.append((funcionario, salario))
    return lista_menor2k
    
while True:
    cadastro()
    
    sair = input('[C]adastro, [S]air, [R]eajuste: \n').lower()
    if sair == 's':
        break
    
    elif sair == 'r':
        correcao_sal(lista_cadastro)
        
        for item in lista_correcao:
            print(item[1])
            
        menor2k(lista_salario_corrigido)
        print('Os funcionarios abaixo de 2k sao:\n')
        for nome,sal in lista_menor2k:
            print(nome)
        break
    
    elif sair == 'c':
        continue
    else:
        print('Comando digitado invalido!')
        pass