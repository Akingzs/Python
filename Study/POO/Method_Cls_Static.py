# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

# class Connection:
#     def __init__(self, host='localhost'):
#         self.host = host
#         self.user = None
#         self.password = None

#     def set_user(self, user):
#         self.user = user

#     def set_password(self, password):
#         self.password = password

#     @classmethod
#     def create_with_auth(cls, user, password):
#         connection = cls()
#         connection.user = user
#         connection.password = password
#         return connection

#     @staticmethod
#     def log(msg):
#         print('LOG:', msg)


# def connection_log(msg):
#     print('LOG:', msg)


# # c1 = Connection()
# c1 = Connection.create_with_auth('luiz', '1234')
# # c1.set_user('luiz')
# # c1.set_password('123')
# print(Connection.log('Essa é a mensagem de log'))
# print(c1.user)
# print(c1.password)


# exemplo CHAT GPT 

class Carro:
    lista_carros = []  # lista para armazenar todas as instâncias de Carro

    def __init__(self, nome, cor, ano):
        self.nome = nome
        self.cor = cor
        self.ano = ano
        self.lista_carros.append(self)  # adiciona a instância à lista de carros

    # tem acesso ao namespace da classe, e nao tem dos atributos
    @classmethod
    def todos_os_carros(cls):
        return cls.lista_carros  # retorna a lista de todos os carros
    
    # Nao tem acesso aos atributos e nem ao namespace da funçao, geralmente fica dentro da classe apenas por organização 
    @staticmethod
    def verifica_ano_valido(ano):
        return 1886 <= ano <= 2024  # retorna True se o ano for válido, False caso contrário


carro1 = Carro('argo','red',2021)
carro2 = Carro('fusca','blue',2020)

    # Chama o método de classe para obter a lista de todos os carros
todos_carros = Carro.todos_os_carros()

    # Imprime as informações de cada carro
for carro in todos_carros:
    print(f"Nome: {carro.nome}, Cor: {carro.cor}, Ano: {carro.ano}")
    # Caso tente executar o print a seguir ira apenas imprimir cada estancia da classe e o espaco da memoria alocado
    # print(carro.nome)