# O polimorfismo é um conceito fundamental na programação orientada a objetos (OOP) 
# que permite que um mesmo método tenha comportamentos diferentes em classes diferentes.
# Isso significa que um método pode ser usado de maneira uniforme, 
# independentemente da classe do objeto em que está sendo chamado

# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.

# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
# Sobrecarga de métodos (overload)  🐍 = ❌
# Sobreposição de métodos (override) 🐍 = ✅


class Animal:
    def locomove(self):
        pass

class Peixe(Animal):
    def locomove(self):
        print("Um peixe nada.")

class Elefante(Animal):
    def locomove(self):
        print("Um elefante anda.")

class Passaro(Animal):
    def locomove(self) -> bool:
        print("Um pássaro voa.")
        return True

def animal_moveu(animal: Animal):
    animal_moveu = animal.locomove()
    if animal_moveu:
        print('Animal se moveu') 
    
    
ave = Passaro()

animal_moveu(ave)