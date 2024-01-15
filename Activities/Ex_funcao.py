# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def multi(*args):
    total = 1
    for item in args:
        total *= item
    print(f'Total multiplicao: {total}')
    return total

def impar_par(number):
    if number % 2 == 0:
        return f'O numero {number} é Par'
    else:
        return f'O numero {number} é Impar'

var1 = multi(2,2)
var2 = multi(7,9)

impar_par(var1)
impar_par(var2)
