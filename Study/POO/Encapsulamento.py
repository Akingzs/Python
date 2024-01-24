# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

# Definindo a classe Foo
class Foo:
    # Método construtor da classe
    def __init__(self):
        # Atributo público
        self.public = 'isso é público'
        # Atributo protegido (por convenção)
        self._protected = 'isso é protegido'
        # Atributo privado (por convenção)
        self.__exemplo = 'isso é private'

    # Método público
    def metodo_publico(self):
        # Acessando o atributo privado
        print(self.__exemplo)
        # Chamando o método privado
        self.__metodo_private()
        return 'metodo_publico'

    # Método protegido (por convenção)
    def _metodo_protected(self):
        print('_metodo_protected')
        return '_metodo_protected'

    # Método privado (por convenção)
    def __metodo_private(self):
        print('__metodo_private')
        return '__metodo_private'

# Criando um objeto da classe Foo
f = Foo()
# Chamando o método público
print(f.metodo_publico())
