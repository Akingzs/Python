'''

args - Argumentos não nomeados
*-* args (empacotamento e desempacotamento)

'''

# x,y, *resto = 1,2,3,4

# print(x, y, resto)

# numeros = 1,2,3,4,5,6

# # Retorna uma tupla
# print(numeros)
# # Usando * para desempacotar a tupla
# print(*numeros)

def funcao(*args):
    print(type(args))  # Saída: <class 'tuple'>

funcao(1, 2, 3)

def funcao(a, b, c):
    print(a, b, c)

valores = (1, 2, 3)
funcao(*valores)  # Saída: 1 2 3
