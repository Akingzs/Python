# Relações entre classes: associação, agregação e composição
# Associação é um tipo de relação onde os objetos
# estão ligados dentro do sistema.
# Essa é a relação mais comum entre objetos e tem subconjuntos
# como agregação e composição (que veremos depois).
# Geralmente, temos uma associação quando um objeto tem
# um atributo que referencia outro objeto.
# A associação não especifica como um objeto controla
# o ciclo de vida de outro objeto.
# Definindo a classe Escritor
class Escritor:
    # Método construtor da classe
    def __init__(self, nome) -> None:
        self.nome = nome  # Nome do escritor
        self._ferramenta = None  # Ferramenta de escrita inicialmente não definida

    # Getter para a ferramenta de escrita
    @property
    def ferramenta(self):
        return self._ferramenta

    # Setter para a ferramenta de escrita
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta  # Define a ferramenta de escrita
    
    def mostrar_acao(self):
        return f'O Escritor {self.nome} esta escrevendo com {self._ferramenta.nome}'

# Definindo a classe FerramentaDeEscrever
class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome  # Nome da ferramenta de escrita

    # Método para escrever
    def escrever(self):
        return f'{self.nome} está escrevendo'  # Retorna a ação de escrita

# Criando um objeto da classe Escritor
escritor = Escritor('Luiz')

# Criando objetos da classe FerramentaDeEscrever
caneta = FerramentaDeEscrever('Caneta Bic')
maquina_de_escrever = FerramentaDeEscrever('Máquina de escrever')

# Definindo a ferramenta de escrita do escritor usando associacao de classes
escritor.ferramenta = maquina_de_escrever

# Imprimindo a ação de escrita das ferramentas
print(caneta.escrever())
print(maquina_de_escrever.escrever())

# Imprimindo a ação de escrita da ferramenta do escritor
print(escritor.ferramenta.escrever())
print(escritor.mostrar_acao())