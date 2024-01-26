# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, x):
    # Crio uma funcao interna para salvar o retorno final da função, e retorno temporariamente a função interna, 
    # permitindo atrasar o retorno da funcao principal
    def interna(y):
        return funcao(x,y) 
    return interna

# Atribuindo o resultado da funcao interna atrasando a finalização da funcao
soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

soma_com_cinco(5)