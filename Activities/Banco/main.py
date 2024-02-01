# Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
# Criar um sistema bancário (extremamente simples) que tem clientes, contas e
# um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
# possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
from abc import ABC, abstractmethod

class Conta(ABC):
    
    def __init__(self, limite_conta: int | float = 0) -> None:
        self._limite_conta = limite_conta
    
    @abstractmethod
    def sacar(self, valor_saque: int | float):
        self._limite_conta -= valor_saque
        return self._limite_conta 
    
    @abstractmethod
    def depositar(self, valor_deposito: int | float):
        self._limite_conta += valor_deposito
        return self._limite_conta 
    
    
class Pessoa(ABC):
    
    def __init__(self, nome: str, idade:int) -> None:
        self._nome = nome
        self._idade = idade
        
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return self._idade
    
    
class Cliente(Pessoa):
    
    def __init__(self, nome: str, idade: int, conta) -> None:
        super().__init__(nome, idade)
        self._conta = conta
    

class Conta_Corrente(Conta):
    
    def __init__(self, limite_conta: int | float = 0) -> None:
        limite_extra_CC = limite_conta * 1.2
        super().__init__(limite_extra_CC)
    
    def sacar(self, valor_saque: int | float):
        retorno = super().sacar(valor_saque)
        print(f'Saque conta Corrente no valor de {valor_saque}\nNovo saldo: {self._limite_conta}')
        return retorno
        
    def depositar(self, valor_deposito: int | float):
        retorno = super().depositar(valor_deposito)
        print(f'Saque conta Corrente no valor de {valor_deposito}\nNovo saldo: {self._limite_conta}')
        return retorno
    
class Conta_Poupanca(Conta):
    
    def __init__(self, limite_conta: int | float = 0) -> None:
        super().__init__(limite_conta)
    
    def sacar(self, valor_saque: int | float):
        retorno = super().sacar(valor_saque)
        print(f'Saque conta Corrente no valor de {valor_saque}\nNovo saldo: {self._limite_conta}')
        return retorno
        
    def depositar(self, valor_deposito: int | float):
        retorno = super().depositar(valor_deposito)
        print(f'Saque conta Corrente no valor de {valor_deposito}\nNovo saldo: {self._limite_conta}')
        return retorno
    
# p = Cliente('Arthur',14,)
# print(p.idade)

conta_arthur = Conta_Corrente(1000)
print(conta_arthur._limite_conta)

conta_arthur.sacar(200)
conta_arthur.depositar(500)
