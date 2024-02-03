# Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
# Criar um sistema bancário (extremamente simples) que tem clientes, contas e
# um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
# possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
from abc import ABC, abstractmethod
import random

class Conta(ABC):
    
    def __init__(self, limite_conta: int | float = 0) -> None:
        self._limite_conta = limite_conta
        self._agencia = 0 #random.randint(0,1)
        self._numero_conta = random.randint(1000,9999)
    
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
    
class Banco():
    
    def __init__(self, contas:list[Conta], clientes:list[Pessoa]) -> None:
        self._contas = contas
        self._clientes = clientes
        # O meu banco trabalha apenas com as contas que tem agencia 0
        self._banco_agencia = 0    


    def autenticar(self,conta,cliente):
        if conta in self._contas:
            if conta._agencia == 0:
                if cliente in self._clientes:
                    print('Voce pode sacar nesse banco')
                    return True
            else:
                print('Voce nao pode sacar nesse banco')
        
        

            
        
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


conta_arthur = Conta_Corrente(1000)
conta2 = Conta_Corrente(4000)
conta3 = Conta_Corrente(500)
lista_contas = [conta_arthur,conta2,conta3]

arthur, luanna = (Pessoa('ARTHUR',24),Pessoa('LUANNA',24))
lista_clientes = [arthur,luanna]
# print(conta_arthur._limite_conta)

# conta_arthur.sacar(200)
# conta_arthur.depositar(500)

banco0 = Banco(lista_contas,lista_clientes)

auth = banco0.autenticar(conta_arthur,arthur)

if auth:
    conta_arthur.sacar(200)
