# Classes decoradoras (Decorator classes)
class Multiplicar:
    def __init__(self, multiplicador):
        # self._multiplicador = multiplicador
        print('init')
        ...
    def __call__(self, *args, **kwargs):
        print(args, kwargs)
        return sum(args)
        # def interna(*args, **kwargs):
        #     resultado = func(*args, **kwargs)
        #     return resultado * self._multiplicador
        # return interna


'''# Quando você usa a sintaxe do decorador @Multiplicar antes da definição da função soma,
# você está efetivamente fazendo soma = Multiplicar(soma). 
# Isso significa que soma agora é uma instância da classe Multiplicar.

# No entanto, é importante notar que a função soma original ainda existe,
# mas agora está “embrulhada” dentro da instância da classe Multiplicar.
# Quando você chama soma(2, 4), você está realmente chamando o método __call__ na instância
# da classe Multiplicar.'''

@Multiplicar
def soma(x, y):
    return x + y

dois_mais_quatro = soma(2, 4)
print(dois_mais_quatro)
