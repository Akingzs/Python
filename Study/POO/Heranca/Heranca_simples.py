
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def show_info(self):
        return print(f'{self.nome} {self.sobrenome} é um/uma {self.__class__.__name__}')

class Professor(Pessoa):
    ...

class Aluno(Pessoa):
    ...

professor1 = Professor('Arthur','Reis')
professor1.show_info()

aluno1 = Aluno('Ricardo','Menezes')
aluno1.show_info()

help(Aluno) 
# -> Method Resolution Order (MRO) Aluno-> Pessoa->buitin.obj 