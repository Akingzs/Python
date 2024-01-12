

def teste(*args):
    print(args)

# teste(1,2,4,5)


def teste2(*args):
    
    for item in args:
        print(item)

# teste2(1,2,4,'d')


def teste3(*args):
    return list(args)

# var1 = teste3('a',3)
# print(var1)

def multi(*args):
    multiplicador = 0
    for item in args:
        resultado = item * multiplicador
        print(f'{item} vezes {multiplicador} = {resultado}')
        multiplicador += 1

# multi(1,2,3,7,8,9)

def somador(*args):
    resultado = 0
    for item in args:
        print(f'{resultado}+{item}')
        resultado += item
        # print(resultado) 
    return resultado
        
        
var2 = somador(1,2,3,7,8,9)

print(f'O valor da variavel 2 é {var2}')