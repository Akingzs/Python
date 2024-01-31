# Funções decoradoras e decoradores com classes

# Definindo a função que será usada para criar a representação em string do objeto
def meu_str(self):
    # Obtendo o nome da classe do objeto
    class_name = self.__class__.__name__
    # Obtendo o dicionário de atributos do objeto
    class_dict = self.__dict__
    # Criando a representação em string
    class_str = f'{class_name}({class_dict})'
    return class_str

# Definindo o decorador que adicionará o método __str__ à classe
def adiciona_str(cls):
    # Adicionando o método __str__ à classe
    cls.__str__ = meu_str
    # Retornando a classe modificada
    return cls

# Usando o decorador na definição da classe Animal
@adiciona_str
class Animal:
    def __init__(self, nome):
        self.nome = nome

# Usando o decorador na definição da classe Fruta
@adiciona_str
class Fruta:
    def __init__(self, nome):
        self.nome = nome

# Criando objetos das classes Animal e Fruta
gato = Animal('Gato')
cachorro = Animal('Cachorro')

maca = Fruta('Maçã')
banana = Fruta('Banana')

# Imprimindo os objetos. Isso chamará o método __str__ que foi adicionado pelo decorador
print(gato)
print(cachorro)

print(maca)
print(banana)
