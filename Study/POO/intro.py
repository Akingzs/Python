# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios *atributos* e *métodos*.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))
class Pessoa:
    # __init__ sempre inicia uma classe e o primeiro param é self, se referindo sempre é uma estancia daquele elemento
    # Atributos
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def andar(self,velocidade):
        return velocidade 

p1 = Pessoa('Luiz', 'Otávio')
p1.andar(5)

print(p1.andar(3))



p2 = Pessoa('Maria', 'Joana')

# print(p1.nome)
# print(p1.sobrenome)

# print(p2.nome)
# print(p2.sobrenome)