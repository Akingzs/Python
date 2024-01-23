# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯

class Caneta:
    def __init__(self, cor=None):
        # Atributos privados da classe Caneta. 
        # O prefixo '_' indica que eles não devem ser acessados diretamente.
        self._cor = cor
        self._cor_tampa = None

    @property
    def cor(self):
        # Este é o getter para o atributo 'cor'. 
        # Quando você tenta acessar o atributo 'cor' de uma instância de Caneta, 
        # este método é chamado.
        print('ESTOU NO GETTER')
        return self._cor

    @cor.setter
    def cor(self, valor):
        # Este é o setter para o atributo 'cor'. 
        # Quando você tenta atribuir um valor ao atributo 'cor' de uma instância de Caneta, 
        # este método é chamado.
        print('ESTOU NO SETTER COR')
        self._cor = valor

    @property
    def cor_tampa(self):
        # Este é o getter para o atributo 'cor_tampa'.
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        # Este é o setter para o atributo 'cor_tampa'.
        print('ESTOU NO SETTER TAMPA')
        self._cor_tampa = valor

# Cria uma instância de Caneta com a cor 'Azul'
caneta = Caneta('Azul')

# Cria uma instância de Caneta sem cor definida
caneta_rosa = Caneta()

# Define a cor da caneta_rosa como 'Rosa' usando o setter
caneta_rosa.cor = 'Rosa'

# Define a cor da tampa da caneta como 'Azul' usando o setter
caneta.cor_tampa = 'Azul'

# Imprime a cor da caneta usando o getter
print(caneta.cor)

# Imprime a cor da tampa da caneta usando o getter
print(caneta.cor_tampa)

# Os getters e setters permitem que você controle como os atributos de uma instância são acessados e modificados. 
# Eles são úteis quando você quer fazer algo além de simplesmente obter ou definir o valor de um atributo, 
# como validar o valor de entrada ou imprimir uma mensagem quando o atributo é acessado. 