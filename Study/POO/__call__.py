class Exemplo:
    def __init__(self):
        self.contador = 0

    def __call__(self):
        self.contador += 1
        print(f'Esta instância foi chamada {self.contador} vezes.')

    def show(self):
        print('Metodo Show chamado')
# Criando uma instância da classe Exemplo
exemplo = Exemplo()

# Agora podemos "chamar" a instância como se fosse uma função
exemplo()
exemplo()
exemplo.show()